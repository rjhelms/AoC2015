from os import path

INPUT = path.join("input", "3.txt")


def main():
    houses = {}
    x = 0
    y = 0
    houses[(0, 0)] = 1
    with open(INPUT, "r") as in_file:
        for line in in_file:
            for char in line:
                if char == ">":
                    x += 1
                elif char == "<":
                    x -= 1
                elif char == "v":
                    y += 1
                elif char == "^":
                    y -= 1
                houses[(x, y)] = 1
    print(len(houses))


if __name__ == "__main__":
    main()
