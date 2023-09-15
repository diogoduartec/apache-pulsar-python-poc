# Apache Pulsar with Python - POC


## Setup Standalone Apache Pulsar with docker-compose
```bash
docker-compose -f docker-compose-standalone.yml up -d
```

## Dependencies
### If you prefer using poetry
https://python-poetry.org/
```bash
poetry shell
poetry install
```

### If you prefer using venv
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Python Client Approach
### Run Consumer
Make sure the env is activated and run consumer
```bash
python client_consumer.py
```

### Run Producer (in a new tab)
Make sure the env is activated and run producer
```bash
python client_producer.py
```
### Expected result (left side consumer, right side producer)
![image](https://github.com/diogoduartec/apache-pulsar-python-poc/assets/31852339/3d196606-043e-47b2-b5da-fc9a005f1f37)

## Websocket Approach
### Run Consumer
Make sure the env is activated and run consumer
```bash
python websocket_consumer.py
```

### Run Producer (in a new tab)
Make sure the env is activated and run producer
```bash
python websocket_producer.py
```
### Expected result (left side consumer, right side producer)
![image](https://github.com/diogoduartec/apache-pulsar-python-poc/assets/31852339/62989575-9913-42b3-94bb-7c0a9483cf50)
