from pyglet import app
from pyglet import shapes
import pyglet
from pyglet.window import Window
from connect4_logic import *


class Connect4Display(pyglet.window.Window):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.board_batch = pyglet.graphics.Batch()
		self.marker_batch = pyglet.graphics.Batch()
		self.label_batch = pyglet.graphics.Batch()
		self.GameLogic = Connect4Logic()

	def setup_board(self):
		self.vline1 = shapes.Line(100 + 300, 0 + 20, 100 + 300, 600 + 20, width = 10, color = (255, 255, 255), batch = self.board_batch)
		self.vline2 = shapes.Line(200 + 300, 0 + 20, 200 + 300, 600 + 20, width = 10, color = (255, 255, 255), batch = self.board_batch)
		self.vline3 = shapes.Line(300 + 300, 0 + 20, 300 + 300, 600 + 20, width = 10, color = (255, 255, 255), batch = self.board_batch)
		self.vline4 = shapes.Line(400 + 300, 0 + 20, 400 + 300, 600 + 20, width = 10, color = (255, 255, 255), batch = self.board_batch)
		self.vline5 = shapes.Line(500 + 300, 0 + 20, 500 + 300, 600 + 20, width = 10, color = (255, 255, 255), batch = self.board_batch)
		self.vline6 = shapes.Line(600 + 300, 0 + 20, 600 + 300, 600 + 20, width = 10, color = (255, 255, 255), batch = self.board_batch)
		self.vline7 = shapes.Line(700 + 300, 0 + 20, 700 + 300, 600 + 20, width = 10, color = (255, 255, 255), batch = self.board_batch)
		self.vline8 = shapes.Line(800 + 300, 0 + 20, 800 + 300, 600 + 20, width = 10, color = (255, 255, 255), batch = self.board_batch)

		self.hline0 = shapes.Line(100 + 300,   0 + 20, 800 + 300,   0 + 20, width = 10, color = (255, 255, 255), batch = self.board_batch)
		self.hline1 = shapes.Line(100 + 300, 100 + 20, 800 + 300, 100 + 20, width = 10, color = (255, 255, 255), batch = self.board_batch)
		self.hline2 = shapes.Line(100 + 300, 200 + 20, 800 + 300, 200 + 20, width = 10, color = (255, 255, 255), batch = self.board_batch)
		self.hline3 = shapes.Line(100 + 300, 300 + 20, 800 + 300, 300 + 20, width = 10, color = (255, 255, 255), batch = self.board_batch)
		self.hline4 = shapes.Line(100 + 300, 400 + 20, 800 + 300, 400 + 20, width = 10, color = (255, 255, 255), batch = self.board_batch)
		self.hline5 = shapes.Line(100 + 300, 500 + 20, 800 + 300, 500 + 20, width = 10, color = (255, 255, 255), batch = self.board_batch)
		self.hline6 = shapes.Line(100 + 300, 600 + 20, 800 + 300, 600 + 20, width = 10, color = (255, 255, 255), batch = self.board_batch)

		# label columns

		self.label1 = pyglet.text.Label('1', font_size = 36, x = 150 + 300, y = 600 + 20 + 40, anchor_x = 'center', anchor_y = 'center', batch = self.board_batch)
		self.label2 = pyglet.text.Label('2', font_size = 36, x = 250 + 300, y = 600 + 20 + 40, anchor_x = 'center', anchor_y = 'center', batch = self.board_batch)
		self.label3 = pyglet.text.Label('3', font_size = 36, x = 350 + 300, y = 600 + 20 + 40, anchor_x = 'center', anchor_y = 'center', batch = self.board_batch)
		self.label4 = pyglet.text.Label('4', font_size = 36, x = 450 + 300, y = 600 + 20 + 40, anchor_x = 'center', anchor_y = 'center', batch = self.board_batch)
		self.label5 = pyglet.text.Label('5', font_size = 36, x = 550 + 300, y = 600 + 20 + 40, anchor_x = 'center', anchor_y = 'center', batch = self.board_batch)
		self.label6 = pyglet.text.Label('6', font_size = 36, x = 650 + 300, y = 600 + 20 + 40, anchor_x = 'center', anchor_y = 'center', batch = self.board_batch)
		self.label7 = pyglet.text.Label('7', font_size = 36, x = 750 + 300, y = 600 + 20 + 40, anchor_x = 'center', anchor_y = 'center', batch = self.board_batch)
		
		self.board_batch.draw()

	def draw_marker(self):
		for i in range(0, len(self.GameLogic.position)):
			if i % 2 == 0:
				marker_color = (255,0,0)
			else:
				marker_color = (255,255,0)

			column = int(self.GameLogic.position[i]) - 1
			row = int(self.GameLogic.position[0:i+1].count(self.GameLogic.position[i])) - 1

			self.marker = shapes.Circle(x = (100 * column) + 150 + 300, y = (100 * row) + 50 + 20, radius = 45, color = marker_color, batch = self.marker_batch)
			self.marker_batch.draw()

	def draw_game_labels(self):
		#Game Title (Static)
		self.game_title = pyglet.text.Label('Connect 4', font_size = 36, x = 180 , y = 600 + 20 + 40, anchor_x = 'center', anchor_y = 'center', batch = self.label_batch)
		
		#Game Status (Changes to Game Over when Game is done)
		game_status_label = 'In Progress' if self.GameLogic.has_winner == False else 'Game Over'
		self.game_status = pyglet.text.Label('Game Status: ' + game_status_label, font_size = 18, x = 180 , y = 600 , anchor_x = 'center', anchor_y = 'center', batch = self.label_batch)

		#Turn Label (Calls for Player to place marker)
		if self.GameLogic.has_winner == False and self.GameLogic.has_slots == True:
			turn_label = 'Player 1 (Red)' if len(self.GameLogic.position) % 2 == 0 else 'Player 2 (Yellow)'	
			self.player_turn = pyglet.text.Label(turn_label + " place your marker!", font_size = 14, x = 180 , y = 500 , anchor_x = 'center', anchor_y = 'center', batch = self.label_batch)
		else:
			turn_label = 'No more moves!'
			self.player_turn = pyglet.text.Label(turn_label, font_size = 14, x = 180 , y = 500 , anchor_x = 'center', anchor_y = 'center', batch = self.label_batch)

		#Winner Label 
		if self.GameLogic.has_winner:
			winner_label = 'Player 1 Wins!' if self.GameLogic.winner == 'A' else 'Player 2 Wins!'
			self.winner_msg = pyglet.text.Label(winner_label, font_size = 14, x = 180 , y = 400 , anchor_x = 'center', anchor_y = 'center', batch = self.label_batch)

		self.label_batch.draw()

	def on_draw(self):
		self.clear()
		self.setup_board()
		self.draw_game_labels()
		self.draw_marker()

	def on_key_press(self, symbol, modifiers):
		if symbol >= pyglet.window.key._0 and symbol <= pyglet.window.key._9:
			try:
				self.GameLogic.execute_turn(int(chr(symbol)))
			except ValueError as e:
				pass


	def update(self, dt):
		self.clear()
		self.on_draw()


