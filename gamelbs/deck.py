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
	def __init__(self,value,sign,up=False):
		# card number (1 to 11)
		self.value = value
		# card sign (aces,spades,clubs hearts)
		self.sign = sign
		#switcher to turn the card uo or down
		self.up = up
	
	def create(self):
		"""
		create the card object
		"""		
		pass
		if self.value == 11:
			outfit = ' ---\n|'+ self.sign +'  |\n| ' + 'J' + ' |\n|  '+ self.sign +'|\n ---'
			self.value = 10
		elif self.value == 12:
			outfit = ' ---\n|'+ self.sign +'  |\n| ' + 'Q' + ' |\n|  '+ self.sign +'|\n ---'
			self.value = 10
		elif self.value == 13:
			outfit = ' ---\n|'+ self.sign +'  |\n| ' + 'K' + ' |\n|  '+ self.sign +'|\n ---'
			self.value = 10
		elif self.value == 1:
			outfit = ' ---\n|'+ self.sign +'  |\n| ' + 'A' + ' |\n|  '+ self.sign +'|\n ---'
			self.value = 11
		else:
			outfit = ' ---\n|'+ self.sign +'  |\n| ' + self.card + ' |\n|  '+ self.sign +'|\n ---'
		return [outfit,self.value,self.sing,self.up]
	
	def create_card_down():
		"""
		create the covered card for the dealer
		"""
		self.up = False
		outfit = ' ---\n|###|\n|###|\n|###|\n ---'
		return [outfit,0,0,self.up]
	
	def turn(self):
		"""
		turn card up or down
		"""
		if self.up == False:
			self.up = True:
		else if self.up == True:
			self.up = False			
		
	
	
class Deck:
	"""
	create the deck
	methods can shuffle and pop a card on top of the deck
	card down is not present
	"""	
	
	def __init__(self):
		"""
		"""
		self.complete_deck = []
		self.deck_signs = {'Hearts': 'h', 'Diamonds': 'd', 'Clubs': 'c', 'Spades': 's'}
		self.deck_vocabulary = {'Ace':  1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Eleven': 11, 'Twelve': 12, 'Thirteen': 13}
		
	def entiredeck(self):
		"""
		for each card create the object and add to the complete_deck
		return the complete_deck
		"""
		pass
		for sign in self.deck_signs:
			for singlecard in self.deck_vocabulary:
				self.complete_deck.append(Card.create(singlecard,sign))
			#Card(str(deckvocabulary[singlecard]),deckvocabulary[singlecard],decksigns[signs]))	
			
	def __str__(self):
		return self.complete_deck
		
	def shuffle(self):
		random.shuffle(self.complete_deck)
		
	def popcard(self):
		"""
		draw first card
		"""
		drawn_card = self.complete_deck.pop()
		return drawn_card
