import paho.mqtt.client as mqtt
import json
import streamlit as st

def connect_mqtt(broker_url='test.mosquitto.org', port=1883):
    client = mqtt.Client()
    client.connect(broker_url, port)
    st.success(f"Connected to MQTT broker at {broker_url}:{port}")
    return client

def publish_mqtt_message(client, topic, payload):
    message = json.dumps(payload)
    client.publish(topic, message)
    st.info(f"Message sent to {topic}: {message}")
    
def subscribe_mqtt_topic(client, topic):
    def on_message(client, userdata, message):
        decoded_message = str(message.payload.decode("utf-8"))
        st.write(f"Message received from {topic}: {decoded_message}")
        
    client.subscribe(topic)
    client.on_message = on_message
    st.info(f"Subscribed to {topic}")
    client.loop_start()
    st.success(f"Subscribed to topic: {topic}")
    
def send_mock_data(client):
    payload = {
        'device_id': 'mock_device',
        'temperature': 25,
        'humidity': 60
    }
    publish_mqtt_message(client, 'iot_data', payload)
    
def handle_mqtt():
    client = connect_mqtt()
    send_mock_data(client)
    subscribe_mqtt_topic(client, 'iot_data')
    
if __name__ == '__main__':
    handle_mqtt()