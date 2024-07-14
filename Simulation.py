from dronekit import connect, VehicleMode, LocationGlobal
import dronekit_sitl
import time
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()

# tcp:127.0.0.1:5760
drone = connect(connection_string, wait_ready=True)

drone_status = drone.is_armable
system_status = drone.system_status.state
battery = drone.battery
location = drone.gps_0
mode = drone.mode.name
target_alt = 10

print(battery, location, mode, drone.location.global_frame)

drone.mode = VehicleMode("GUIDED")
drone.armed = True
drone.airspeed = 5
drone.simple_takeoff(target_alt)

while True:
    print(drone.location.global_frame.alt)
    if drone.location.global_relative_frame.alt >= target_alt * 0.95: # Break after target altitude is attained
        break
    time.sleep(2)

print(drone.location.global_relative_frame)

time.sleep(2)

waypoint1 = LocationGlobal(10, 15, 20)
drone.simple_goto(waypoint1)

time.sleep(10)

print(drone.location.global_relative_frame)

#drone.mode = VehicleMode("RTL") # RTL = Return To Launch

drone.close()

sitl.stop()