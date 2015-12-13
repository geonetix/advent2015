from collections import defaultdict


def deliver_presents(roofmap, housegrid):
    santa = (0, 0)
    drop_present(housegrid, santa)
    for c in roofmap:
        santa = move_santa(santa, c)
        drop_present(housegrid, santa)


def drop_present(grid, pos):
    grid[pos] += 1


def move_santa(pos, direction):
    """ We assume origin is top left. So north is -1, east is +1 """
    if direction == '^':
        return (pos[0], pos[1] - 1)
    elif direction == 'v':
        return (pos[0], pos[1] + 1)
    elif direction == '<':
        return (pos[0] - 1, pos[1])
    elif direction == '>':
        return (pos[0] + 1, pos[1])
    raise Exception("Unsupported move %s" % repr(direction))


def housegrid_houses_delivered(grid):
    return len(grid.keys())


def main():
    housegrid = defaultdict(int)

    with open("data.txt", "rb") as rd:
        roofmap = rd.read().strip()

    deliver_presents(roofmap, housegrid)
    print "Number of houses touched: ", housegrid_houses_delivered(housegrid)


if __name__ == "__main__":
    main()
