import websocket, base64, json

#token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTY5NDcyMDI2MiwiZXhwIjoxNjk0NzYzNDYyfQ.Pie3zfT8X5XZRBjUlMpKfGQ489BysIFEv-0CVgrWiiQ'

#authHeader = 'Bearer ' + token

#TOPIC = 'wss://pulsar.example.com:8001/ws/v2/producer/persistent/public/local-pulsar/test-topic'
TOPIC = 'ws://localhost:8080/ws/v2/producer/persistent/public/default/testtopic'


#ws = websocket.create_connection(TOPIC, header={"Authorization": authHeader})
ws = websocket.create_connection(TOPIC)

message = 'Hello World'
encodedBytes = base64.b64encode(message.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
# Send one message as JSON
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

