inp = input("Enter Input : ").split(",")

def perket(i = 0, result = None):
    if i == len(inp):
        return result
    for j in range(len(inp) - i):
        total_sour = 1
        total_bitt = 0
        for k in inp[j:len(inp) - i]:
            s, b = k.split()
            total_sour *= int(s)
            total_bitt += int(b)
        res = abs(total_sour - total_bitt)
        if result is None or res < result:
            result = res
    return perket(i + 1, result)

print(perket())