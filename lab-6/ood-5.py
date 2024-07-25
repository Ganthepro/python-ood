def asteroid_collision(asts: list, i = 0):
    if i >= len(asts) - 1:
        return asts
    cur = asts[i]
    next = asts[i + 1] if i + 1 < len(asts) else None
    if next is not None:
        if (next < 0 and cur > 0) and abs(cur) == abs(next):
            asts.pop(i)
            asts.pop(i)
            return asteroid_collision(asts, 0)
        elif cur > 0 and next < 0 and abs(cur) > abs(next):
            asts.pop(i + 1)
            return asteroid_collision(asts, 0)
        elif cur > 0 and next < 0 and abs(cur) < abs(next):
            asts.pop(i)
            return asteroid_collision(asts, 0)
        return asteroid_collision(asts, i + 1)
    return asts

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))