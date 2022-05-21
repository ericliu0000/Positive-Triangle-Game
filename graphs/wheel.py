from manim import *
from sys import argv

class WheelGraph(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        try:
            w = int(argv[-1])
        except ValueError as e:
            w = 4
            print("last argument specifies number of vertices")

        graph = Graph(self.generate_vertices(w),
                      self.generate_edges(w),
                      layout="kamada_kawai").scale(1.5)
        graph.set_color(BLACK)

        # Make graph and text
        self.play(Create(graph))

    def generate_vertices(self, n):
        return [i for i in range(n)]

    def generate_edges(self, n):
        edges = [(1, n - 1)]

        # Generate outer cycles
        for i in range(1, n - 1):
            edges.append((i, i + 1))

        # Generate "spokes"
        for i in range(1, n):
            edges.append((0, i))

        return edges
