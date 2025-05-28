import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 100)
scat = ax.scatter([], [])

# Define the update function
def update(frame):
    x = np.random.rand(20) * 10
    print(type(x))
    y = np.random.rand(20) * 100
    print(y)
    scat.set_offsets(np.c_[x, y])
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=500)

# Display the animation
plt.show()