import json
import requests
requests.packages.urllib3.disable_warnings()

HOST = '192.168.56.107'
PORT = '443'
USER = 'cisco'
PASS = 'cisco123!'

url_base = "https://{h}/restconf".format(h=HOST)
headers = {'Content-Type': 'application/yang-data+json',
 'Accept':'application/yang-data+json'}

def get_ip():
    url = url_base + "/data/ietf-interfaces:interfaces"
    response = requests.get(url,
                            auth=(USER, PASS),
                            headers=headers,
                            verify=False
                            )

    data = response.json()["ietf-interfaces:interfaces"]["interface"][1]["ietf-ip:ipv4"]["address"][0]

    try:
        IP = data["ip"]
    except KeyError:
        print("Json Error")

    return IP