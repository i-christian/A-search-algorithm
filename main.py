#!/usr/bin/python3
from models.a_star_algorithm import algorithm
from models.model_visualisation import *


def main(win, width):
    """
    The main function to run the program.

    Args:
    win (pygame.Surface): The surface to draw the grid on.
    width (int): The width of the screen.

    Returns: 
    None
    """

    # Set the number of rows in the grid
    ROWS = 50

    # Create the grid with the specified number of rows and width
    grid = make_grid(ROWS, width)

    # Set the start and end nodes to None initially
    start = None
    end = None

    # Set the run flag to True to keep the game running
    run = True

    # Set the started flag to False initially
    started = False

    # Run the game loop
    while run:
        # Draw the grid on the window
        draw(win, grid, ROWS, width)

        # Handle events
        for event in pygame.event.get():
            # If the user clicks the close button, quit the game loop
            if event.type == pygame.QUIT:
                run = False

            # If the user left-clicks on a spot, make it a start or end node
            if pygame.mouse.get_pressed()[0]:  # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()

                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    spot.make_barrier()

            # If the user right-clicks on a spot, reset it
            elif pygame.mouse.get_pressed()[2]:  # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()

                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            # If the user presses the space bar and there are start and end nodes, run the A* algorithm
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    # The A* algorithm solving the given puzzle
                    algorithm(lambda: draw(win, grid, ROWS, width),
                              grid, start, end)

                # If the user presses the 'c' key, reset the start and end nodes and the grid
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    pygame.quit()


if __name__ == "__main__":
    """Run the program """
    main(WIN, WIDTH)
