from operator import mul


def get_all_presents(rd):
    for line in rd:
        yield parse_size(line)


def parse_size(line):
    return map(int, line.split("x"))


def get_ribbon(present):
    sides = list(present)
    sides.remove(max(sides))
    return sum(2 * x for x in sides) + reduce(mul, present)


def main():
    total = 0
    with open("data.txt", "rb") as rd:
        for present in get_all_presents(rd):
            total += get_ribbon(present)

    print "total size", total


if __name__ == "__main__":
    print "Sanity check: 2x3x4 =", get_ribbon((2, 3, 4))
    print "Sanity check: 1x1x10 =", get_ribbon((1, 1, 10))

    main()
