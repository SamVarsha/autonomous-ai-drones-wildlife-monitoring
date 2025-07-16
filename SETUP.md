
# ⚙️ SETUP.md – Detailed Setup Instructions

## ✅ Prerequisites

- Windows 10/11 (64-bit)
- Python 3.11+
- Unreal Engine 4.27+
- Git (for cloning repo)
- GPU with at least 6GB VRAM (recommended for smooth simulation)

## 🔧 1. Installing Unreal Engine

1. Download and install [Epic Games Launcher](https://www.unrealengine.com/en-US/download).
2. Launch it and install **Unreal Engine 4.27**.

## 📦 2. Clone and Setup AirSim

```bash
git clone https://github.com/microsoft/AirSim.git
cd AirSim
./setup.sh
./build.sh
```

## 🌲 3. Create or Import Forest Environment

1. Open Unreal Editor.
2. Create a new project using "Blank" template.
3. Enable **AirSim plugin** (Edit → Plugins → Search "AirSim").
4. Import assets for forest or wildlife terrain from Marketplace.
5. Place static animal models if needed.

## ⚙️ 4. Configure AirSim (settings.json)

Place `settings.json` in your `Documents/AirSim/` folder:

```json
{
  "SettingsVersion": 1.2,
  "SimMode": "Multirotor",
  "Vehicles": {
    "Drone1": {
      "VehicleType": "SimpleFlight",
      "X": 0, "Y": 0, "Z": 0,
      "Cameras": {
        "front_center": {
          "CaptureSettings": [
            {
              "ImageType": 0,
              "Width": 640,
              "Height": 480,
              "FOV_Degrees": 90
            }
          ],
          "X": 0.5, "Y": 0, "Z": -0.2
        }
      }
    }
  }
}
```

## 🐍 5. Install Python Dependencies

```bash
pip install opencv-python ultralytics pandas numpy
```

## 🚁 6. Run the Drone Navigation

```bash
cd scripts/
python drone_navigation.py
```

## 🦌 7. Run Animal Detection

```bash
python animal_detection.py
```

## 📝 8. Log the Detected Animals

```bash
python data_logger.py
```

---

Now you're ready to simulate autonomous AI drones for wildlife monitoring!
