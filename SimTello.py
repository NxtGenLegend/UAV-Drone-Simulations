import time
from djitellopy import Tello

# Create Tello object
tello = Tello()

# Connect to Tello simulator and enable simulation mode
tello.connect()
tello.enable_simulation_mode()

# Main program loop
while True:
    try:
        # Get current position of the drone
        position = tello.get_position()
        latitude = position[0]
        longitude = position[1]
        altitude = position[2]

        # Print the coordinates
        print("Latitude:", latitude)
        print("Longitude:", longitude)
        print("Altitude:", altitude)

        # Delay between position updates
        time.sleep(1)

    except KeyboardInterrupt:
        # Land and disconnect if program interrupted by user
        tello.land()
        tello.end()
        break
