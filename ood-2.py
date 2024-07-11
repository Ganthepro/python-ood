class TorKham:
    def __init__(self):
        self.words = []

    def restart(self):
        self.words.clear()
        return "game restarted"

    def play(self, word):
        if self.words == []:
            self.words.append(word[2:])
        else:
            if word[2:4].lower() == self.words[-1][-2:].lower():
                self.words.append(word[2:])
            else:
                print(f"'{word[2:]}' -> game over")
                exit()
        return self.words

torkham = TorKham()

print("*** TorKham HanSaa ***")

S = input("Enter Input : ").split(',')

for s in S:
    if s[0] == 'P':
        print(f"'{s[2:]}' -> {torkham.play(s)}")
    elif s[0] == 'R':
        print(torkham.restart())
    elif s[0] == 'X':
        break
    else:
        print(f"'{s}' is Invalid Input !!!")
        exit()