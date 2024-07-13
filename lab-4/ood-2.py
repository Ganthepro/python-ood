class Customer:
    def __init__(self, order_time: int, order_duration: int, id: int) -> None:
        self.__order_time = order_time
        self.__order_duration = order_duration
        self.__id = id

    @property
    def order_time(self):
        return self.__order_time
    
    @property
    def order_duration(self):
        return self.__order_duration

    @property
    def id(self):
        return self.__id
    
class Queue:
    def __init__(self):
        self.__customers: list[Customer] = []
        self.__time_orders = []

    @property
    def customers(self):
        return self.__customers
    
    @property
    def time_orders(self):
        return self.__time_orders
    
    def get_sum_of_order_times(self):
        return sum([n[0] for n in self.__time_orders])
    
    def get_sum_result(self, data):
        if len(self.__time_orders) > 0:
            if self.__time_orders[-1][0] > data.order_time:
                return [data.order_time + data.order_duration + (self.__time_orders[-1][0] - data.order_time), data.id, self.__time_orders[-1][0] - data.order_time]
            else:
                return [data.order_time + data.order_duration, data.id]
        else:
            return [data.order_time + data.order_duration, data.id]

    def push(self, data: Customer):
        self.__customers.append(data)
        self.__time_orders.append(self.get_sum_result(data))

print(" ***Cafe***")
inp = input("Log : ").split("/")
customers = []
b1 = Queue()
b2 = Queue()

for i ,j in enumerate(inp):
    t, d = j.split(",")
    customer = Customer(int(t), int(d), i + 1)
    if b1.get_sum_result(customer)[0] <= b2.get_sum_result(customer)[0]:
        b1.push(customer)
    else:
        b2.push(customer)

merge = b1.time_orders + b2.time_orders
for i in range(len(merge)):
    for j in range(i, len(merge)):
        if merge[i][0] > merge[j][0]:
            temp = merge[j]
            merge[j] = merge[i]
            merge[i] = temp
        elif merge[i][0] == merge[j][0] and merge[i][1] > merge[j][1]:
            temp = merge[j]
            merge[j] = merge[i]
            merge[i] = temp

highest = [0, 0]
for m in merge:
    print(f"Time {m[0]} customer {m[1]} get coffee")
    try:
        if m[2] > highest[1]:
            highest = [m[1], m[2]]
    except:
        pass

if highest[1] == 0:
    print("No waiting")
else:
    print(f"The customer who waited the longest is : {highest[0]}")
    print(f"The customer waited for {highest[1]} minutes")