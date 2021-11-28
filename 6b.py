from os import path

INPUT = path.join("input", "6.txt")


def init_field(field):
    for x in range(1000):
        for y in range(1000):
            field[x, y] = 0


def main():
    field = {}
    init_field(field)

    with open(INPUT, "r") as in_file:
        for line in in_file:
            split = line.split(" ")
            start = [int(x) for x in split[-3].split(",")]
            end = [int(x) for x in split[-1].split(",")]
            instruction = split[0]
            if instruction == "turn":
                instruction = split[1]

            for x in range(start[0], end[0] + 1):
                for y in range(start[1], end[1] + 1):
                    if instruction == "toggle":
                        field[x, y] += 2
                    elif instruction == "on":
                        field[x, y] += 1
                    elif instruction == "off":
                        field[x, y] -= 1
                        if field[x, y] < 0:
                            field[x, y] = 0

        print(sum(field.values()))


if __name__ == "__main__":
    main()
