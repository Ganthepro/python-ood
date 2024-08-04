def alphabet_sequece(char, step, lenght):
    char = char.upper()
    start = ord(char)
    for i in range(0, (lenght * 2) - step, step):
        cur = i % 26
        print(chr(start + cur), end="=")
    print(chr(start + cur + step))

char, step, lenght = input().split()
alphabet_sequece(char, int(step), int(lenght))