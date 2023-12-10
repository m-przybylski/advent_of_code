# 5 of kind - 6
# 4 of kind - 5
# FH of kind - 4
# 3 of kind - 3
# 2 pair - 2
# 1 pair - 1

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
cardsWithJ = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

class Card:
    def __init__(self, card, count) -> None:
        self.card = card
        self.count = count

    def __str__(self) -> str:
        return f"{self.card}:{self.count}"

class Bet:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        self.cards = []
        for card in cards:
            count = 0
            for cardInHand in self.hand:
                if cardInHand == card: 
                    count += 1
            self.cards.append(Card(card, count))
        self.cards.sort(key=lambda card: card.count)
        self.rank = self.__calculateRank()

    def __calculateRank(self) -> int:
        clone = self.cards.copy()
        topCards = clone.pop()
        secondTop = clone.pop()

        if (topCards.count == 5):
            return 6
        if (topCards.count == 4):
            return 5
        if (topCards.count == 3 and secondTop.count == 2):
            return 4
        if (topCards.count == 3):
            return 3
        if (topCards.count == 2 and secondTop.count == 2):
            return 2
        if (topCards.count == 2):
            return 1
        
        return 0

    def __lt__(self, other):
        if (self.rank != other.rank):
            return self.rank < other.rank
        else:
            for i in range(len(self.hand)):
                i1 = cards.index(self.hand[i])
                i2 = cards.index(other.hand[i])
                if (i1 == i2):
                    continue
                return i1 > i2

            # Object are equal
            return False        

class BetWithJoker:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        self.cards = []
        self.jokers = 0
        for card in cardsWithJ:
            count = 0                
            for cardInHand in self.hand:
                if cardInHand == card: 
                    if (card == "J"):
                        self.jokers += 1
                    else:
                        count += 1

            self.cards.append(Card(card, count))

        self.cards.sort(key=lambda card: card.count)
        self.rank = self.__calculateRank()

    def __calculateRank(self) -> int:
        clone = self.cards.copy()
        topCards = clone.pop()
        secondTop = clone.pop()

        topCards.count += self.jokers

        if (topCards.count == 5):
            return 6
        if (topCards.count == 4):
            return 5
        if (topCards.count == 3 and secondTop.count == 2):
            return 4
        if (topCards.count == 3):
            return 3
        if (topCards.count == 2 and secondTop.count == 2):
            return 2
        if (topCards.count == 2):
            return 1
        
        return 0

    def __lt__(self, other):
        if (self.rank != other.rank):
            return self.rank < other.rank
        else:
            for i in range(len(self.hand)):
                i1 = cardsWithJ.index(self.hand[i])
                i2 = cardsWithJ.index(other.hand[i])
                if (i1 == i2):
                    continue
                return i1 > i2

            # Object are equal
            return False

    def __str__(self) -> str:
        return f"{self.hand}: {self.rank}"

def compare(hand1, hand2):
    if (hand1.hand == hand2.hand):
        return 0
    if (hand1.rank != hand2.rank):
        return hand1.rank - hand2.rank


def parseData():
    f = open("input/day7", "r")
    bets = f.read().split("\n")

    b = []
    for bet in bets:
        hand,bid = bet.split(" ")
        b.append(Bet(hand, bid))

    b.sort()

    return b

def parseDataWithJokers():
    f = open("input/day7", "r")
    bets = f.read().split("\n")

    b = []
    for bet in bets:
        hand,bid = bet.split(" ")
        b.append(BetWithJoker(hand, bid))

    b.sort()

    return b

bets = parseDataWithJokers()
betsCount = len(bets)
sum = 0
for index in range(len(bets)):
    bet = bets[index]
    sum += bet.bid * (index + 1)


print(sum)