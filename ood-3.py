class funString():

    def __init__(self,string = ""):
        self.string = string

    def __str__(self):
        return self.string

    def size(self):
        return len(self.string)

    def changeSize(self):
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        lst_str = list(self.string)
        for c in range(len(self.string)):
            if self.string[c] in upper:
                lst_str[c] = lower[upper.index(self.string[c])]
            elif self.string[c] in lower:
                lst_str[c] = upper[lower.index(self.string[c])]
        return "".join(lst_str)

    def reverse(self):
        return self.string[::-1]

    def deleteSame(self):
        res = ""
        for c in self.string:
            if c not in res:
                res += c
        return res

str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())