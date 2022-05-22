from manim import *
from constants import *
from graphs.wheel import WheelGraph
import util


class AdjacencyMatrix(Scene):
    wheel = WheelGraph()
    mat_val = [0, 0, 0, 0, 0]

    def construct(self):
        text = f"""The cubed adjacency matrix of <span {GRAPH_COLOR}>W<sub>5</sub></span>
        shows the number of triangles it has.
        #
        At each vertex, there are two closed 
        walks of length 3 to itself,
        # 
        representing a triangle.
        
        #
        This occurs 3 times in a triangle, where
        6 closed walks of length 3 are created.
        #
        The number of triangles is therefore the
        the sum of the main diagonal divided by 6.
        """

        text_objects = util.text_generator(text, DOWN * 1.5)

        numerator = MathTex("24").shift(UP + RIGHT * 3.25)
        comb = MathTex("\\frac{24}{6}").shift(UP + RIGHT * 3.25)
        result = MathTex("\\frac{24}{6} = 4").shift(UP + RIGHT * 3.25)

        g = Graph(self.wheel.generate_vertices(5),
                  self.wheel.generate_edges(5),
                  layout="kamada_kawai",
                  labels={0: "1", 1: "2", 2: "3", 3: "4", 4: "5"}).shift(UP + LEFT * 3.5)

        # Make initial matrix and store previous matrix
        m = self.make_a3()

        # Create graph and text
        self.play(Create(g))
        self.play(Create(text_objects[0][0]), Create(text_objects[0][1]))
        self.play(Create(m))

        # Cycle text
        self.play(ReplacementTransform(text_objects[0][0], text_objects[1][0]),
                  ReplacementTransform(text_objects[0][1], text_objects[1][1]))

        self.wait(SHORT_DWELL_TIME)

        # Cycle text
        self.play(ReplacementTransform(text_objects[1][0], text_objects[2][0]),
                  ReplacementTransform(text_objects[1][1], text_objects[2][1]))

        # Expand vertex 1 and show paths
        self.play(g.vertices[0].animate(run_time=BRIEF_ANIMATION_TIME).set_fill(PURE_RED))

        v0_options = [
            [(0, 4), (1, 4), (0, 1)],
            [(0, 1), (1, 4), (0, 4)],
            [(0, 1), (1, 2), (0, 2)],
            [(0, 2), (1, 2), (0, 1)],
            [(0, 2), (2, 3), (0, 3)],
            [(0, 3), (2, 3), (0, 2)],
            [(0, 3), (3, 4), (0, 4)],
            [(0, 4), (3, 4), (0, 3)]
        ]

        for option in v0_options:
            # Blink a triangle in sequence
            util.bulk_play(self, *[Indicate(g.edges[i], run_time=SHORT_ANIMATION_TIME, color=PURE_BLUE, rate_func=rate_functions.rush_into) for i in option])

            # Update matrix and return graph color
            next = self.make_a3(0, 1)
            self.play(ReplacementTransform(m, next, run_time=SHORT_ANIMATION_TIME))
            m = next

            util.recolor(self, g, [edge for entry in v0_options for edge in entry], WHITE)

        self.play(g.vertices[0].animate(run_time=BRIEF_ANIMATION_TIME).set_fill(WHITE))

        # Indicate resulting triangle patterns
        for i in range(1, 5):
            # Color and decolor vertices
            self.play(g.vertices[i - 1].animate(run_time=BRIEF_ANIMATION_TIME).set_fill(WHITE, 0.7),
                      g.vertices[i].animate(run_time=BRIEF_ANIMATION_TIME).set_fill(PURE_RED))

            edges = [v0_options[2 * (i - 1) % 8], v0_options[2 * (i) % 8]]

            for edge in edges:
                util.bulk_indicate(self, g, edge, run_time=ANIMATION_TIME, color=PURE_BLUE, include_vertices=False)

                # Update matrix
                next = self.make_a3(i)
                self.play(ReplacementTransform(m, next, run_time=SHORT_ANIMATION_TIME))
                m = next

        # Clear last dot
        self.play(g.vertices[4].animate(run_time=BRIEF_ANIMATION_TIME).set_fill(WHITE, 0.7))

        # Cycle text
        self.play(ReplacementTransform(text_objects[2][0], text_objects[3][0]),
                  ReplacementTransform(text_objects[2][1], text_objects[3][1]))

        # Swap matrix to 24
        self.play(ReplacementTransform(m, numerator))

        self.wait(SHORT_DWELL_TIME)

        # Swap 24 to 24/6
        self.play(ReplacementTransform(numerator, comb))

        # Cycle text
        self.play(ReplacementTransform(text_objects[3][0], text_objects[4][0]),
                  ReplacementTransform(text_objects[3][1], text_objects[4][1]))

        # Swap 24/6 to 24/6 = 4
        self.play(ReplacementTransform(comb, result))

        # Blink all four triangles
        for i in range(0, 8, 2):
            util.bulk_indicate(self, g, v0_options[i], include_vertices=False)

        # Deconstruct everything
        self.play(Uncreate(text_objects[4][0]), Uncreate(text_objects[4][1]))
        self.play(Uncreate(result), Uncreate(g))

        self.wait(SHORT_DWELL_TIME)

    def make_a3(self, sel=-1, inc=2):
        original = Matrix([[self.mat_val[j] if i == j and self.mat_val[j] > 0 else "\\square" for i in range(5)] for j in range(5)]).shift(UP + RIGHT * 3.25)

        if sel < 0:
            return original

        self.mat_val[sel] += inc

        return Matrix([[self.mat_val[j] if i == j and self.mat_val[j] > 0 else "\\square" for i in range(5)] for j in range(5)]).shift(UP + RIGHT * 3.25)

    def test(self, text_objects):
        # Cycle all text
        self.play(Create(text_objects[0][0]), Create(text_objects[0][1]))

        self.wait(SHORT_DWELL_TIME)

        self.play(ReplacementTransform(text_objects[0][0], text_objects[1][0]),
                  ReplacementTransform(text_objects[0][1], text_objects[1][1]))

        self.wait(SHORT_DWELL_TIME)

        self.play(ReplacementTransform(text_objects[1][0], text_objects[2][0]),
                  ReplacementTransform(text_objects[1][1], text_objects[2][1]))

        self.wait(SHORT_DWELL_TIME)

        self.play(ReplacementTransform(text_objects[2][0], text_objects[3][0]),
                  ReplacementTransform(text_objects[2][1], text_objects[3][1]))

        self.wait(SHORT_DWELL_TIME)

        self.play(ReplacementTransform(text_objects[3][0], text_objects[4][0]),
                  ReplacementTransform(text_objects[3][1], text_objects[4][1]))
