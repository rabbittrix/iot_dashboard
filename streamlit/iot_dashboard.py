import streamlit as st
import sqlite3
from turtle_draw import draw_device_icon
from devices_handler import get_devices, update_device_status, configure_device
from mqtt_handler import connect_mqtt, send_mock_data
from websocket_handler import init_websocket
from utils import Utils
from mock_devices import generate_mock_devices

# Create a connection to the SQLite database
conn = sqlite3.connect('devices.db')
cursor = conn.cursor()

# Create devices table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT,
    status TEXT DEFAULT 'unconfigured',
    x_position INTEGER DEFAULT 0,
    y_position INTEGER DEFAULT 0,
    config JSON DEFAULT '{}'
)
''')

if __name__ == "__main__":
    # Other initializations...
    init_websocket()

# MQTT Connection
client = connect_mqtt()
client.loop_start()

# Initialize Websocket (this will start the websocket server)
init_websocket()

# Check if mock devices should be used
if st.checkbox('Use Mock Devices'):
    devices = generate_mock_devices()
else:
    devices = get_devices(cursor)

# Display devices in the dashboard
for index, device in enumerate(devices):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(f"Device: {device['name']} - {device['type']}")
        draw_device_icon(device['type'], Utils(cursor).get_device_color(device['status']))
    with col2:
        st.write(f"Status: {device['status']}")
    with col3:
        if st.button('Configure', key=f'configure_{device["id"]}_{index}'):
            update_device_status(cursor, device['id'], 'connected')
            configure_device(cursor, device['id'])
        if st.button('Connect', key=f'connect_{device["id"]}_{index}'):
            update_device_status(cursor, device['id'], 'connected')


# Send mock data using MQTT
if st.button('Send Mock Data'):
    send_mock_data(client)

# Allow dragging and dropping devices
Utils(cursor).drag_and_drop(devices)

# Commit changes to the database and close the connection
conn.commit()
conn.close()
