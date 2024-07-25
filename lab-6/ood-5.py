def is_left(asts, current):
    if asts[current] < 0:
        return True
    return False

def is_right(asts, current):
    if asts[current] > 0:
        return True
    return False

def is_collision(asts, i, is_left):
    pass


def asteroid_collision(asts: list, i = 0):
    if i == 0 and is_left(asts, i):
        return asteroid_collision(asts, i+1)
    if i == len(asts) - 1:
        if is_left(asts, i):
            is_collision(asts, i)
        return asts
    cond = is_left(asts, i)
    if cond:
        lst = asts[:i]
    else:
        lst = asts[i+1:]
    is_collision(lst, i, cond)
    return asteroid_collision(asts, i+1)

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))