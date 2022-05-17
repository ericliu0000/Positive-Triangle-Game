from manim import *
from sys import argv


class TriangleLadderGraph(Scene):
    SPACING = 1

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
                      layout=self.generate_layout(w))
        graph.set_color(BLACK)

        # Make graph and text
        self.play(Create(graph))

        for i in range(w):
            self.play(Indicate(graph.vertices[i + 1]))
            self.wait(0.5)

    def generate_vertices(self, n):
        return [i + 1 for i in range(n)]

    def generate_edges(self, n):
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

        print(edges)
        return edges


    def generate_layout(self, n):
        layout = {}

        x_list = [(self.SPACING / 2) - (n / (4 / self.SPACING)) + (i * self.SPACING) for i in range(int(n / 2) + 1)]

        for i in range(int(n / 2)):
            layout[i + 1] = (x_list[i], self.SPACING / 2, 0)
        for i in range(int(n / 2), n):
            layout[i + 1] = (x_list[(n - i - 1)], -self.SPACING / 2, 0)

        print(layout)
        return layout
