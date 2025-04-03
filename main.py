from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    num_rows, num_cols = 12, 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    seed = 1

    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed)
    print("Maze Completed!")
    print("Starting Maze Solving...")
    
    output = maze.solve()
    if output:
        print("Maze Solved")
    else:
        print("Maze cant be solved")
   

    win.wait_for_close()

if __name__ == "__main__":
    print("Starting Window")
    main()
