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

    def smallest_perimeter(self):
        perimeters = [
            2 * (self.l + self.w),
            2 * (self.w + self.h),
            2 * (self.h + self.l),
        ]
        perimeters.sort()
        return perimeters[0]

    def volume(self):
        return self.l * self.w * self.h

    def ribbon(self):
        return self.smallest_perimeter() + self.volume()


def main():
    packages = []

    with open(INPUT, "r") as in_file:
        for line in in_file:
            dims = line.split("x")
            package = Package(int(dims[0]), int(dims[1]), int(dims[2]))
            packages.append(package)

    ribbon = 0
    for package in packages:
        ribbon += package.ribbon()

    print(ribbon)


if __name__ == "__main__":
    main()
