from os import path

INPUT = path.join("input", "7.txt")

DEFINED = {}
RESOLVED = {}


class Gate:
    def __init__(self, oper, left, right):
        self.oper = oper
        self.left = left
        self.right = right

    def resolve(self):
        if type(self.left) == str:
            if self.left in RESOLVED:
                self.left = RESOLVED[self.left]
            else:
                return None
        if type(self.right) == str:
            if self.right in RESOLVED:
                self.right = RESOLVED[self.right]
            else:
                return None
        return self.oper(self.left, self.right)


def b_and(left, right):
    return left & right


def b_or(left, right):
    return left | right


def b_not(left, right):
    return (~right) & 65535


def b_lshift(left, right):
    return (left << right) & 65535


def b_rshift(left, right):
    return (left >> right) & 65535


def b_equals(left, right):
    return left


OPER_DICT = {
    "AND": b_and,
    "OR": b_or,
    "NOT": b_not,
    "LSHIFT": b_lshift,
    "RSHIFT": b_rshift,
    "EQ": b_equals,
}


def parse_input():
    with open(INPUT, "r") as in_file:
        for line in in_file:
            split_line = line.split("->")
            name = split_line[1].strip()
            if split_line[0].strip().isnumeric():
                RESOLVED[name] = int(split_line[0])
            else:

                left = None
                right = None
                oper = None
                instruction = split_line[0].split()
                if len(instruction) == 2:
                    oper = instruction[0]
                    right = instruction[1]
                elif len(instruction) == 1:
                    left = instruction[0]
                    oper = "EQ"
                else:
                    left = instruction[0]
                    oper = instruction[1]
                    right = instruction[2]
                if left and left.isnumeric():
                    left = int(left)
                if right and right.isnumeric():
                    right = int(right)
                oper = OPER_DICT[oper]
                DEFINED[name] = Gate(oper, left, right)


def main():
    parse_input()
    iter = 0
    while "a" not in RESOLVED:
        print("Iteration %i, unresolved %i" % (iter, len(DEFINED)))
        for key in DEFINED:
            result = DEFINED[key].resolve()
            if type(result) is int:
                RESOLVED[key] = result
        for key in RESOLVED:
            if key in DEFINED:
                DEFINED.pop(key)
        iter += 1

    print(RESOLVED["a"])


if __name__ == "__main__":
    main()
