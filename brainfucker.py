valid = '><+-.,[]'

global arr, ptr
arr = []
ptr = 0

def interpreter(bf: str):
    global arr, ptr
    i = 0

    while i < len(bf):
        print(arr)

        c = bf[i]

        if c == '>':
            ptr += 1

            if ptr >= len(arr):
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
            arr[ptr] = int(input(': '))
        elif c == '[':
            while arr[ptr]:
                interpreter(bf[i:])
        elif c == ']':
            return

        i += 1

interpreter(''.join(c for c in input(': ') if c in valid))
