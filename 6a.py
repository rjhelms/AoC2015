from os import path

INPUT = path.join("input", "6.txt")


def init_field(field):
    for x in range(1000):
        for y in range(1000):
            field[x, y] = False


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
                        field[x, y] = not field[x, y]
                    elif instruction == "on":
                        field[x, y] = True
                    elif instruction == "off":
                        field[x, y] = False

        print(sum(value for value in field.values()))


if __name__ == "__main__":
    main()
