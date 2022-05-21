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

