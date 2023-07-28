"""
convex_hull.py

Implements the gift wrapping algorithm to compute the convex hull of a 3D point cloud.

The main entry point is the gift_wrapping() function.
"""
import queue
import numpy as np

from Edge import Edge
from Face import Face
from Point import Point


def dot_product(a, b):
    """Calculate the dot product of two points (a and b)."""
    return a.x * b.x + a.y * b.y + a.z * b.z


def project(a, b):
    """Project point 'a' onto the direction vector 'b'."""
    length = dot_product(a, b)
    return Point(length * b.x, length * b.y, length * b.z)


def cross_product(a, b):
    """Calculate the cross product of two points 'a' and 'b'."""
    aa = [a.x, a.y, a.z]
    bb = [b.x, b.y, b.z]

    c = np.cross(aa, bb)
    return Point(c[0], c[1], c[2])


def merge(e1, e2):
    """Merge two lists of edges while removing any duplicate edges."""
    result = e1
    for e in e2:
        if e in e1:
            result.remove(e)
        elif e.reverse() in e1:
            result.remove(e.reverse())
        else:
            result.append(e)
    return result


def find_lowest_point(points):
    """Find the lowest point in a list of points (based on their z, y, and x coordinates respectively)."""
    best_point = points[0]
    for p in points[1:]:
        if p < best_point:
            best_point = p

    return best_point


def find_next_point(points, p1, p2):
    """Find the next point that forms the convex hull with p1 and p2."""
    if p2 is None:
        p2 = p1 - Point(1, 1, 0)

    edge = p2 - p1

    best_point = None
    for p in points:
        if p not in [p1, p2]:
            if best_point is None:
                best_point = p
            else:
                # The volume is positive if p is to the left of the plane defined by the triangle (p1,p2,best_point)
                # This means p is a better choice than before.

                # These vector calculations give the singed volume of the tetrahedron (p1, p2, best_point, p).
                v = p - p1
                v = v - project(v, edge)

                u = best_point - p1
                u = u - project(u, edge)

                cross = cross_product(u, v)
                if dot_product(cross, edge) > 0:
                    best_point = p
    return best_point


def gift_wrapping(points):
    """Gift Wrapping algorithm to find the convex hull of a set of 3D points."""
    hull = []

    # Queue of edges and list of edges processed
    edges_available = queue.Queue()
    edges_processed = []

    # A function to create an edge indicating that it has been processed. 
    # If the reverse of this edge has not been processed before, then add that to the queue.
    def add_edge(e):
        """Add an edge to the list of processed edges and add its reverse to the queue if not already processed."""
        edges_processed.append(e)
        if e.reverse() not in edges_processed:
            edges_available.put(e.reverse())

    # Find the first edge
    fp1 = find_lowest_point(points)
    fp2 = find_next_point(points, fp1, None)

    add_edge(Edge(fp2, fp1))

    while not edges_available.empty():
        edge = edges_available.get()
        p1 = edge.start
        p2 = edge.end

        if edge not in edges_processed:
            # Get next point
            p3 = find_next_point(points, p1, p2)

            # Add the face to the convex hull, and its edges to the queue.
            hull.append(Face(p1, p2, p3))
            add_edge(Edge(p1, p2))
            add_edge(Edge(p2, p3))
            add_edge(Edge(p3, p1))

    return hull
