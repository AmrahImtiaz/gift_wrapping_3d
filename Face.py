from Edge import Edge


class Face:
    def __init__(self, p1, p2, p3):
        self.points = [p1, p2, p3]

    def edges(self):
        """Get the edges of the face as a list of Edge objects."""
        edges = []
        for i in range(3):
            edges.append(Edge(self.points[i], self.points[(i + 1) % 3]))
        return edges

    # requires that edge is in the face
    def other_point(self, edge):
        """Given an edge of the face, return the third point not present in the edge."""
        ls = [edge.start, edge.end]
        for i in range(3):
            if self.points[i] not in ls:
                return self.points[i]

        return self.points[0]

    def __eq__(self, other):
        """Check if two faces are equal (have the same points)."""
        return set(self.points) == set(other.points)

    def __hash__(self):
        """Calculate the hash value for the face."""
        return (hash(self.points[0]) + hash(self.points[1]) ** 2 + hash(self.points[2]) ** 3) % 100
