import requests
import json
import websocket

HOST = 'http://octopi.local'

HEADERS = {
    'X-Api-Key': '73CAD071FD664D26A858210F92EA95BF',
}

ENDPOINT = '/api/version';

#r = requests.get('https://www.somecompany.com/api/v2/groups/', headers=headers)

REQ = requests.get(HOST+ENDPOINT, headers=HEADERS)
print(REQ.text)

ENDPOINT = '/api/printer?history=true&limit=2';

REQ = requests.get(HOST+ENDPOINT, headers=HEADERS)
print(REQ.text)
RJSON = REQ.json()
print("Bed: " + json.dumps(RJSON['temperature']['bed']['actual']) + "℃")
print("Hot: " + json.dumps(RJSON['temperature']['tool0']['actual']) + "℃")
#print(REQ.text)
