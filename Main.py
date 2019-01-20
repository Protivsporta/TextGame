import World 
from GameOver import GameOver

def run_game():

	new_world = World.World()

	while True:
		try:
			turn()
		except GameOver:
			break
	print('Game Over')

def turn(self):
	new_world = World()

if __name__ == "__main__": 
    run_game()	