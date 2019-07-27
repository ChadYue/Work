import random

color_List = ['黑桃', '红心', '梅花', '方片']


class Poke:
    def __init__(self):
        self.Card = []
        self.card = ()

        for color in color_List:
            for value in range(1, 14):
                if value == 1:
                    self.card = color + 'A'
                elif value == 11:
                    self.card = color + 'J'
                elif value == 12:
                    self.card = color + 'Q'
                elif value == 13:
                    self.card = color + 'K'
                else:
                    self.card = color + str(value)
                self.Card.append(self.card)

    def output(self):
        i = 0
        for self.card in self.Card:
            print(self.card, end='\t')
            i += 1
            if i % 13 == 0:
                print()


class Hands:
    def __init__(self, hands):
        self.hands = hands
        self.x = 0

    def hand(self):
        global x
        handcolor = [card[:2] for card in self.hands]
        handvalue = []
        for key in self.hands:
            if key[2:] == 'A':
                key = 1
            elif key[2:] == 'J':
                key = 11
            elif key[2:] == 'Q':
                key = 12
            elif key[2:] == 'K':
                key = 13
            else:
                key = int(key[2:])
            handvalue.append(key)
        handcolorset = set(handcolor)
        handvalueset = set(handvalue)
        handvaluesorted = sorted(handvalue)
        if len(handcolorset) == 1:
            if len(handvalueset) == 5 and handvaluesorted[4] - handvaluesorted[0] == 4:
                baccarat = '同花顺'
                x = 1
            else:
                baccarat = '同花'
        elif len(handvalueset) == 2:
            if handvaluesorted[1] == handvaluesorted[2]:
                baccarat = '四条'
            else:
                baccarat = '葫芦'
        elif len(handvalueset) == 3:
            if handvaluesorted.count(handvaluesorted[2]) == 3:
                baccarat = '三条'
            else:
                baccarat = '两对'
        elif len(handvalueset) == 4:
            baccarat = '一对'
        elif len(handvalueset) == 5:
            if handvaluesorted[4] - handvaluesorted[0] == 4:
                baccarat = '顺子'
            else:
                baccarat = '杂牌'
        print(baccarat)
        return x


p = Poke()
p.output()
x = 0
y = 0
while x != 1:
    y += 1
    random.shuffle(p.Card)
    A_hands = p.Card[0:20:4]
    B_hands = p.Card[1:20:4]
    C_hands = p.Card[2:20:4]
    D_hands = p.Card[3:20:4]
    Hands(A_hands).hand()
    Hands(B_hands).hand()
    Hands(C_hands).hand()
    Hands(D_hands).hand()