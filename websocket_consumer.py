import websocket, base64, json

#token='TOKEN'

#authHeader = 'Bearer ' + token

TOPIC = 'ws://localhost:8080/ws/v2/consumer/persistent/public/default/testtopic/my-subscription'

#ws = websocket.create_connection(TOPIC, header={"Authorization": authHeader})
ws = websocket.create_connection(TOPIC)

while True:
    msg = json.loads(ws.recv())
    if not msg: break

    print ("Received: {} - payload: {}".format(msg, base64.b64decode(msg['payload'])))

    # Acknowledge successful processing
    ws.send(json.dumps({'messageId' : msg['messageId']}))

ws.close()

