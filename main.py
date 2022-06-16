# DOCUMENTATION
# ampy --port COM3 --baud 115200 put .\main.py
#import your stuff
from machine import Pin, PWM
from time import sleep
try:
    import usocket as socket
except:
    import socket

from boot import is_connected, web_page #, some other var


#set the parameters
FREQUENCY = 1000
SPEED_LOW = 0
SPEED_HIGH = 512
BUILT_IN_LED_D4 = PWM(Pin(2), FREQUENCY) #builtin led
MOTOR1_DIRECTION_D1 = PWM(Pin(5), FREQUENCY) #motor1 direction
MOTOR1_SPEED_D2 = PWM(Pin(4), FREQUENCY) #motor1 speed 
MOTOR2_DIRECTION_D5 = PWM(Pin(14), FREQUENCY) #motor2 direction
MOTOR2_SPEED_D6 = PWM(Pin(12), FREQUENCY) #motor2 speed

BUILT_IN_LED_D4.duty(0)
MOTOR1_DIRECTION_D1.duty(0)
MOTOR1_SPEED_D2.duty(0)
MOTOR2_DIRECTION_D5.duty(0)
MOTOR2_SPEED_D6.duty(0)

# create http server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 80))
server.listen(5)


while True:
# if WIFI turn on builtin led
  if is_connected:
    BUILT_IN_LED_D4.duty(512)    
    conn, addr = server.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    if request.find('/on') == 6:
      response = 'ON'
    elif request.find('/off') == 6:
      response = 'OFF'
      MOTOR1_DIRECTION_D1.duty(0)
      MOTOR1_SPEED_D2.duty(0)
      MOTOR2_DIRECTION_D5.duty(0)
      MOTOR2_SPEED_D6.duty(0)
    elif request.find('/forw') == 6:
      response = 'FORWARD'
      MOTOR1_DIRECTION_D1.duty(512)
      MOTOR1_SPEED_D2.duty(1023)
      MOTOR2_DIRECTION_D5.duty(512)
      MOTOR2_SPEED_D6.duty(1023)
    elif request.find('/back') == 6:
      response = 'BACK'
      MOTOR1_DIRECTION_D1.duty(1023)
      MOTOR1_SPEED_D2.duty(512)
      MOTOR2_DIRECTION_D5.duty(1023)
      MOTOR2_SPEED_D6.duty(512)      
    elif request.find('/left') == 6:
      response = 'LEFT'
      MOTOR1_DIRECTION_D1.duty(0)
      MOTOR1_SPEED_D2.duty(0)
      MOTOR2_DIRECTION_D5.duty(512)
      MOTOR2_SPEED_D6.duty(1023)
    elif request.find('/right') == 6:
      response = 'RIGHT'
      MOTOR1_DIRECTION_D1.duty(512)
      MOTOR1_SPEED_D2.duty(1023)
      MOTOR2_DIRECTION_D5.duty(0)
      MOTOR2_SPEED_D6.duty(0)
    else:
      response = 'NO MATCH'  
# return a response to the browser
    print(response)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(web_page())
    conn.close()
  else:
    BUILT_IN_LED_D4.duty(0)  