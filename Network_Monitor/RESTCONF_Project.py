import json
import requests
requests.packages.urllib3.disable_warnings()

HOST = '192.168.56.105'
PORT = '443'
USER = 'cisco'
PASS = 'cisco123!'

url_base = "https://{h}/restconf".format(h=HOST)
headers = {'Content-Type': 'application/yang-data+json',
 'Accept':'application/yang-data+json'}

def get_routing_protocol():
    url = url_base + "/data/ietf-routing:routing-state"
    response = requests.get(url,
                            auth=(USER, PASS),
                            headers=headers,
                            verify=False
                            )

    data = response.json()["ietf-routing:routing-state"]["routing-instance"][0]
    route1 = response.json()["ietf-routing:routing-state"]["routing-instance"][0]["routing-protocols"]["routing-protocol"][0]
    route2 = response.json()["ietf-routing:routing-state"]["routing-instance"][0]["routing-protocols"]["routing-protocol"][1]
    route3 = response.json()["ietf-routing:routing-state"]["routing-instance"][0]["routing-protocols"]["routing-protocol"][2]
    route4 = response.json()["ietf-routing:routing-state"]["routing-instance"][0]["routing-protocols"]["routing-protocol"][3]

    print("Routing Protocols:")
    try:
        routingProtocol1 = route1["type"]
        routingProtocol2 = route2["type"]
        routingProtocol3 = route3["type"]
        routingProtocol4 = route4["type"]
        routerId = data["router-id"]
    except KeyError:
        print("Json Error")

    print("Router ID: "+routerId)
    print("Routing Protocol 1: "+routingProtocol1)
    print("Routing Protocol 2: "+routingProtocol2)
    print("Routing Protocol 3: "+routingProtocol3)
    print("Routing Protocol 4: "+routingProtocol4)

get_routing_protocol()