### New improved blackjack in python.
Still in progress. 


### Documentation (to do):
+ structure
+ tests
+ add images
+ create wiki
+ comment code

### Current notes:
__best aces logic:__ 
+ compute top outcome
+ if higher than 21 change one to 1
+ proceed until under 21
+ need an aces counter
+ keep if higher than 21 but no more aces

__game logic:__
+ at start ask player name and money to start with
+ refresh with ui
		
		
+ loop tru all cards.
+ print each card and sum the score
+ evaluate best aces
+ print score
+ evaluate if it is out
+ if out declare cpu the winner
+ if not ask for pass or hit
+ if hit restart from the loop
+ if pass go to cpu
+ refresh all ui

				
+ cpu
+ loop tru all cards.
+ print each card and sum the score
+ evaluate best aces
+ print score
+ if under player score hit 
+ if over player score and under 21 win
+ if over player and out lose
+ refresh all ui
		
	
+ evaluate new money for player
+ if zero endgame
+ if not ask to continue or exit


### future updates:
+ savegames
+ settings
+ use of generic deck
+ handle red+black background
+ add other games
+ graphical ui
