from os import path
import hashlib

INPUT = path.join("input", "4.txt")


def main():
    base = ""
    offset = 1
    with open(INPUT, "r") as in_file:
        for line in in_file:
            base = line

    found = False
    while not found:
        key = base + str(offset)
        hash = hashlib.md5(key.encode())
        if hash.hexdigest()[0:5] == "00000":
            found = True
            print(offset)
        offset += 1


if __name__ == "__main__":
    main()
