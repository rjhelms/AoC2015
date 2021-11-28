from os import path

INPUT = path.join("input", "3.txt")


def main():
    houses = {}
    x = [0, 0]
    y = [0, 0]
    phase = 0
    houses[(0, 0)] = 1
    with open(INPUT, "r") as in_file:
        for line in in_file:
            for char in line:
                if char == ">":
                    x[phase] += 1
                elif char == "<":
                    x[phase] -= 1
                elif char == "v":
                    y[phase] += 1
                elif char == "^":
                    y[phase] -= 1
                houses[(x[phase], y[phase])] = 1
                phase = (phase + 1) % 2
    print(len(houses))


if __name__ == "__main__":
    main()
