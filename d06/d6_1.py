import re

import numpy


def execute_instructions(insts, grid):
    for inst in insts:
        if inst.startswith("turn on"):
            turn_on(grid, *parse_coords(inst))
        elif inst.startswith("turn off"):
            turn_off(grid, *parse_coords(inst))
        elif inst.startswith("toggle"):
            toggle(grid, *parse_coords(inst))


def turn_on(grid, start, end):
    action = lambda a: 1
    operate_on_grid(grid, start, end, action)


def turn_off(grid, start, end):
    action = lambda a: 0
    operate_on_grid(grid, start, end, action)


def toggle(grid, start, end):
    action = lambda a: 0 if bool(a) else 1
    operate_on_grid(grid, start, end, action)


def operate_on_grid(grid, start, end, action):
    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            grid[x][y] = action(grid[x][y])


def parse_coords(line):
    start, end = re.findall(r'\d+,\d+', line)
    return parse_coord(start), parse_coord(end)


def parse_coord(coords):
    return map(int, coords.split(','))


def main():
    light_grid = numpy.array([[0] * 1000] * 1000)

    with open("data.txt", "rb") as rd:
        instructions = [x.strip() for x in rd.readlines()]
        execute_instructions(instructions, light_grid)

    print "Lights lit:", sum(cell for row in light_grid for cell in row)


if __name__ == "__main__":
    main()
