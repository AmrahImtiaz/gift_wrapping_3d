import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint

# Global variables
fig, ax = plt.subplots()
ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000)

def generate_random_points(num_points):
    return [[randint(300, 700), randint(300, 700)] for _ in range(num_points)]

def animate(frame):
    ax.clear()
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)
    for i in range(frame):
        ax.plot(pointList[i][0], pointList[i][1], 'bo')
    # Add the current line being considered in QuickHull
    if frame > 1:
        ax.plot([pointList[frame-2][0], pointList[frame-1][0]], [pointList[frame-2][1], pointList[frame-1][1]], 'r-')

def quickhull(points):
    if len(points) <= 1:
        return points
    else:
        # Your QuickHull implementation here
        pass

# Generate random points
pointList = generate_random_points(20)

# Run QuickHull algorithm
# Replace this with your actual QuickHull implementation
quickhull(pointList)

# Animate the steps
ani = animation.FuncAnimation(fig, animate, frames=len(pointList)+1, interval=1000)
plt.show()
