import os
import sys
import time
import requests
from prometheus_client import start_http_server, Gauge

# Check if required environment variables are set
required_env_vars = ["RABBITMQ_HOST", "RABBITMQ_USER", "RABBITMQ_PASSWORD"]
missing_vars = [var for var in required_env_vars if not os.getenv(var)]

if missing_vars:
    print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
    sys.exit(1)

# Environment variables
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_USER = os.getenv("RABBITMQ_USER")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")

# Fetch interval in seconds (default to 10 if not set)
FETCH_INTERVAL = int(os.getenv("FETCH_INTERVAL", "10"))

# Prometheus metrics
QUEUE_MESSAGES = Gauge(
    "rabbitmq_individual_queue_messages",
    "Total count of messages in the queue",
    ["host", "vhost", "name"]
)
QUEUE_MESSAGES_READY = Gauge(
    "rabbitmq_individual_queue_messages_ready",
    "Count of messages ready in the queue",
    ["host", "vhost", "name"]
)
QUEUE_MESSAGES_UNACKNOWLEDGED = Gauge(
    "rabbitmq_individual_queue_messages_unacknowledged",
    "Count of unacknowledged messages in the queue",
    ["host", "vhost", "name"]
)

def fetch_queue_metrics():
    """
    Fetch queue metrics from RabbitMQ Management API.
    """
    url = f"http://{RABBITMQ_HOST}:15672/api/queues"
    auth = (RABBITMQ_USER, RABBITMQ_PASSWORD)

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        queues = response.json()

        for queue in queues:
            vhost = queue["vhost"]
            name = queue["name"]
            messages = queue["messages"]
            messages_ready = queue["messages_ready"]
            messages_unacknowledged = queue["messages_unacknowledged"]

            # Set Prometheus metrics
            QUEUE_MESSAGES.labels(host=RABBITMQ_HOST, vhost=vhost, name=name).set(messages)
            QUEUE_MESSAGES_READY.labels(host=RABBITMQ_HOST, vhost=vhost, name=name).set(messages_ready)
            QUEUE_MESSAGES_UNACKNOWLEDGED.labels(host=RABBITMQ_HOST, vhost=vhost, name=name).set(messages_unacknowledged)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching metrics from RabbitMQ: {e}")

def main():
    """
    Start the Prometheus exporter and periodically fetch metrics.
    """
    # Start Prometheus HTTP server
    start_http_server(8000)
    print(f"RabbitMQ Prometheus exporter started on port 8000 with a fetch interval of {FETCH_INTERVAL} seconds")

    while True:
        fetch_queue_metrics()
        time.sleep(FETCH_INTERVAL)  # Fetch metrics every FETCH_INTERVAL seconds

if __name__ == "__main__":
    main()