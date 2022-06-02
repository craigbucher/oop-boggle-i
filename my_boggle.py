from string import ascii_uppercase
import random

class BoggleBoard:

    _char_map = {"Q": "Qu"}

    def __init__(self):
        self.board = [list("----") for i in range(4)]
        
    def __str__(self):
        strings = list()

        for row in self.board:
            strings.append(" ".join(self._char_map.get(char, char).ljust(2) for char in row))
        return "\n".join(strings)

    def shake(self):
        self.board = [[random.choice(ascii_uppercase) for i in range(4)] for i_ in range(4)]


def main():
    boggle = BoggleBoard()
    print(boggle)
    boggle.shake()
    print(boggle)
###### Why do we need this ##########
if __name__ =="__main__":
    main()