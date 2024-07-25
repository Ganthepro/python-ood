inp = input("Enter Input : ").split()

def recursion(i, max = int(inp[0])):
    if i == len(inp):
        return max
    inp_int = int(inp[i])
    if inp_int > max:
        max = inp_int
    return recursion(i + 1, max)

print(recursion(0))