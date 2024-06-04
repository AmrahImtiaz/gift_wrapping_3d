import matplotlib.animation as animation
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.colors as colors
from convex_hull import gift_wrapping, Point
from random import randint

def generate_random_points(num_points, max_coord):
    xs = [randint(0, max_coord) for _ in range(num_points)]
    ys = [randint(0, max_coord) for _ in range(num_points)]
    zs = [randint(0, max_coord) for _ in range(num_points)]
    labels = ["(" + str(x) + "," + str(y) + "," + str(z) + ")" for x, y, z in zip(xs, ys, zs)]

    return [xs, ys, zs, labels]

def get_hull_faces(points):
    P = []
    for j in range(len(points[0])):
        P.append(Point(points[0][j], points[1][j], points[2][j]))

    c_hull = gift_wrapping(P)
    return c_hull

def update(frame, points, hull):
    ax.clear()
    ax.set_xlabel('X Axis', fontsize=14, color='green')
    ax.set_ylabel('Y Axis', fontsize=14, color='green')
    ax.set_zlabel('Z Axis', fontsize=14, color='green')
    
    ax.scatter3D(points[0], points[1], points[2])
    
    for p in range(len(points[3])):
        ax.text(points[0][p], points[1][p], points[2][p], points[3][p], ha='center')
    
    triangles = []
    for c in range(frame+1):
        x = [hull[c].points[0].x, hull[c].points[1].x, hull[c].points[2].x]
        y = [hull[c].points[0].y, hull[c].points[1].y, hull[c].points[2].y]
        z = [hull[c].points[0].z, hull[c].points[1].z, hull[c].points[2].z]
        tri_points = list(zip(x, y, z))
        triangles.append(tri_points)
    
    tri3d = art3d.Poly3DCollection(triangles)
    tri3d.set_color(colors.rgb2hex([0.5, 0.5, 0.5]))
    tri3d.set_alpha(0.3)
    ax.add_collection3d(tri3d)

if __name__ == "__main__":
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(projection='3d')

    nrange = 60
    npoints = 10  # Change to desired number of points

    points = generate_random_points(npoints, nrange)
    hull = get_hull_faces(points)

    ani = animation.FuncAnimation(fig, update, frames=len(hull), fargs=(points, hull), interval=1000, repeat=False)

    plt.show()
