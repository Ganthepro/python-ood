inp = int(input("Enter Number : "))

def recursion(n, current = 0, max = 0):
    if n < 0:
        return "Only Positive & Zero Number ! ! !"
    elif n == 0:
        return 0
    print(bin(current)[2:].zfill(n))
    max = 2**n - 1
    if current == max:
        return
    return recursion(n, current + 1, max)

output = recursion(inp)
if output is not None:
    print(output)