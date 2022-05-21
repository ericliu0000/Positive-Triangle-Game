from manim import MarkupText
from constants import *

def text_generator(text, ref):
    lines = text.split("\n")
    groups = []

    temp = []
    for line in lines:
        line = line.strip()

        if line.startswith("#"):
            groups.append(temp)
            temp = []
        else:
            obj = MarkupText(line, color=TEXT_COLOR)

            if len(temp) == 0:
                obj.next_to(ref, DOWN, buff=TOP_TEXT_BUFFER)
            else:
                obj.next_to(temp[-1], DOWN, buff=BETWEEN_TEXT_BUFFER)

            temp.append(obj)

    groups.append(temp)

    return groups

def bulk_play(self, *args, **kwargs):
    for arg in args:
        if type(arg) == list:
            self.play(*arg)
        else:
            self.play(arg, **kwargs)

def bulk_indicate(self, graph, edges):
    actions = []

    # Get vertices from unique parts of edges
    vertices = list(set([edge[0] for edge in edges] + [edge[1] for edge in edges]))

    for edge in edges:
        actions.append(Indicate(graph.edges[edge], color=INDICATE_COLOR, scale_factor=INDICATE_SCALE_FACTOR))

    for vertex in vertices:
        actions.append(Indicate(graph.vertices[vertex], color=INDICATE_COLOR, scale_factor=INDICATE_SCALE_FACTOR))

    bulk_play(self, actions)
