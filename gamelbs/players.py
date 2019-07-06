class player:
	"""
	define player's attributes and methods:
		attributes:
			cards
			money
			total score
			bet
	"""
	
	def __init__(self,name,money):
		self.name = name
		self.hand = []
		self.money = money
		self.score = 0
		self.betting_money = 0
		
	def hit(self,deckname):
		"""
		ask for a new card.
		the card is added to the hand
		"""
		self.hand.append(deckname.popcard())
		
	def bet(self,amount):
		"""
		handle betting
		"""
		self.betting_money = amount
		self.money -= amount
	
	

class cpu:
	"""
	define cpu attributes and methods:
		cards
		first card up or down
		total score
	"""

	def __init__(self):
		self.name = 'cpu'
		self.hand = []
		self.score = 0

	def hit(self,deckname):
		"""
		cpu hand
		handle first card down
		"""
		self.hand.append(deckname.popcard())