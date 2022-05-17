from manim import *
from sys import argv

class ComplexGraph(Scene):
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
        edges = []

        # Draw edge between evey vertex
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    continue
                edges.append((i, j))

        return edges
