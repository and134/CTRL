# CTRL — Autonomous Raspberry Pi Car

CTRL is an open-source autonomous car project built around a **Raspberry Pi 3B**. It supports both **Manual** and **Automatic** driving modes, line-following logic, and a responsive web interface for remote control.

---

## Features

* **Manual Mode**: control forward, backward, left, right, and stop via web UI
* **Automatic Mode**: line-following using digital IR sensors (configurable with 1 or 3 sensors)
* **Mode Toggle**: switch between Manual and Automatic in the UI
* **Servo Steering**: PWM‑controlled MG995 servo for precise direction
* **Wi‑Fi Browser Control**: lightweight Flask server for real‑time commands

---

## 🛠️ Hardware Components

* **Raspberry Pi 3B**
* **2× DC Motors** (Tamiya 70097 Twin‑Motor Gearbox)
* **L298N Dual H‑Bridge Driver**
* **MG995 Servo Motor** for steering
* **IR Line‑Tracking Sensor(s)** (1–3) digital output
* **HC‑SR04 Ultrasonic Sensor** (optional obstacle avoidance)
* **External 6V battery pack** for motors
* **5V 3A power supply** for Raspberry Pi

---

## 💾 Software Requirements

* Raspberry Pi OS (64‑bit)
* Python 3.x
* Flask (`pip install flask`)
* RPi.GPIO

---

## 🚀 Installation & Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/and134/CTRL.git
   cd CTRL
   ```
2. **Create a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**:

   ```bash
   pip install flask RPi.GPIO
   ```
4. **Start the server**:

   ```bash
   python3 web_control.py
   ```
5. **Open your browser** on any device in the same Wi‑Fi network:

   ```
   http://<raspberry_pi_ip>:5000
   ```

---

## 🎮 Usage

1. **Manual Mode**: Ensure mode toggle is set to **Manual**, then use the arrow buttons to drive.
2. **Automatic Mode**: Switch to **Automatic**, car will start line‑following logic.
3. **Emergency Stop**: Press **Stop** button or switch back to Manual.
