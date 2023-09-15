import websocket, base64, json

TOPIC = 'ws://localhost:8080/ws/v2/producer/persistent/public/default/testtopic'


ws = websocket.create_connection(TOPIC)

message = 'Hello World'
encodedBytes = base64.b64encode(message.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")

ws.send(json.dumps({
    'payload' : encodedStr,
    'properties': {
        'key1' : 'value1',
        'key2' : 'value2'
    },
    'context' : 5
}))

response =  json.loads(ws.recv())
if response['result'] == 'ok':
    print ('Message published successfully')
else:
    print ('Failed to publish message:', response)

ws.close()
