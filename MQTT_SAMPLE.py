import paho.mqtt.client as mqtt
import json
import base64

# MQTT Broker configuration
broker = "broker.hivemq.com"
port = 1883
topic = "home/livingroom/image"  # Choose any topic

# Create an MQTT client instance
client = mqtt.Client("ImagePublisher")

# Connect to the MQTT broker
client.connect(broker, port, 60)

# Read the image file in binary mode and encode it using Base64
with open("sample.jpg", "rb") as image_file:
    image_data = image_file.read()
    # Encode binary data to Base64 string and decode bytes to UTF-8 string
    encoded_data = base64.b64encode(image_data).decode('utf-8')

# Create a JSON object with the Base64 encoded image data
payload = json.dumps({"image": encoded_data})

# Publish the JSON payload to the MQTT topic
client.publish(topic, payload=payload)
print("Published JSON payload with encoded image data to topic:", topic)

# Disconnect the client
client.disconnect()
