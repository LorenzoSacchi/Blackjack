import random

class Card:
    """
    create a single card.
    must pass number and sign
    output is an object with 4 attributes:
            number
            sign
            outline
            face up or down
    """
    pass
    def __init__(self,value,value_name,sign,sign_name):
        # card number (1 to 11)
        self.value = value
        self.number = value
        self.value_name = value_name
        # card sign (aces,spades,clubs hearts)
        self.sign = sign
        self.sign_name = sign_name


    def outfit(self):
        """
        create the card object
        """
        if self.number == 11:
            outfit = ' ---\n|'+ self.sign +'  |\n| ' + 'J' + ' |\n|  '+ self.sign +'|\n ---'
            self.value = 10
        elif self.number == 12:
            outfit = ' ---\n|'+ self.sign +'  |\n| ' + 'Q' + ' |\n|  '+ self.sign +'|\n ---'
            self.value = 10
        elif self.number == 13:
            outfit = ' ---\n|'+ self.sign +'  |\n| ' + 'K' + ' |\n|  '+ self.sign +'|\n ---'
            self.value = 10
        elif self.number == 1:
            outfit = ' ---\n|'+ self.sign +'  |\n| ' + 'A' + ' |\n|  '+ self.sign +'|\n ---'
            self.value = 11
        elif self.number == 10:
            outfit = ' ---\n|'+ self.sign +'  |\n| ' + str(self.number) + '|\n|  '+ self.sign +'|\n ---'
            self.value = 10
        else:
            outfit = ' ---\n|'+ self.sign +'  |\n| ' + str(self.number) + ' |\n|  '+ self.sign +'|\n ---'
        return outfit

    def outfit_card_down(self):
        """
        create the covered card for the dealer
        """
        outfit = ' ---\n|###|\n|###|\n|###|\n ---'
        return outfit


class Deck:
    """
    create the deck
    methods can shuffle and pop a card on top of the deck
    card down is not present
            for each card create the object and add to the complete_deck
            return the complete_deck
    """

    def __init__(self):
        self.complete_deck = []
        self.deck_signs = {'Hearts': 'h', 'Diamonds': 'd', 'Clubs': 'c', 'Spades': 's'}
        self.deck_vocabulary = {'Ace':  1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13}


        for sign_name,sign in self.deck_signs.items():
            for singlecard_name,singlecard in self.deck_vocabulary.items():
                self.complete_deck.append(Card(singlecard, singlecard_name, sign, sign_name))

    def mix(self):
        """
        shuffle card before drawing
        """
        random.shuffle(self.complete_deck)

    def popcard(self):
        """
        draw first card
        """
        drawn_card = self.complete_deck.pop()
        return drawn_card

