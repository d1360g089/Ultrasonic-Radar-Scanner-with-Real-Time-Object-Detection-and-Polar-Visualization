# Ultrasonic Radar Scanner with Real-Time Object Detection and Polar Visualization

This project implements an ultrasonic radar system capable of real-time object detection, distance tracking, and angular scanning using a servo-mounted sensor. The system combines Arduino-based hardware control with a Python-powered polar visualization interface for intuitive feedback and target analysis. 

## 🧠 Project Overview

The core hardware consists of an HC-SR04 ultrasonic distance sensor mounted on a servo motor, allowing for angular scanning from 0° to 180°. The Arduino handles sensor triggering, servo control, and distance measurement, while simultaneously outputting angle-distance pairs via serial communication. The system also integrates a 16x2 LCD display to provide real-time distance and angle readings, along with a buzzer that alerts the user when an object is detected within a critical threshold.

On the software side, the data is received by a Python script that plots polar coordinates in real time using Matplotlib. The visualization features:
- A sweep line representing the scanning angle
- Scatter points representing detected distances
- A highlighted marker for the closest object
- Cluster detection using angle-distance proximity to reduce noise

This radar visualization mimics real-world tracking systems by clustering spatially close data points and locking onto the closest object with a dynamic green marker. The interface also includes live textual annotations for current scan data and locked object distance, providing clarity in rapidly changing environments.

Through this project, I deepened my understanding of real-time embedded systems, serial communication protocols, servo motor actuation, and ultrasonic sensing. On the software side, I gained experience with data visualization, cluster-based analysis for signal noise reduction, and using Python libraries like Matplotlib and NumPy for hardware-integrated applications. This project also provided practical experience in integrating multi-modal feedback systems (visual, textual, audio) for responsive robotics applications.

---

## 🛠️ Hardware Components
- Arduino Uno
- HC-SR04 Ultrasonic Sensor
- SG90 Servo Motor
- 16x2 LCD Display (with I2C or parallel interface)
- Buzzer
- Breadboard and jumper wires
- USB Serial Cable

---

## 🧾 Files Included
- radarscanner.ino -> arduino file controls the hardware
- radarscanner.py -> python file controls the graphing and object detection alogrithms
  

---

## 📸 Demo
![radar-demo](demo.gif)  
[📺 Watch Demo Video](https://youtu.be/your-link-here)

---

## 📡 Features
- 180° ultrasonic scanning
- Real-time polar radar graph
- Closest-object locking algorithm using clustering
- Dynamic sweep line and object highlighting
- LCD readout for range and angle
- Buzzer alerts for close proximity detection

---

## 🔬 Concepts and Skills Learned
- Real-time sensor integration and timing control
- Serial communication between Arduino and Python
- Servo actuation and angular control
- Noise reduction using cluster-based analysis
- Data visualization using polar coordinates
- Embedded systems debugging and visualization synchronization

---

## 🚀 Future Improvements
- Add object tracking across frames to detect motion
- Implement smoothing filter for distance data
- Upgrade to a 360° scanning system using a continuous rotation servo
- Add obstacle mapping or SLAM-style logging

---

## 📁 Folder Structure
