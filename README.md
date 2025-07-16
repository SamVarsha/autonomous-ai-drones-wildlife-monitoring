
# 🛰️ Autonomous AI Drones for Wildlife Monitoring (AirSim Simulation)

This project simulates an autonomous drone system equipped with AI-powered vision for wildlife monitoring, using Microsoft's AirSim and Unreal Engine. The primary objective is to develop a virtual testbed where drones can detect and track wildlife in real time within a synthetic environment, supporting conservation and anti-poaching efforts.

## 🔍 Key Objectives

- Simulate drone-based wildlife surveillance.
- Integrate YOLOv8 for animal detection.
- Enable autonomous navigation using AirSim APIs.
- Log and visualize detection results.

## 🧠 Technologies Used

- **AirSim** – For simulating drones in Unreal environments.
- **Unreal Engine** – Custom forest environment.
- **Python 3.11+** – Core programming language.
- **YOLOv8** – For object detection.
- **OpenCV, NumPy, Pandas** – For processing and analysis.

## 📂 Folder Structure

```
├── README.md            # Project overview and instructions
├── SETUP.md             # Step-by-step setup instructions
├── settings.json        # AirSim simulation settings
├── scripts/             # Python scripts for detection & navigation
│   ├── drone_navigation.py
│   ├── animal_detection.py
│   └── data_logger.py
├── media/               # Demo videos or screenshots
│   ├── demo.gif
│   └── screenshots/
│       ├── detection_view.png
│       └── simulation_view.png
```

## 🚀 Features

- Real-time animal detection using YOLOv8.
- Autonomous flight path execution via AirSim API.
- Configurable drone behavior and camera feeds.
- Sample outputs and detection logs.

## 📽️ Demo Preview

If a video is available, upload to YouTube and link here. Otherwise, use media/demo.gif for basic visualization.

## 👨‍💻 Author

**Bunny** – This project was developed using college infrastructure with high-end GPU systems to support AirSim simulations.
