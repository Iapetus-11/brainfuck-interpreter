def cleanup(bf: str) -> str:
    return ''.join(c in bf if c in '><+-.,[]')

def make_bracemap(bf: str) -> dict:
    bracemap = {}
    temp = []

    for i, c in enumerate(bf):
        if c == '[':
            temp.append(i)
        elif c == ']':
            start = temp.pop()
            bracemap[start] = i
            bracemap[i] = start

    return bracemap


def evaluate(bf: str) -> None:
    bf = cleanup(bf)
    bracemap = make_bracemap(bf)

    arr = [0]
    ptr = 0
    i = 0

    while i < len(bf):
        c = bf[i]

        if c == '>':
            ptr += 1
        elif c == '<':
            ptr = 0 if ptr <= 0 else ptr - 1
        elif c == '+':
            arr[ptr] += 1
        elif c == '-':
            arr[ptr] -= 1
        elif c == '.':
            print(arr[ptr])
        elif c == ',':
            arr[ptr] = input(': ')[0]
        elif c == '[' and arr[ptr] == 0:
            ptr = bracemap[ptr]
        elif c == ']' and arr[ptr] != 0:
            ptr = bracemap[ptr]

        ptr += 1

evaluate(input(': '))
