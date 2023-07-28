class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def length(self):
        """Calculate the length of the edge vector."""
        return self.vector().length()

    def vector(self):
        """Calculate the edge vector, from start to end."""
        return self.end - self.start

    def __eq__(self, other):
        """Check if two edges are equal (have the same start and end points)."""
        return (self.start == other.start) and (self.end == other.end)

    def reverse(self):
        """Create a new edge with reversed start and end points."""
        return Edge(self.end, self.start)
