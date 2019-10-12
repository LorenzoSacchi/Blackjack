import gamelbs.deck as deck
import gamelbs.game as game
import gamelbs.players as players


#here is the main function
def main():
    """
    at open create player based on the create or restore from saved game.
    at first run create deck and shuffle.
    at every run:
            save status.
            refresh screen.
            evaluate the game status.
            create interface.
            put things in place.
    if there is a winner exit status with exit menu asking to continue/restart
    """
    pass


def testoutput():
    #single card creation
    #Ace = deck.Card(1,'h')
    #print(dir(Ace))
    #print(Ace.outfit())
    #print(Ace.outfit_card_down())
    #print(Ace.value)
    #print(Ace.sign)

    #all deck creation. all values accessibe. shuffle
    AllDeck = deck.Deck()
    AllDeck.mix()
    #create Player1
    Player1 = players.player('unzia',100)
    #ask to hit. name is tied to deck name
    #Player1.hit(AllDeck)
    #print(Player1.hand[0].outfit())
    #for each hit see cards and score
    #aces logic to be done
    #print(Player1.score)
    #Player1.score += Player1.hand[0].value
    #print(Player1.score)

    #Player1.hit(AllDeck)
    #print(Player1.hand[1].outfit())
    #print(Player1.score)
    #Player1.score += Player1.hand[1].value
    #print(Player1.score)

    #bet logic
    #Player1.bet(5)
    #print(Player1.betting_money)
    #print(Player1.money)



    #print all deck or a card
    #for i in range(52):
            #print(AllDeck.entiredeck()[i].outfit())
            #print (ShuffledDeck[i])
            #print(AllDeck.entiredeck()[9].outfit_card_down())
            #print(AllDeck.entiredeck()[9].value_name)
            #print(AllDeck.entiredeck()[9].sign_name)
            #print(AllDeck.complete_deck[i].outfit())
            #print(AllDeck.complete_deck[i].outfit_card_down())
            #print(AllDeck.complete_deck[i].value_name, 'of' ,AllDeck.complete_deck[i].sign_name)
            #print(AllDeck.complete_deck[i].value, 'of' ,AllDeck.complete_deck[i].sign)
    #decide card number. create a hand with first card down. must be part of player and cpu methods
    cardnumber = 2
    hand = []
    for i in range(cardnumber):
        hand.append(AllDeck.popcard())

    print(hand[0].outfit_card_down())
    #print(hand[0].value_name, 'of' ,hand[0].sign_name)
    for k in range(1,cardnumber):
        print(hand[k].outfit())
        #print(hand[k].outfit())
        print(hand[k].value_name, 'of' ,hand[k].sign_name)
        #print(hand[k].value)
        #print(hand[k].number)



# --- Here the program is started ---
if __name__ == "__main__":
    #main()
    testoutput()

