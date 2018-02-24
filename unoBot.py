from random import randrange

class unoCard():
    def __init__(self, color, denom):
        self.color = color
        self.denom = denom

    def __str__(self):
        value = ""
        if(self.denom > -1 and self.denom < 11):
            value = str(self.denom)
        if(self.denom == 11):
            value = "Reverse"
        if(self.denom == 12):
            value = "Draw 2"
        if(self.denom == 13):
            value = "Card"
        if(self.denom == 14):
            value = "Card +4"
        return (str(self.color) + " " + value)

class player():
    def __init__(self, name):
        self.hand = []
        self.name = name
    
    def __str__(self):
        return self.name

    def drawCards(self, drawnCards):
        i = 0
        while( i < len(drawnCards)):
            self.hand.append(drawnCards[i])
            i += 1

class unoDeck():
    def __init__(self):
        unoDeck = []
        colors = ["Red", "Green", "Yellow", "Blue"]
        colorDenoms = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12]
        for color in colors:
            for denom in colorDenoms:
                unoDeck.append(unoCard(color, denom))
        for i in range(1,5):
            unoDeck.append(unoCard("Wild", 13))
            unoDeck.append(unoCard("Wild", 14))
        self.unoDeck = unoDeck

    def shuffle(self):
        for i in range(len(self.unoDeck)-1, 0, -1):
            j = randrange(i + 1)
            self.unoDeck[i], self.unoDeck[j] = self.unoDeck[j], self.unoDeck[i]
    
    def dealCards(self, numCards):
        toDeal = []
        i = 0
        while (i < numCards):
            toDeal.append(self.unoDeck.pop())
            i += 1
        return toDeal

    def length(self):
        return len(self.unoDeck)
        
class table():
    def __init__(self, deck):
        self.deck = deck
        self.playerList = []
    
    def createPlayer(self, playerName):
        self.playerList.append(player(playerName))

    def dealOpeners(self):
        for item in self.playerList:
            item.drawCards(self.deck.dealCards(7))
        
def createTable():
    currentDeck = unoDeck()
    currentDeck.shuffle()
    theTable = table(currentDeck)
    theTable.createPlayer("Player 1")
    theTable.createPlayer("Player 2")
    theTable.createPlayer("Player 3")
    theTable.createPlayer("Human Player")
    theTable.dealOpeners()
    return theTable

currentTable = createTable()
for item in currentTable.playerList:
    print item.name
    for card in item.hand:
        print card
    print "\n"




