 #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----




def print_rangoli(size):
    # Upper half
    for i in range(size - 1, 0, -1):
        print('-' * (i * 2), end='')
        for j in range(size, i, -1):
            print(chr(96 + j), end='-')
        for k in range(i + 2, size + 1):
            print(chr(96 + k), end='-')
        print('-' * (i * 2))

    # Middle line
    print('-' * (size - 1), end='')
    for i in range(size, 1, -1):
        print(chr(96 + i), end='-')
    for j in range(2, size + 1):
        print(chr(96 + j), end='-')
    print('-' * (size - 1))

    # Lower half
    for i in range(2, size):
        print('-' * (i * 2), end='')
        for j in range(size, i, -1):
            print(chr(96 + j), end='-')
        for k in range(i + 2, size + 1):
            print(chr(96 + k), end='-')
        print('-' * (i * 2))

if __name__ == '__main__':
    # n = int(input("Enter the size: "))
    n = 5
    print_rangoli(n)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
