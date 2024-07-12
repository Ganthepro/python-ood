class Queue:
    def __init__(self, time = None, max = None) -> None:
        self.__items = []
        self.__time = time
        self.__max = max

    def push(self, data):
        self.__items.append(data)

    def pop(self):
        try:
            temp = self.__items[0]
            self.__items.pop(0)
            return temp
        except:
            pass

    def size(self):
        return len(self.__items)

    @property
    def items(self):
        return self.__items
    
    @property
    def time(self):
        return self.__time
    
    @property
    def max(self):
        return self.__max

inp = input("Enter people : ")
q_main = Queue()
q_1 = Queue(3, 5)
q_2 = Queue(2, 5)

for i in inp:
    q_main.push(i)

time = 1
while q_main.size() > 0:
    temp = q_main.pop()
    if q_1.size() < q_1.max:
        q_1.push(temp)
    else:
        q_2.push(temp)
    print(f"{time} {q_main.items} {q_1.items} {q_2.items}")
    if (q_1.time % time == 0 or time % q_1.time == 0) and time > 1:
        q_1.pop()
    if q_2.time % (time + 1) == 0 or (time + 1) % q_2.time == 0:
        q_2.pop()
    time += 1