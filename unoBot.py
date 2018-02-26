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
        print self.name + " draws " + str(len(drawnCards)) + " cards"
        while( i < len(drawnCards)):
            self.hand.append(drawnCards[i])
            i += 1

    def playCard(self, numCardToPlay):
        return self.hand.pop((numCardToPlay))

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
    
    def append(self, card):
        self.unoDeck.append(card)
        
class table():
    def __init__(self, deck):
        self.deck = deck
        self.playerList = []
        self.pile = []
        self.currentPlayer = 0
        self.direction = 1
        self.gameOver = False
    
    def createPlayer(self, playerName):
        self.playerList.append(player(playerName))

    def dealOpeners(self):
        for item in self.playerList:
            item.drawCards(self.deck.dealCards(7))
    
    def playerPlayCard(self, playerNum, cardNum):
        colors = ["Red", "Green", "Yellow", "Blue"]
        playedCard = self.playerList[playerNum].playCard(cardNum)
        if (playedCard.denom == 11):
            ##print "Reverse code goes here"
            self.direction *= -1
        if (playedCard.denom == 12):
            ##print "Draw 2 code goes here"
            drawingPlayer = playerNum + self.direction
            if (drawingPlayer == 4):
                drawingPlayer = 0
            if (drawingPlayer == -1):
                drawingPlayer = 3
            self.playerList[drawingPlayer].drawCards(self.deck.dealCards(2))
        if (playedCard.denom == 13):
            ##print "Wildcard code goes here"
            colorPicker = randrange(0,3)
            playedCard.color = colors[colorPicker]
            print "Chosen color is: " + str(playedCard.color)
        if (playedCard.denom == 14):
            ##print "Wildcard +4 code goes here"
            drawingPlayer = playerNum + self.direction
            if (drawingPlayer == 4):
                drawingPlayer = 0
            if (drawingPlayer == -1):
                drawingPlayer = 3
            self.playerList[drawingPlayer].drawCards(self.deck.dealCards(4))
            colorPicker = randrange(0,3)
            playedCard.color = colors[colorPicker]
            print "Chosen color is: " + str(playedCard.color)
        ##self.currentPlayer += self.direction
        ##if (self.currentPlayer == 4):
            ##self.currentPlayer = 0
        ##if (self.currentPlayer == -1):
            ##self.currentPlayer = 3
        self.pile.append(playedCard)

    def getValidPlays(self, playerNum):
        pileTop = self.pile[-1]
        validCards = []
        i = 0
        for item in self.playerList[playerNum].hand:
            if((item.denom == pileTop.denom) or (item.color == pileTop.color)):
                validCards.append(i)
            if(item.color == "Wild"):
                validCards.append(i)
            i += 1
        return validCards

    def takeTurn(self, playerNum):
        ##print self.currentPlayer
        if (self.deck.length() <= 5):
            self.shufflePile()
        ##print "Top card of pile is : " + str(self.pile[-1])
        makePlay = True
        validPlays = self.getValidPlays(playerNum)
        if (len(validPlays) == 0):
            print self.playerList[playerNum].name + " can't make a move and draws a card"
            self.playerList[playerNum].drawCards(self.deck.dealCards(1))
            validPlays = self.getValidPlays(playerNum)
            if (len(validPlays) == 0):
                print "No plays available for " + self.playerList[playerNum].name + ", passing turn"
                ##self.currentPlayer += self.direction
                ##if (self.currentPlayer == 4):
                    ##self.currentPlayer = 0
                ##if (self.currentPlayer == -1):
                    ##self.currentPlayer = 3
                makePlay = False
        if (makePlay == True):
            if (len(validPlays) == 1):
                picker = 0
            else:
                picker = (randrange(1,len(validPlays)))
                picker -= 1
            ##print "Cards in hand: "
            ##for item in self.playerList[playerNum].hand:
                ##print item
            ##print "picker "+ str(picker)
            ##print "valid plays:"
            ##for item in validPlays:
                ##print item
            print str(self.playerList[playerNum].name) + " plays: " + str(self.playerList[playerNum].hand[validPlays[picker]])
            self.playerPlayCard(playerNum, validPlays[picker])
            if (len(self.playerList[playerNum].hand) == 1):
                print "UNO!"
            if (len(self.playerList[playerNum].hand) == 0):
                print "Game Over!"
                self.gameOver = True
                print "Winner: " + self.playerList[playerNum].name


        self.currentPlayer = self.currentPlayer + self.direction
        if (self.currentPlayer == 4):
            self.currentPlayer = 0
        if (self.currentPlayer == -1):
            self.currentPlayer = 3
        ##print self.currentPlayer

    def shufflePile(self):
        pileCard = self.pile.pop(-1)
        for item in self.pile:
            if (item.denom == "Card" or item.denom == "Card +4"):
                item.color = "Wild"
            self.deck.append(item)
        self.pile = [pileCard]
        self.deck.shuffle()

def createTable():
    currentDeck = unoDeck()
    currentDeck.shuffle()
    theTable = table(currentDeck)
    theTable.createPlayer("Player 1")
    theTable.createPlayer("Player 2")
    theTable.createPlayer("Player 3")
    theTable.createPlayer("Player 4")
    theTable.dealOpeners()
    theTable.pile.append(theTable.deck.dealCards(1)[0])
    while (theTable.pile[-1].color == "Wild"):
        theTable.pile.append(theTable.deck.dealCards(1)[0])
    return theTable

currentTable = createTable()
print "Top card of pile is : " + str(currentTable.pile[-1])
while (currentTable.gameOver == False):
    currentTable.takeTurn(currentTable.currentPlayer)
for player in currentTable.playerList:
    print player.name
    print len(player.hand)
    for card in player.hand:
        print card


