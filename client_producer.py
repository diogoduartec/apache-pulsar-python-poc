import pulsar
import time

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('my-topic')

for i in range(10):
    time.sleep(3)
    producer.send(('hello-pulsar-%d' % i).encode('utf-8'))

client.close()
