from manim import *


class Vertexify(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        w = int(input())

        graph = Graph(self.generate_vertices(w),
                self.generate_edges(w),
                layout="kamada_kawai").scale(1.5)
        graph.set_color(BLACK)

        # Make graph and text
        self.play(Create(graph))

