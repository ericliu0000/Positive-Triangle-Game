from manim import *


class MatrixTest(Scene):
    def construct(self):
        m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        self.play(Create(m))

        ms = [Matrix([[1, i, 3], [4, 5, 6], [7, 8, 9]]) for i in range(10)]

        last_m = m

        for mat in ms:
            self.play(ReplacementTransform(last_m, mat), run_time=0.2)
            last_m = mat
            self.wait(0.2)