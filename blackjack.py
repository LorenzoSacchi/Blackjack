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
	print('ok')
	
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
	#ShuffledDeck = AllDeck.shuffle()
	for i in range(52):
		#
		print(AllDeck.entiredeck()[i].outfit())
		#print (ShuffledDeck[i])
		#print(AllDeck.entiredeck()[9].outfit_card_down())
		#print(AllDeck.entiredeck()[9].value_name)
		#print(AllDeck.entiredeck()[9].sign_name)

#here the program is started
if __name__ == "__main__":
	#main()
	testoutput()

