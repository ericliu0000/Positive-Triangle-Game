from manim import *
import complete
import triangleladder
import wheel
import vertexify


class Scratchpad(Scene):
    generator = wheel.WheelGraph()

    def construct(self):
        self.camera.background_color = WHITE

        # section w7
        """
        e = 7
        g = Graph(self.generator.generate_vertices(e),
                    self.generator.generate_edges(e),
                    layout = self.generator.generate_layout(e))

        g = Graph((1, 2, 3, 4),
                [(1, 2), (2, 3), (3, 1), (3, 4)],
                layout="kamada_kawai")
        """

        # section
        """
        plus_1 = SVGMobject(file_name="../res/plus.svg").scale(0.3)
        plus_2, plus_3, plus_4 = [plus_1.copy() for i in range(3)]

        plus_1.move_to(g.edges[(1, 6)])
        plus_2.move_to(g.edges[(2, 5)])
        plus_3.move_to(g.edges[(3, 5)])
        plus_4.move_to(g.edges[(3, 4)])

        self.add(g)

        self.add(plus_1)
        self.play(*[Indicate(g.edges[edge], rate_func=rate_functions.linear, color=PURE_RED, scale_factor=1) for edge in [(1, 7), (6, 7), (1, 6), (1, 2), (2, 6)]])

        self.add(plus_1, plus_2, plus_3, plus_4)
        self.play(*[Indicate(g.edges[edge], rate_func=rate_functions.linear, color=PURE_RED, scale_factor=1) for edge in [(2, 3), (2, 5), (3, 5), (3, 4), (4, 5)]])
        """

        # section text
        # text = MathTex("\\sum_{i=0}^{\\infty} PL(E)=3T")
        # text = MathTex("T=\\frac{1}{6}\\sum_{i=1}^{n} A(G)^{3}_{[i][i]}")
        # text = MathTex("\\frac{deg(X(E))}{2}=PL(E)")

        text = MathTex("\\frac{\\sum_{j=0}^{j_{max}}\\varepsilon(G)_{[i][j]}}{2}=PL(E_{i})")

        self.add(text.scale(2.5))

        # section tl7
        """
        g = Graph(self.generator.generate_vertices(7),
            self.generator.generate_edges(7),
            layout=self.generator.generate_layout(7), 
            labels=False)

        self.add(g)

        # Create PL labels for TL7
        edge_labels = [MarkupText("1", font_size=22, color=YELLOW) for _ in range(7)]
        edge_labels += [MarkupText("2", font_size=22, color=YELLOW) for _ in range(4)]

        edge_bg = [Circle(0.18, LIGHT_PINK, fill_opacity=1) for _ in range(11)]

        for num, edge in enumerate([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (1, 7), (1, 6), (2, 6), (2, 5), (3, 5)]):
            edge_labels[num].move_to(g.edges[edge])
            edge_bg[num].move_to(g.edges[edge])

        for label in edge_labels:
            self.add_foreground_mobject(label)

        self.add(*[label for label in edge_labels], *[bg for bg in edge_bg])
        """


        # section w5
        """
        lg = {
            0: (0, 0, 0),
            1: (2, 2, 0),
            2: (-2, 2, 0),
            3: (-2, -2, 0),
            4: (2, -2, 0)
        }

        lxg = {
            1: (2, 0, 0),
            2: (0, 2, 0),
            3: (-2, 0, 0),
            4: (0, -2, 0),
            5: (1, 1, 0),
            6: (-1, 1, 0),
            7: (-1, -1, 0),
            8: (1, -1, 0)
        }

        laxg = {
            1: "2",
            2: "2",
            3: "2",
            4: "2",
            5: "4",
            6: "4",
            7: "4",
            8: "4"
        }
        
        g = Graph(self.generator.generate_vertices(5),
            self.generator.generate_edges(5),
            layout=lg).shift(LEFT * 3)

        xg = Graph(vertexify.Vertexify().generate_vertices(g.edges),
            vertexify.Vertexify().generate_edges(g.edges),
            layout=lxg,
            labels=laxg).shift(RIGHT * 3)

        # Create PL labels for W5
        edge_labels = [MarkupText("1", font_size=32, color=YELLOW) for _ in range(4)]
        edge_labels += [MarkupText("2", font_size=32, color=YELLOW) for _ in range(4)]

        edge_bg = [Circle(0.24, LIGHT_PINK, fill_opacity=1) for _ in range(8)]

        for num, edge in enumerate([(1, 2), (2, 3), (3, 4), (1, 4), (0, 1), (0, 2), (0, 3), (0, 4)]):
            edge_labels[num].move_to(g.edges[edge])
            edge_bg[num].move_to(g.edges[edge])

        for label in edge_labels:
            self.add_foreground_mobject(label)

        self.add(g, xg)
        self.add(*[label for label in edge_labels], *[bg for bg in edge_bg])
        """

        # section k5
        """
        g = Graph(complete.CompleteGraph().generate_vertices(5),
            complete.CompleteGraph().generate_edges(5),
            layout="kamada_kawai",
            labels=True).shift(UP)

        text = MarkupText("What is the <gradient from=\"GREEN\" to=\"BLUE\">power level</gradient>")
        text2 = MarkupText("of edges in <span foreground=\"red\">K<sub>5</sub></span>?")

        text.move_to(DOWN * 2)
        text2.next_to(text, DOWN, buff=0.3)

        self.add(g, text, text2)
        """
