import json
from confluent_kafka import Producer
import os


kafka_host =  os.getenv("KAFKA_HOST","localhost:9092")
producer = Producer(
    {
        "bootstrap.servers": kafka_host
    }
)


def delivery_report(err, msg):
    if err:
        print(err)
    else:
        print(f"Produced -> {msg.topic()} [{msg.partition()}]")


def publish(data: dict):

    producer.produce(
        topic="cars",
        value=json.dumps(data),
        callback=delivery_report,
    )

    producer.poll(0)