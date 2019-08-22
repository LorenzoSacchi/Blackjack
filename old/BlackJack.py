import random
import console

#Class that creates a single card
class Card:
    """
    create one card
    methods:
        Onecard - return the card design
        OneValue - return the card actual value
    """        
    def __init__(self,card,value,sign):
        self.card = card
        self.value = value
        self.sign = sign
        
    def OneCard(self):
        if self.value == 11:
            thecard = ' ---\n|'+ self.sign +'  |\n| ' + 'J' + ' |\n|  '+ self.sign +'|\n ---'
            self.value = 10
        elif self.value == 12:
            thecard = ' ---\n|'+ self.sign +'  |\n| ' + 'Q' + ' |\n|  '+ self.sign +'|\n ---'
            self.value = 10
        elif self.value == 13:
            thecard = ' ---\n|'+ self.sign +'  |\n| ' + 'K' + ' |\n|  '+ self.sign +'|\n ---'
            self.value = 10
        elif self.value == 1:
            thecard = ' ---\n|'+ self.sign +'  |\n| ' + 'A' + ' |\n|  '+ self.sign +'|\n ---'
            self.value = 11
        else:
            thecard = ' ---\n|'+ self.sign +'  |\n| ' + self.card + ' |\n|  '+ self.sign +'|\n ---'
        return thecard
        
    def OneValue(self):
        thevalue = self.value
        return thevalue

#Create the entire deck, each card is an object in the array
class Deck:
    """
    create a list of object, ecah one is a card
    methods:
        Shuffle - shuffle deck
    """
    def __init__(self):
        self.CompleteDeck = []
        decksigns = {'Hearts': 'h', 'Diamonds': 'd', 'Clubs': 'c', 'Spades': 's'}
        deckvocabulary = {'Ace':  1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Eleven': 11, 'Twelve': 12, 'Thirteen': 13}
        for signs in decksigns:
            for singlecard in deckvocabulary:
                self.CompleteDeck.append(Card(str(deckvocabulary[singlecard]),deckvocabulary[singlecard],decksigns[signs]))
                
    def __str__(self):
        return self.CompleteDeck
        
    def Shuffle(self):
        random.shuffle(self.CompleteDeck)

        
                


        
class Game:
    """
    handle the game and each turn
    request if pass or hit.
    exit handles the win-lose-continue
    """
    def __init__(self,chips,bet):
        self.chips = chips
        self.bet = bet
    
    def Interface(self):
        return print(f'--- Blackjack ---\nChips:       {self.chips}\nCurrent bet: {self.bet}')
    
    def Outcome(self):
        pass


class Player:
    """
    handle players turn and amount of money, and bet
    """    
    def __init__(self,chips=100, bet=0,hand=[]):
        self.chips = chips
        self.bet = bet
        self.hand = hand
    
    def Bet(self):
        self.chips -= self.bet
        player = [self.chips,self.bet]
        return player
        
    def Hand(self):
        pass
    
    def Hit(self):
        pass
    
    def Pass(self):
        pass
        
    


class Starting:
    """
    starts the game, restarts, exits, refreshes screen.
    import setting as save-restore game on ini file
    reset game
    handle interface
    """
    def start(self):
        pass


class Hand:
    """
    create each player's hand
    add his cards if hit
"""
    
    
#here starts the main
#use main definition. improve interface

#create deck and show card and value
#deck = Deck()
#print(f'{deck.CompleteDeck[0].OneCard()}   {deck.CompleteDeck[0].OneValue()}')
#deck.Shuffle()
#print(f'{deck.CompleteDeck[0].OneCard()}   {deck.CompleteDeck[0].OneValue()}')

#start player and its basic amount, pass bet (more than one)
#play = Player(102, 5)
#play.Bet()
#print(f'{play.chips}   {play.bet}')
#play = Player(play.chips,3)
#play.Bet()
#print(f'{play.chips}   {play.bet}')

#interface
#game = Game(play.chips,play.bet)
#game.Interface()
#clear interface
#console.clear()

#create a hand by adding cards from the top of the deck
#obj= []
#obj.append(deck.CompleteDeck.pop())
#obj.append(deck.CompleteDeck.pop())
#print(obj[0].OneCard())
#print(obj[1].OneCard())
#print(f'{obj[0].OneValue()}')
#print(f'{obj[1].OneValue()}')
#print(f'total = {int(obj[0].OneValue()) + int(obj[1].OneValue())}')


