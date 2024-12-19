from connect4_display import *
from connect4_logic import *


def startConnect4Game():
	game = Connect4Display(1280, 720, vsync = True)
	pyglet.clock.schedule_interval(game.update, 1.0/60)
	pyglet.app.run()


if __name__ == '__main__':
	startConnect4Game()