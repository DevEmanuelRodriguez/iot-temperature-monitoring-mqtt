# 🌡️ IoT Temperature Monitoring System (MQTT)

Real-time temperature monitoring system using MQTT protocol, Python-based sensor simulation, and a Node-RED dashboard for visualization.

The system demonstrates event-driven communication between devices using a publish/subscribe architecture.

---

## ✨ Features

* Real-time temperature data streaming
* MQTT publish/subscribe communication
* Python-based sensor simulation
* Node-RED dashboard for visualization
* Lightweight and scalable architecture

---

## 🧱 Tech Stack

* Python (sensor simulation)
* MQTT
* Eclipse Mosquitto
* Node-RED

---

## 🏗️ Architecture

* Python script publishes temperature data
* Mosquitto acts as MQTT broker
* Node-RED subscribes to topic and displays data
* Dashboard shows real-time updates

---

## ⚙️ Setup

### 1. Start Mosquitto broker

```bash id="p1kqz6"
mosquitto
```

---

### 2. Run Python sensor

```bash id="v3ksd9"
python sensor.py
```

---

### 3. Start Node-RED

```bash id="v5kzq2"
node-red
```

Access dashboard at:

```id="g9k2l1"
http://localhost:1880/ui
```

---

## 📸 Application Preview

*(Add dashboard screenshot here)*

---

## 📌 Notes

This project demonstrates IoT communication using MQTT and event-driven architecture, commonly used in real-world monitoring systems.
