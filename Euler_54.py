ranks = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']

# helper functions
def cardRank(array):
    return getRank(array[0])
def getRank(value):
    return ranks.index(value)
def firstValueInArray(array):
    return array[0]

# returns an array of all possible poker hands that can be made using the cards in cardArray
def getHand(cardArray):
    # print(cardArray)
    hands = []
    allCardsSameSuit = False # true if all cards in the array are of the same suit
    consecutiveValues = False

    cardArray.sort(key=cardRank)

    # Check for matching suits
    if len(set([x[1] for x in cardArray])) == 1:
        allCardsSameSuit = True

    # Check for consecutive values
    cardRanks = []
    for x in cardArray:
        cardRanks.append(getRank(x[0]))
    cardRanks.sort()
    if (cardRanks[0] + 4 == cardRanks[1] + 3 == cardRanks[2] + 2 == cardRanks[3] + 1 == cardRanks[4]):
        consecutiveValues = True

    if allCardsSameSuit and consecutiveValues:
        # Check for a royal flush
        if [x[0] for x in cardArray] == ranks[-5:]:
            hands.append([10, cardArray[0][1]])
        else:
            # Checks for a straight flush
            hands.append([9, cardArray[0][0]])

    # Check for a four of a kind and full houses
    cardValueSet = set([x[0] for x in cardArray])
    if len(cardValueSet) == 2:
        for y in cardValueSet:
            if len([x[0] for x in cardArray if x[0] == y]) == 4:
                hands.append([8, y])
            elif len([x[0] for x in cardArray if x[0] == y]) == 3:
                hands.append([7, y])

    # Flush
    if allCardsSameSuit:
        hands.append([6, cardArray[0][1]])

    # Straight
    if consecutiveValues:
        hands.append([5, cardArray[0][0]])

    # Three of a kinds and pairs
    for y in cardValueSet:
        nrOfCardsOfSaidValue = len([x[0] for x in cardArray if x[0] == y]) # reducing the number of list comprehensions
        if nrOfCardsOfSaidValue == 3:
            hands.append([4, y])
        elif nrOfCardsOfSaidValue == 2:
            hands.append([2, y])

    # two pairs
    if len([x for x in hands if x[0] == 2]) == 2:
        hands.append([3, max([x[0] for x in hands if x[0] == 2])])

    # High card
    for c in cardArray:
        hands.append([1, c[0]])

    hands.sort(key= firstValueInArray)
    return hands

p1Wins = 0
p2Wins = 0

with open('ProblemFiles/Problem_54.txt') as f:
    for line in f:
        cards = line.strip().split(' ')
        cards = [list(x) for x in cards]
        for c in cards:
            try:
                c[0] = int(c[0])
            except:
                pass

        p1Cards = cards[:5]
        p2Cards = cards[5:]

        p1Hands = getHand(p1Cards)
        p2Hands = getHand(p2Cards)


        while True:
            if p1Hands[-1][0] != p2Hands[-1][0]:
                if p1Hands[-1][0] > p2Hands[-1][0]:
                    p1Wins +=1
                    break
                else:
                    p2Wins +=1
                    break
            else:
                if (ranks.index(p1Hands[-1][1]) != ranks.index(p2Hands[-1][1])) and p1Hands[-1][0] not in [6, 9, 10]:
                    if ranks.index(p1Hands[-1][1]) > ranks.index(p2Hands[-1][1]):
                        p1Wins += 1
                        break
                    else:
                        p2Wins += 1
                        break

            # Equal hands or high cards
            if p1Hands[-1][0] != 1:
                p1Hands = [x for x in p1Hands if x[0] == 1]
                p2Hands = [x for x in p2Hands if x[0] == 1]
                continue
            p1Hands = p1Hands[:-1]
            p2Hands = p2Hands[:-1]


print('Player 1:', p1Wins, 'Wins')
print('Player 2:', p2Wins, 'Wins')