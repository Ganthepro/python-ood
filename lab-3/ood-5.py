class Stack:
    def __init__(self):
        self.trees = []

    def push(self, value):
        self.trees.append(value)

    def poisoned(self):
        for t in range(len(self.trees)):
            if self.trees[t] % 2 == 0 and self.trees[t] > 1:
                self.trees[t] -= 1
            elif self.trees[t] % 2 != 0:
                self.trees[t] += 2

    def whats_behind(self):
        temp = 0
        counter = 0
        for t in reversed(self.trees):
            if t > temp:
                temp = t
                counter += 1
        print(counter)

S = Stack()

inp = input('Enter Input : ').split(',')

for e in inp:
    if e[0] == 'A':
        S.push(int(e[2:]))
    elif e[0] == 'B':
        S.whats_behind()
    elif e[0] == 'S':
        S.poisoned()