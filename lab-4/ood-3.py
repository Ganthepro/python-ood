class Queue:
    def __init__(self, value) -> None:
        self.items = value

def encodemsg(q1: Queue, q2: Queue):
    en_lst = []
    q2_index = 0
    for i in q1.items:
        if q2_index == len(q2.items):
            q2_index = 0
        new_ord = ord(i) + q2.items[q2_index]
        if i.islower():
            start = 97
            end = 112
        else:
            start = 65
            end = 90
        print(new_ord, chr(new_ord), end, en_lst)
        if new_ord > end:
            temp = new_ord - end
            new_ord = start + (temp - 1)
        en_lst.append(chr(new_ord))
        print(new_ord, chr(new_ord), end, en_lst)
        q2_index += 1
    return en_lst

def decodemsg(q1: Queue, q2: Queue):
    de_lst = []
    q2_index = 0
    for i in q1.items:
        if q2_index == len(q2.items):
            q2_index = 0
        new_ord = ord(i) - q2.items[q2_index]
        if i.islower():
            start = 97
            end = 112
        else:
            start = 65
            end = 90
        if new_ord < start:
            temp = start - new_ord
            new_ord = end - (temp - 1)
        de_lst.append(chr(new_ord))
        q2_index += 1
    return de_lst

s_inp, c_inp = input("Enter String and Code : ").split(",")
q1 = Queue([s for s in s_inp if s != " "])
q2 = Queue([int(n) for n in c_inp])

q_en = encodemsg(q1, q2)
print("Encode message is : ", q_en)
print("Decode message is : ", decodemsg(Queue(q_en), q2))
