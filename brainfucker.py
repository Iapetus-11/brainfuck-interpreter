
def cleanup(bf: str) -> str:
    return ''.join(c for c in bf if c in '><+-.,[]')

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

            if ptr == len(arr):
                arr.append(0)
        elif c == '<':
            ptr = 0 if ptr <= 0 else ptr - 1
        elif c == '+':
            arr[ptr] = arr[ptr] + 1 if arr[ptr] < 255 else 0
        elif c == '-':
            arr[ptr] = arr[ptr] - 1 if arr[ptr] > 0 else 255
        elif c == '.':
            print(chr(arr[ptr]), end='')
        elif c == ',':
            arr[ptr] = ord(input(': ')[0])
        elif c == '[' and arr[ptr] == 0:
            i = bracemap[i]
        elif c == ']' and arr[ptr] != 0:
            i = bracemap[i]

        i += 1

evaluate(input(': '))
