from manim import *

# Text configuration constants
TEXT_COLOR = "#edcaeb"
TOP_TEXT_BUFFER = 0.5
BETWEEN_TEXT_BUFFER = 0.25

# Animation time scale constants
SHORT_ANIMATION_TIME = 0.2
BRIEF_ANIMATION_TIME = 0.5
ANIMATION_TIME = 0.8
LONG_ANIMATION_TIME = 1.5
SHORT_DWELL_TIME = 1
LONG_DWELL_TIME = 4

# Plus and minus sign scale factors
PLUS_SCALE = 0.5
MINUS_SCALE = 0.12

# Graph edge and vertex indication constants
INDICATE_COLOR = YELLOW
INDICATE_SCALE_FACTOR = 1.5

# Power level label constants
PL_CIRCLE_SIZE = 0.18
PL_FONT_SIZE = 22

# Vocabulary color constants
POSITIVE_TRIANGLE_COLOR = "foreground=\"green\""
GRAPH_COLOR = "foreground=\"red\""
SINGLE_UNDERLINE = "underline=\"single\" underline_color=\"yellow\""
DOUBLE_UNDERLINE = "underline=\"double\" underline_color=\"red\""
POWER_LEVEL_GRADIENT = "from=\"GREEN\" to=\"BLUE\""
ONE_COMPLETE_GRADIENT = "from=\"YELLOW_C\" to=\"RED\""
VERTEXIFIED_GRADIENT = "from=\"TEAL_E\" to=\"PURE_BLUE\""
MEMBERS_GRADIENT = "from=\"PINK\" to=\"GOLD_E\""

# Layouts
K5_LAYOUT = {
    0: (0, 1.5, 0),
    1: (-1.427, 0.464, 0),
    2: (-0.882, -1.214, 0),
    3: (0.882, -1.214, 0),
    4: (1.427, 0.464, 0)
}

W7_LAYOUT = {
    0: (0, 0, 0),
    1: (1.732, 1, 0),
    2: (0, 2, 0),
    3: (-1.732, 1, 0),
    4: (-1.732, -1, 0),
    5: (0, -2, 0),
    6: (1.732, -1, 0)
}

XW7_LAYOUT = {
    1: (1.732, 0, 0),
    2: (0.866, 1.5, 0),
    3: (-0.866, 1.5, 0),
    4: (-1.732, 0, 0),
    5: (-0.866, -1.5, 0),
    6: (0.866, -1.5, 0),
    7: (0.866, 0.5, 0),
    8: (0, 1, 0),
    9: (-0.866, 0.5, 0),
    10: (-0.866, -0.5, 0),
    11: (0, -1, 0),
    12: (0.866, -0.5, 0)
}
