# ⚙️ Setup Instructions

## 1. Environment Requirements
- Windows 10 or 11 (64-bit)
- Unreal Engine 4.27+
- AirSim plugin installed
- Python 3.11+
- GPU with at least 6GB VRAM (for smooth simulation)

## 2. Unreal + AirSim Setup
1. Download and set up [AirSim](https://github.com/microsoft/AirSim).
2. Create a forest or wildlife environment in Unreal.
3. Enable the AirSim plugin and configure the simulation settings.

## 3. Python Dependencies

```bash
pip install opencv-python ultralytics pandas numpy
```

## 4. Clone Repo and Run
```bash
git clone https://github.com/yourusername/autonomous-ai-drones-wildlife-monitoring.git
cd scripts/
python drone_navigation.py
```

## 5. Notes
- Simulation was conducted on a college workstation with a dedicated RTX GPU.
- This repository contains mock outputs for demonstration only.
