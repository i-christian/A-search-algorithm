#!/usr/bin/python3
from models.model_visualisation import *


def algorithm(draw, grid, start, end):
    """
    Finds the shortest path using the A* algorithm
    Args:
        draw (function): Function to draw the visualisation of the algorithm
        grid (list): The 2D grid of spots
        start (Spot): The start node of the path
        end (Spot): The end node of the path

    Returns:
        bool: True if path found, False otherwise

    """
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0

    f_score = {spot: float("inf")
               for row in grid for spot in row if spot != start}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]  # Get the node with the lowest f-score
        open_set_hash.remove(current)  # Remove the node from the open set

        if current == end:  # If the goal is reached, reconstruct the path
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:  # Check the neighbors of the current node
            # Calculate the tentative g-score of the neighbor
            temp_g_score = g_score[current] + 1

            # If the tentative g-score is better than the previous g-score
            if temp_g_score < g_score[neighbor]:
                # Update the came_from dictionary
                came_from[neighbor] = current
                # Update the g-score of the neighbor
                g_score[neighbor] = temp_g_score
                # Update the f-score of the neighbor
                f_score[neighbor] = temp_g_score + \
                    h(neighbor.get_pos(), end.get_pos())

                if neighbor not in open_set_hash:  # If the neighbor is not in the open set
                    count += 1  # Increment the counter
                    # Add the neighbor to the open set
                    open_set.put((f_score[neighbor], count, neighbor))
                    # Add the neighbor to the set of nodes in the open set
                    open_set_hash.add(neighbor)
                    neighbor.make_open()  # Mark the neighbor as open

        draw()  # Redraw the grid

        if current != start:  # If the current node is not the start node
            current.make_closed()  # Mark the current node as closed

    return False
