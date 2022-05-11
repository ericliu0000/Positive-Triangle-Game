from manim import *
from util import *


class Ladder(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        w = int(input())

        graph = Graph(TriangleLadder.generate_vertices(w),
                TriangleLadder.generate_edges(w),
                layout="spring").scale(1.5)
        graph.set_color(BLACK)

        # Make graph and text
        self.play(Create(graph))

