def get_biggest_region(grid):
    max_count = 0

    # Iterate thru each cell left to right, top to bottom
    for i in xrange(len(grid)):
        for j in xrange(len(grid[0])):
            count = count_cells(grid, i, j)
            if count > 0 and count > max_count:
                max_count = count
                # print 'region count =', count

    return max_count


def count_cells(grid, i, j):
    # Exclude out-of-bounds cells
    if i < 0 or j < 0 or i > (len(grid) - 1) or j > (len(grid[0]) - 1):
        return 0

    if grid[i][j] == 1:
        # Flip to 0 to mark it as "visited"
        grid[i][j] = 0
        region_count = 1

        # if larger than largest region, replace with current value

        # check all adjacent cells; 8 possible adjacent cases
        region_count += count_cells(grid, i - 1, j - 1)
        region_count += count_cells(grid, i - 1, j)
        region_count += count_cells(grid, i - 1, j + 1)
        region_count += count_cells(grid, i, j + 1)
        region_count += count_cells(grid, i + 1, j + 1)
        region_count += count_cells(grid, i + 1, j)
        region_count += count_cells(grid, i + 1, j - 1)
        region_count += count_cells(grid, i, j - 1)

        return region_count
    else:
        return 0


n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)
