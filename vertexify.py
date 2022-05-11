from manim import *


class DualPlusPlus(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        w = int(input())

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

        for i in range(n):
            for j in range(i, n):
                if i == j:
                    continue
                edges.append((i, j))

        print(edges)
        return edges