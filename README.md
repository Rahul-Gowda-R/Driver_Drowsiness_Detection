# 🚗 Driver Drowsiness Detection System

A real-time computer vision system that detects driver drowsiness using facial features such as eye closure, yawning, and driver presence. The system provides immediate alerts to improve road safety.

---

## 📌 Overview

Driver fatigue is one of the leading causes of road accidents. This project aims to monitor the driver continuously using a webcam and detect signs of drowsiness in real-time.

The system combines **OpenCV** and **MediaPipe** to analyze facial behavior and trigger alerts when unsafe conditions are detected.

---

## ⚙️ Features

* 👀 **Eye Closure Detection**

  * Detects if eyes remain closed for a prolonged period
  * Triggers *DROWSY* alert with sound

* 😮 **Yawning Detection (MediaPipe)**

  * Uses facial landmarks to measure mouth opening
  * More accurate than traditional methods

* 🚫 **Driver Not Detected**

  * Detects absence of driver from camera
  * Triggers alert if face is not visible

* 🔊 **Audio Alerts**

  * Real-time sound alerts using system beeps

* 🎥 **Live Video Processing**

  * Processes webcam feed in real-time

---

## 🧠 Technologies Used

* **Python 3.10**
* **OpenCV** – Face and eye detection
* **MediaPipe** – Facial landmark detection
* **NumPy** – Numerical operations
* **Winsound** – Audio alerts (Windows)

---

## 🏗️ System Architecture

```text
Webcam → Frame Capture → Face Detection → 
    ├── Eye Detection → Drowsiness Check
    ├── MediaPipe → Yawning Detection
    └── Face Presence → Driver Detection
→ Alert System (Sound + Text)
```

---

## 🚀 How It Works

### 1. Face Detection

* Uses Haar Cascade classifier to detect face region
* Defines region of interest (ROI)

### 2. Eye Detection

* Detects eyes inside face ROI
* If eyes are not detected for multiple frames:
  → Driver is considered drowsy

---

### 3. Yawning Detection (MediaPipe)

* Detects facial landmarks (lips)
* Calculates distance between upper and lower lip
* If mouth opens beyond threshold:
  → Yawning detected

---

### 4. Driver Presence Detection

* If no face is detected for a period:
  → “Driver Not Detected” alert

---

### 5. Alert Mechanism

* Visual alerts using OpenCV text overlay
* Audio alerts using system beep

---

## 📂 Project Structure

```text
Driver-Drowsiness-Detection/
│
├── Driver Drowsiness Detection.py
├── haarcascade_frontalface_default.xml
├── haarcascade_eye.xml
├── README.md
```

---

## ⚡ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/driver-drowsiness-detection.git
cd driver-drowsiness-detection
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install opencv-python==4.8.0.76
pip install mediapipe==0.10.11
pip install numpy==1.24.4
```

---

## ▶️ Run the Project

```bash
python "Driver Drowsiness Detection.py"
```

---

## 🎯 Results

* Real-time detection of:

  * Drowsiness ✔
  * Yawning ✔
  * Driver absence ✔

* System responds instantly with alerts

---

## ⚠️ Limitations

* Haar Cascade eye detection may fail in:

  * Low lighting
  * Extreme head angles

* Requires webcam access

* Yawning threshold may vary per user

---

## 🚀 Future Improvements

* 🔥 Replace eye detection with MediaPipe (EAR calculation)
* 🎤 Add voice-based alerts instead of beep
* 📊 Add logging system for driver behavior
* 📱 Convert into mobile application
* 🌙 Improve night-time detection

---

## 💡 Applications

* Smart vehicles
* Driver monitoring systems
* Fleet safety systems
* AI-based surveillance

---

## 👨‍💻 Author

**Rahul Gowda R**
Computer Science Engineering Student

---

## 📜 License

This project is for educational and research purposes.

---

# ⭐ Final Note

This project demonstrates the integration of **Computer Vision + Real-time Processing + Safety Systems**, making it a strong addition to portfolios and interviews.

