
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
        print(i)
        c = bf[i]

        if c == '>':
            ptr += 1

            if ptr == len(arr):
                arr.append(0)
        elif c == '<':
            ptr -= 1
        elif c == '+':
            arr[ptr] += 1
        elif c == '-':
            arr[ptr] -= 1
        elif c == '.':
            print(arr[ptr])
        elif c == ',':
            arr[ptr] = input(': ')[0]
        elif c == '[' and arr[ptr] == 0:
            i = bracemap[i]
        elif c == ']' and arr[ptr] != 0:
            i = bracemap[i]

        i += 1

evaluate(input(': '))
