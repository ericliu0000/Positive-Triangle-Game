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

def bulk_indicate(self, graph, edges, color=INDICATE_COLOR, include_vertices=True, **kwargs):
    actions = []

    # Get vertices from unique parts of edges
    vertices = list(set([edge[0] for edge in edges] + [edge[1] for edge in edges]))

    for edge in edges:
        actions.append(Indicate(graph.edges[edge], color=color, scale_factor=INDICATE_SCALE_FACTOR, **kwargs))

    if include_vertices:
        for vertex in vertices:
            actions.append(Indicate(graph.vertices[vertex], color=color, scale_factor=INDICATE_SCALE_FACTOR, **kwargs))

    bulk_play(self, actions)

def recolor(self, graph, edges, color):
    actions = []

    for edge in edges:
        actions.append(graph.edges[edge].animate(run_time=BRIEF_ANIMATION_TIME).set_color(color))

    bulk_play(self, actions)

def recolor_return(graph, edges, color):
    actions = []

    for edge in edges:
        actions.append(graph.edges[edge].animate(run_time=SHORT_ANIMATION_TIME).set_color(color))

    return actions