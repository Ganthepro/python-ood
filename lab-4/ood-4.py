class Customer:
    def __init__(self, order_time, order_duration, id) -> None:
        self.order_time = order_time
        self.order_duration = order_duration
        self.id = id

    def __str__(self) -> str:
        return f"duration: {self.order_duration}, id: {self.id}"

class Queue:
    def __init__(self) -> None:
        self.next_order = 0
        self.customers: list[Customer] = []

    def push(self, customer: Customer):
        self.customers.append(customer)
        # print(customer)
        self.next_order += customer.order_duration

    def pop(self):
        try:
            self.customers.remove(self.customers[0])
        except:
            pass

    def show_customer(self, index, time):
        print(f"time: {time} {self.customers[index]}")

    def update_queun(self, time):
        if time >= self.next_order:
            try:
                self.show_customer(0, time)
            except:
                pass
            self.pop()

print(" ***Cafe***")

inp = "0,3/0,7/2,3/7,7/10,5/10,1".split("/")
b1 = Queue()
b2 = Queue()

for i in inp:
    t, d = i.split(",")
    b1.update_queun(int(t))
    b2.update_queun(int(t))
    if b1.next_order <= b2.next_order:
        b1.push(Customer(int(t), int(d), inp.index(i) + 1))
    else:
        b2.push(Customer(int(t), int(d), inp.index(i) + 1))
        # print(f"b2", end=" ")
        # b2.show_customers()
