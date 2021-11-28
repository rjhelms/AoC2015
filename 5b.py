from os import path

INPUT = path.join("input", "5.txt")


def validate(candidate):
    pair_check = False
    repeat_check = False

    # pair check
    for i in range(1, len(candidate)):
        if candidate[i - 1 : i + 1] in candidate[i + 1 :]:
            pair_check = True

    # repeat check
    for i in range(2, len(candidate)):
        if candidate[i] == candidate[i - 2]:
            repeat_check = True

    return pair_check and repeat_check


def main():
    nice = 0

    with open(INPUT, "r") as in_file:
        for line in in_file:
            if validate(line):
                nice += 1
    print(nice)


if __name__ == "__main__":
    main()
