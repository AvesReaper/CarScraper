import json
import os
from confluent_kafka import Consumer

from app.utils.datacleaner import etl
from app.datapusher import sendtodb

kafka_host =  os.getenv("KAFKA_HOST","localhost:9092")

consumer = Consumer(
    {
        "bootstrap.servers": kafka_host,
        "group.id": "car-cleaner",
        "auto.offset.reset": "earliest",
    }
)

consumer.subscribe(["cars"])

print("Waiting for messages...")

while True:

    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        print(msg.error())
        continue

    data = json.loads(msg.value().decode())

    cleaned_data = etl(data)

    print("response from api: ",sendtodb(cleaned_data))
