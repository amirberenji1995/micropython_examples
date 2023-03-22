import urequests
import ujson
import gc

from wifi_connectivity import connect

network_ssid = 'amirhosseinb'
network_pass = 'B09121793316a'
getUrl = 'https://reqres.in/api/unknown/2'
postUrl = 'https://reqres.in/api/users'

if __name__ == '__main__':
    print('\n\nStarting with WIFI Connectivity\n')
    connect(network_ssid, network_pass)
    print('\nChecking Get Request')
    getResponse = urequests.get(url = getUrl)
    print('Get Request Response Code : ', getResponse.status_code)
    del(getResponse)
    gc.collect()
    print('\nChecking Post Request')
    postResponse = urequests.post(url = postUrl,
                                  data = ujson.dumps({
                                                    "name": "morpheus",
                                                    "job": "leader"
                                                }))
    print('Post Request Response Code : ', postResponse.status_code)
