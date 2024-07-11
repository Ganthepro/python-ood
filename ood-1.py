def check_str(s):
    if s == "-":
        return "1"
    elif s != "#":
        return str(int(s) + 1)
    else:
        return s
    


def num_grid(lst):
    for x in range(len(lst)):
       for y in range(len(lst[x])):
            if lst[x][y] == "#":
                if x > 0:
                    lst[x-1][y] = check_str(lst[x-1][y])
                if x < len(lst)-1:
                    lst[x+1][y] = check_str(lst[x+1][y])
                if y > 0:
                    lst[x][y-1] = check_str(lst[x][y-1])
                if y < len(lst[x])-1:
                    lst[x][y+1] = check_str(lst[x][y+1])
                if x > 0 and y > 0:
                    lst[x-1][y-1] = check_str(lst[x-1][y-1])
                if x > 0 and y < len(lst[x])-1:
                    lst[x-1][y+1] = check_str(lst[x-1][y+1])
                if x < len(lst)-1 and y > 0:
                    lst[x+1][y-1] = check_str(lst[x+1][y-1])
                if x < len(lst)-1 and y < len(lst[x])-1:
                    lst[x+1][y+1] = check_str(lst[x+1][y+1])
    for x in range(len(lst)):
        for y in range(len(lst[x])):
            if lst[x][y] == "-":
                lst[x][y] = "0"
    return lst



# lst_input = [
#     ["-","#","-","-","-"],
#     ["-","-","-","#","-"],
#     ["-","-","#","-","-"],
#     ["-","-","-","-","-"],
#     ["-","-","-","#","-"]
# ]
print("*** Minesweeper ***")
lst_input = []

input_list = input("Enter input(5x5) : ").split(",")

for e in input_list:

  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")

print("\n",*num_grid(lst_input),sep = "\n")