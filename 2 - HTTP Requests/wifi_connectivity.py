import network

def connect(network_ssid, network_pass):
    sta_if = network.WLAN(network.STA_IF)
    
    if not sta_if.isconnected():
        print('Connecting to the network...')
        sta_if.active(True)
        sta_if.connect(network_ssid, network_pass)
        while not sta_if.isconnected():
            pass
        
    print('network config:', sta_if.ifconfig())