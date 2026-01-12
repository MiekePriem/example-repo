# Example Repo – Minesweeper Project

## Project Description
This project is a Python implementation of a simplified Minesweeper grid.

The program takes a 2D list representing a minesweeper board, where:
- "#" represents a mine
- "-" represents an empty cell

For each empty cell, the program calculates how many mines are present in the surrounding 8 cells.

## How the Program Works
- The grid is iterated row by row and column by column
- If a cell contains a mine ("#"), it is copied directly to the output
- If the cell is empty ("-"), the program checks all neighbouring cells
- A counter is used to count how many mines are adjacent
- The result is returned as a new grid with mine counts

## Example Output
The program prints the updated grid showing the number of adjacent mines for each cell.
