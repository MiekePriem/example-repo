def minesweeper(grid):
    rows = len(grid)
    cols = len(grid[0])

    result = []

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    for r in range(rows):
        row_result = []
        for c in range(cols):

            # If it's a mine, keep it as "#"
            if grid[r][c] == "#":
                row_result.append("#")
            else:
                # Count adjacent mines
                count = 0

                # Check all 8 surrounding cells
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:

                        # skip the current cell itself
                        if dr == 0 and dc == 0:
                            continue

                        nr = r + dr
                        nc = c + dc

                        if in_bounds(nr, nc) and grid[nr][nc] == "#":
                            count += 1

                row_result.append(count)

        result.append(row_result)

    return result


# Example test from the task sheet
input_grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

output_grid = minesweeper(input_grid)

for row in output_grid:
    print(row)
