from dronekit import connect, VehicleMode
import dronekit_sitl
import time

# Start SITL
sitl = dronekit_sitl.start_default()

# Connect to the simulated vehicle
connection_string = sitl.connection_string()
vehicle = connect(connection_string, wait_ready=True)

# Arm the vehicle and take off
print("Arming motors")
vehicle.mode = VehicleMode("GUIDED")
vehicle.airspeed = 1
vehicle.armed = True
vehicle.simple_takeoff(10)  # Take off to an altitude of 10 meters

# Wait until the vehicle reaches the target altitude
while True:
    print("Altitude: {0}".format(vehicle.location.global_relative_frame.alt))
    if vehicle.location.global_relative_frame.alt >= 10 * 0.95:
        print("Target altitude reached")
        break
    time.sleep(1)

# Land the vehicle
print("Landing")
vehicle.mode = VehicleMode("LAND")

# Wait for the vehicle to land
while vehicle.armed:
    print("Waiting for vehicle to land")
    time.sleep(1)

# Close the connection and stop the SITL simulation
vehicle.close()
sitl.stop()
