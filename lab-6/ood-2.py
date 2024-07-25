i = 1

def length(txt):
    global i
    if i % 2 == 0:
        spc = "~"
    else:
        spc = "*"
    print(f"{txt[i - 1]}", end=spc)
    if i == len(txt):
        return len(txt)
    i += 1
    return length(txt)

print("\n",length(input("Enter Input : ")),sep="")
