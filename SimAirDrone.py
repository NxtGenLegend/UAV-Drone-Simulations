import airsim

# Connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()

# Set the initial state of the drone
initial_state = client.getMultirotorState()

# Get the initial location coordinates
initial_location = initial_state.kinematics_estimated.position
initial_x, initial_y, initial_z = initial_location.x_val, initial_location.y_val, initial_location.z_val

print("Initial Location:")
print("X: ", initial_x)
print("Y: ", initial_y)
print("Z: ", initial_z)

# Takeoff
client.takeoffAsync().join()

# Get the post-takeoff state of the drone
post_takeoff_state = client.getMultirotorState()

# Get the post-takeoff location coordinates
post_takeoff_location = post_takeoff_state.kinematics_estimated.position
post_takeoff_x, post_takeoff_y, post_takeoff_z = post_takeoff_location.x_val, post_takeoff_location.y_val, post_takeoff_location.z_val

print("\nPost-Takeoff Location:")
print("X: ", post_takeoff_x)
print("Y: ", post_takeoff_y)
print("Z: ", post_takeoff_z)