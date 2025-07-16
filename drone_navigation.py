import airsim
import time

client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

client.takeoffAsync().join()
client.moveToPositionAsync(10, 0, -5, 3).join()
client.hoverAsync().join()

print("Navigation complete.")
client.landAsync().join()
client.armDisarm(False)
client.enableApiControl(False)
