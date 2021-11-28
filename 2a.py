from os import path

INPUT = path.join("input", "2.txt")


class Package:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    def wrap(self):
        sides = [self.l * self.w, self.w * self.h, self.h * self.l]
        sides.sort()
        paper = (2 * (sides[0] + sides[1] + sides[2])) + sides[0]
        return paper


def main():
    packages = []

    with open(INPUT, "r") as in_file:
        for line in in_file:
            dims = line.split("x")
            package = Package(int(dims[0]), int(dims[1]), int(dims[2]))
            packages.append(package)

    paper = 0
    for package in packages:
        paper += package.wrap()

    print(paper)


if __name__ == "__main__":
    main()
