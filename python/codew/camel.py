#!/usr/bin/python3

def camel(a):
    eng = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    sml = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    out = ""
    t = 0
    for x, i in zip(a, range(0, len(a))):
        if x in ['-', '_']:
            t = 1
        elif x in sml and t == 1:
            out += eng[sml.index(x)]
        elif x in sml and t == 0:
            out += x
        elif x in eng and t == 1:
            out += x
        elif x in eng and i == 0:
            out += x
        else:
            pass

    return out


def main():
    print("snake_case:", camel(input("camelcase: ")))


if __name__ == "__main__":
    main()
