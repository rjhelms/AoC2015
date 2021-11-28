from os import path

INPUT = path.join('input', '5.txt')

def validate(candidate):
    vowel_count = 0
    vowel_check = False
    double_check = False
    forbidden_check = False

    for i in range(0, len(candidate)):
        if candidate[i] in "aeiou":
            vowel_count += 1
        if i > 0:
            if candidate[i] == candidate[i - 1]:
                double_check = True
            if candidate[i - 1 : i + 1] in ("ab", "cd", "pq", "xy"):
                forbidden_check = True

    vowel_check = vowel_count > 2
    return vowel_check and double_check and not forbidden_check


def main():
    nice = 0
    with open(INPUT, 'r') as in_file:
        for line in in_file:
            if validate(line):
                nice += 1
    print(nice)


if __name__ == "__main__":
    main()
