import pika
from django.conf import settings


class RabbitMQClient:
    def __init__(self, host, port, username, password):
        self.connection_params = pika.ConnectionParameters(
            host=host,
            port=port,
            credentials=pika.PlainCredentials(username, password),
            heartbeat=0,
            blocked_connection_timeout=300,
        )
        self.connection = None
        self.channel = None

    def connect(self):
        self.connection = pika.BlockingConnection(self.connection_params)
        self.channel = self.connection.channel()

    def send_message(self, exchange, routing_key, message):
        self.channel.basic_publish(
            exchange=exchange, routing_key=routing_key, body=message
        )

    def close_connection(self):
        if self.connection and self.connection.is_open:
            self.connection.close()


rabbitmq_client = RabbitMQClient(**settings.RABBITMQ_CREDS)
rabbitmq_client.connect()
rabbitmq_client.channel.queue_declare(queue="sales_queue")
