valid = '><+-.,[]'

bf = ''.join(c for c in input(': ') if c in valid)

arr = []
ptr = 0

def interpreter(bf: str):
    while i < len(bf):
        c = bf[i]

        if c == '>':
            ptr += 1
        elif c == '<':
            ptr -= 1
        elif c == '+':
            arr[ptr] += 1
        elif c == '-':
            arr[ptr] -= 1
        elif c == '.':
            print(arr[ptr])
        elif c == ',':
            arr[ptr] = int(input(': '))
        elif c == '[':
            while arr[ptr]:
                interpreter(bf[i:])
        elif c == ']':
            return

        i += 1
