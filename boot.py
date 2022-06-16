import network
import esp
esp.osdebug(None)
import gc

gc.collect()

conn_type = 'AP'

if conn_type == 'STA':
    print('station')
    ssid = 'YOURSSID'
    password = 'PASSWORD'

    station = network.WLAN(network.STA_IF)

    station.active(True)
    station.connect(ssid, password)

    while station.isconnected() == False:
        pass
    is_connected = True
else:
    print('ap')
    ssid = 'Electric'
    password = '12345678910'

    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.ifconfig(('192.168.0.1', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
    ap.config(essid=ssid, password=password)

    while ap.active() == False:
        pass
    is_connected = True    

    print('Connection successful')
    print(ap.ifconfig())


def web_page():
    html = """<html><head> <title>Motor Boat</title> <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
    border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1> 
    <!--<p><a href="/on"><button class="button">ON</button></a></p>-->
    <p><a href="/off"><button class="button">OFF</button></a></p>
    <p><a href="/forw"><button class="button">FORWARD</button></a></p>
    <p><a href="/back"><button class="button">BACK</button></a></p>
    <p><a href="/left"><button class="button">LEFT</button></a></p>
    <p><a href="/right"><button class="button">RIGHT</button></a></p>
    </body></html>"""
    return html
