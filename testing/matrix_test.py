from manim import *


class MatrixTest(Scene):
    def construct(self):
        m = Matrix([[8, 0, 0, 0, 0], [0, 4, 0, 0, 0], [0, 0, 4, 0, 0], [0, 0, 0, 4, 0], [0, 0, 0, 0, 4]]).shift(UP + RIGHT * 3.25)
        next = MathTex("\\frac{1}{2}")

        self.play(Create(m))

        self.wait(2)
        
        self.play(ReplacementTransform(m, next))

        self.wait(3)
