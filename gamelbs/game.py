class interface:
	"""
	defone the genertal outline of the objects in the game
	"""
	def __init__(self):
		self.top = '-----   blackjack   -----'

		

class game_status:
	"""
	get the values based on the cards on screen.
	elaborate game's score and present it.
	present winner
	"""
	def __init__(self):
		pass



class game_interaction:
	"""
	present the line asking for all actions:
		start new game/exit/restart
		bet
		hit/stay
	"""
	def __init__(self):
		pass



class new_game:
	"""
	list of actions for new game:
		start
		load
		restart
		exit
		acquire user name, amount
		remember tu destroy
	"""
	def __init__(self, username, starting_amount):
		self.username = username
		self.starting_amount = starting_amount



class bet:
	"""
	bet at the beginning of the game
	"""
	def __init__(self):
		pass



class gamble:
	"""
	ask to hit or stay
	"""
	def __init__(self):
		pass