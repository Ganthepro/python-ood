lst = list(range(10))
lst2 = lst.copy()
for i in lst2:
    lst.pop(0)
    print(i)
    print(lst)