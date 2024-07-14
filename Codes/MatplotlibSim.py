import matplotlib.pyplot as plt

# Define drone parameters
mass = 1.0  # Mass of the drone
initial_position = [0.0, 0.0]  # Initial position of the drone
initial_velocity = [0.0, 0.0]  # Initial velocity of the drone

# Set simulation parameters
simulation_time = 10.0  # Total simulation time
time_step = 0.1  # Time step for each iteration

# Initialize variables
position = initial_position
velocity = initial_velocity
acceleration = [0.0, 0.0]
simulation_time = 0.0

# Lists to store position data
x_values = [position[0]]
y_values = [position[1]]

# Simulation loop
while simulation_time <= simulation_time:
    # Calculate control inputs
    thrust = 1.0  # Thrust force applied to the drone

    # Update acceleration, velocity, and position
    acceleration[0] = thrust / mass
    velocity[0] += acceleration[0] * time_step
    position[0] += velocity[0] * time_step

    # Store position data
    x_values.append(position[0])
    y_values.append(position[1])

    # Increment simulation time
    simulation_time += time_step

# Plot the trajectory
plt.plot(x_values, y_values)
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('Drone Trajectory')
plt.grid(True)
plt.show()