# MA4500 Graph Theory with REX Math Final Project

## Presentation animations for problem "Positive Triangle Game"

### Cooper Xie, Emmy Tang, Eric Liu

## Usage

Animations in this project were created using [Manim Community](https://www.manim.community/) in Python 3.10. 

To create a video file, run 

`manim [file].py`

with a file that contains a valid Manim structure. This outputs a file into directory `media/videos` relative to where the script was run.

## Structure

`graphs` contains specific basic graphs that are used in the other animations:
* Complete graphs
* Triangle ladder graphs
* Wheel graphs
* "Vertexification" operation

The root folder contains a few files and scenes
* `util.py` contains helper functions
* `constants.py` contains project animation constants
* Other files are the animations themselves

Testing is for experimenting with matrices and manim operations.