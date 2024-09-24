import paho.mqtt.client as mqtt
import json
import streamlit as st
import time
import sqlite3

class Utils:
    def __init__(self, cursor):
        self.cursor = cursor
        self.mqtt_client = None
        
    if 'device_positions' not in st.session_state:
        st.session_state['device_positions'] = {}

    # Get the color based on device status
    def get_device_color(self, status):
        if status == 'connected':
            return 'green'
        elif status == 'disconnected':
            return 'red'
        else:
            return 'orange'

    # Logic to allow moving devices on the dashboard
    def drag_and_drop(self, devices):
        for index, device in enumerate(devices):
            new_x = st.number_input(f"X Position for {device['name']}", value=device['x_position'], key=f"x_pos_{device['id']}_{index}")
            new_y = st.number_input(f"Y Position for {device['name']}", value=device['y_position'], key=f"y_pos_{device['id']}_{index}")

            if st.button(f"Update {device['name']} Position", key=f"update_pos_{device['id']}_{index}"):
                self.update_device_position(device['id'], new_x, new_y)
                st.success(f"{device['name']} position updated to ({new_x}, {new_y})")

            # Optionally update the session state to track updated positions
            if device['id'] in st.session_state['device_positions']:
                new_x, new_y = st.session_state['device_positions'][device['id']]

                
    # Update device position in the database
    def update_device_position(self, device_id, new_x, new_y):
        retries = 5
        while retries > 0:
            try:
                self.cursor.execute("UPDATE devices SET x_position=?, y_position=? WHERE id=?", (new_x, new_y, device_id))
                # Optionally, update the session state to reflect the new position
                if 'device_positions' not in st.session_state:
                    st.session_state['device_positions'] = {}
                st.session_state['device_positions'][device_id] = (new_x, new_y)  
                st.success(f"Position updated for device {device_id}")
                break  # Break if successful
            except sqlite3.OperationalError as e:
                if 'database is locked' in str(e):
                    time.sleep(0.1)  # Wait before retrying
                    retries -= 1
                else:
                    raise  # Reraise if it's a different error
        else:
            st.error("Failed to update device position after multiple attempts.")


    # Connect to MQTT broker
    def connect_mqtt(self):
        if not self.mqtt_client:
            self.mqtt_client = mqtt.Client()
            self.mqtt_client.connect('test.mosquitto.org', 1883)
            st.success("Connected to MQTT broker")
        return self.mqtt_client

    # Publish a message to a topic (MQTT)
    def publish_mqtt_message(self, topic, payload):
        if not self.mqtt_client:
            self.mqtt_client = self.connect_mqtt()
        message = json.dumps(payload)
        self.mqtt_client.publish(topic, message)
        st.info(f"Message sent to {topic}: {message}")

    # Subscribe to a topic and print the message received (MQTT)
    def subscribe_mqtt_topic(self, topic):
        if not self.mqtt_client:
            self.mqtt_client = self.connect_mqtt()

        def on_message(client, userdata, message):
            decoded_message = str(message.payload.decode("utf-8"))
            st.write(f"Message received from {topic}: {decoded_message}")

        self.mqtt_client.subscribe(topic)
        self.mqtt_client.on_message = on_message
        self.mqtt_client.loop_start()
        st.success(f"Subscribed to topic: {topic}")
    
