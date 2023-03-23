# A* Pathfinding Algorithm Visualisation

This program visualizes the *A\* pathfinding algorithm*. The algorithm is used to find the shortest path between two points on a 2D grid. The user can create a maze on the grid and set the start and end points. The program then runs the A* algorithm and shows the shortest path between the two points.


```
A* Pathfinding Algorithm*:  

A* is a popular pathfinding algorithm used to find the shortest path between two points on a graph. It works by exploring the graph in a systematic way, keeping track of the total cost of each possible path from the starting point to the end point. The algorithm uses both the actual cost of a path (i.e. the distance between two points) and an estimate of the remaining cost (i.e. the heuristic) to determine which path to explore next. The heuristic is usually an estimate of the distance between a given point and the end point, and is used to prioritize paths that are closer to the end point. A* is known for its efficiency and is widely used in games and robotics.

```

## Tests: heavy_check_mark:

* [tests](./tests/): test files:
    * [test_algorithm.py](./tests/test_algorithm.py)

* To run the test:
```python3 -m unittest discover -v -s tests```

## :warning: Prerequisites

* Must have `git` installed.
* Download from here: [git](https://git-scm.com/downloads)
* For linux user's: ```sudo apt-get install git```

## Installation

To use this program, follow these steps:

* Clone the repository:
```https://github.com/i-christian/A-star-Pathfinding-Algorithm-Visualisation```

* [Python 3.10](https://www.python.org/downloads/release/python-31010/) - The python version used.

* Install the required dependencies using pip:
```pip install pygame```


## Usage :running:

1. Run the program:
```python3 main.py```
2. Draw walls on the grid by left-clicking and dragging the mouse. To remove a wall, right-click on it.
3. Set the start and end points by left-clicking on the cells.
4. Press the ***space key*** <kbd>space</kbd> to run the algorithm.
5. Press the ***c key*** <kbd>c</kbd> to clear the grid.

## Screenshots

<h1 align="center">Before the Algorthim was run</h1>
<p align="center">
<img src="https://github.com/i-christian/A-star-Pathfinding-Algorithm-Visualisation/blob/main/assets/images/before_run.png" alt="Visualisation Grid">
</p>

<h1 align="center">After the Algorthim was run</h1>
<p align="center">
<img src="https://github.com/i-christian/A-star-Pathfinding-Algorithm-Visualisation/blob/main/assets/images/after_run.png" alt="Visualisation Grid">
</p>

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

### Contributors :black_nib:
* Christian Innocent Mhango <[i-christian](https://github.com/i-christian)>