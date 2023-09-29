# Import KafkaProducer from Kafka library
from kafka import KafkaProducer

# Define server with port
bootstrap_servers = ['localhost:29092']

# Define topic name where the message will publish
topicName = 'test'

# Initialize producer variable
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

# Publish text in defined topic
producer.send(topicName, b'Hello Kafka...')

# Print message
print("Message Sent")