from manim import *
from sys import argv


class Ladder(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        try:
            w = int(argv[-1])
        except ValueError as e:
            w = 4
            print("last argument specifies number of vertices")

        # TODO: layout is ugly. please fix
        graph = Graph(self.generate_vertices(w),
                      self.generate_edges(w),
                      layout="spring").scale(1.5)
        graph.set_color(BLACK)

        # Make graph and text
        self.play(Create(graph))

    def generate_vertices(self, n):
        # if (n % 2):
        #     return
        return [i + 1 for i in range(n)]

    def generate_edges(self, n):
        # if (n % 2):
        #     return
        edges = [(1, n)]

        # Generate outer cycle
        for i in range(1, n):
            edges.append((i, i + 1))

        # Generate vertical spokes
        if n >= 6:
            for i in range(2, int(n / 2), 2):
                edges.append((i, n - i + 1))

        # Generate diagonals
        if n >= 4:
            for i in range(1, int(n / 2)):
                edges.append((i, n - i))

        return edges
