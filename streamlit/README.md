# IoT Device Dashboard with WebSockets, MQTT, and Advanced Configurations

# Project Structure
    iot_dashboard/
    │
    ├── iot_dashboard.py           # Main Streamlit application file
    ├── devices_handler.py         # Handles device configuration and connection
    ├── matplotlib_ploty.py        # Module for Turtle graphics (device icons)
    ├── mqtt_handler.py            # Handles MQTT communication
    ├── websocket_handler.py       # Handles WebSocket communication
    ├── mock_devices.py            # Mock for simulating devices
    ├── devices.db                 # SQLite database for storing device states
    ├── utils.py                   # Utility functions managing the dashboard
    ├── requirements.txt           # Project dependencies
    └── README.md                  # Documentation of the project

## Overview

    This enhanced version of the IoT dashboard now supports **WebSockets** and **MQTT** for real-time communication. Each IoT device, such as ESP32 and sensors, can be monitored and configured with advanced settings, allowing dynamic interaction with devices. The system can also simulate devices using mock data for testing.

### Features
    - **WebSocket and MQTT Communication**: Real-time data exchange between the dashboard and devices.
    - **Advanced Device Configuration**: Configure thresholds, alerts, and other settings for each device.
    - **Mock Devices**: Test the dashboard using simulated devices.
    - **Responsive Design**: Works on mobile, tablet, and desktop.
    - **Device Status**: Real-time status updates (green for connected, red for disconnected, orange for unconfigured).
    - **Drag-and-Drop**: Reposition devices on the dashboard.
    - **Device Icons**: Custom icons for each device using Turtle graphics.

### Requirements

    - Python 3.x
    - Streamlit
    - Turtle
    - paho-mqtt
    - websockets
    - SQLite

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rabbittrix/iot_dashboard.git

2. Install dependencies:
    pip install -r requirements.txt
    pip freeze > requirements.txt

3. Run the application:
    streamlit run iot_dashboard.py

Using Mock Devices
    Check the "Use Mock Devices" box in the UI to simulate devices for testing. Mock devices will be displayed with default configurations.

Sending Mock Data
    Press the "Send Mock Data" button to simulate sending device data via MQTT.

WebSocket Communication
    The WebSocket client connects to the default server URL (ws://example.com/iot) and handles real-time communication for connected devices.

Advanced Configurations
    Each device can be configured with thresholds and alert settings using the advanced configuration panel.

## Future Improvements
    * Add support for more device types.
    * Implement a richer UI for managing device configurations.
    * Enable more real-time protocols like CoAP.


### Dependencies (`requirements.txt`)
    streamlit turtle sqlite3 paho-mqtt websockets


### Como rodar o projeto

1. Clone o repositório e instale as dependências:
   ```bash
   git clone https://github.com/rabbittrix/iot_dashboard.git
   cd iot_dashboard
   pip install -r requirements.txt

2. Execute o dashboard:
    streamlit run iot_dashboard.py

3. To test with mock devices, select the "Use Mock Devices" checkbox.

# Another POC made by the team https://www.kr-so.com