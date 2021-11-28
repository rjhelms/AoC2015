from os import path

INPUT = path.join("input", "1.txt")


def main():
    floor = 0
    position = 0
    with open(INPUT, "r") as in_file:
        for line in in_file:
            for character in line:
                if character == "(":
                    floor += 1
                elif character == ")":
                    floor -= 1
                position += 1
                if floor == -1:
                    print(position)
                    exit()


if __name__ == "__main__":
    main()
