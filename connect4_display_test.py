from pyglet import app
from pyglet import shapes
import pyglet
from pyglet.window import Window

win = Window(1280, 720, vsync = True)
base_batch = pyglet.graphics.Batch()


# create board
vline1 = shapes.Line(100 + 300, 0 + 20, 100 + 300, 600 + 20, width = 10, color = (255, 255, 255), batch = base_batch)
vline2 = shapes.Line(200 + 300, 0 + 20, 200 + 300, 600 + 20, width = 10, color = (255, 255, 255), batch = base_batch)
vline3 = shapes.Line(300 + 300, 0 + 20, 300 + 300, 600 + 20, width = 10, color = (255, 255, 255), batch = base_batch)
vline4 = shapes.Line(400 + 300, 0 + 20, 400 + 300, 600 + 20, width = 10, color = (255, 255, 255), batch = base_batch)
vline5 = shapes.Line(500 + 300, 0 + 20, 500 + 300, 600 + 20, width = 10, color = (255, 255, 255), batch = base_batch)
vline6 = shapes.Line(600 + 300, 0 + 20, 600 + 300, 600 + 20, width = 10, color = (255, 255, 255), batch = base_batch)
vline7 = shapes.Line(700 + 300, 0 + 20, 700 + 300, 600 + 20, width = 10, color = (255, 255, 255), batch = base_batch)
vline8 = shapes.Line(800 + 300, 0 + 20, 800 + 300, 600 + 20, width = 10, color = (255, 255, 255), batch = base_batch)

hline0 = shapes.Line(100 + 300,   0 + 20, 800 + 300,   0 + 20, width = 10, color = (255, 255, 255), batch = base_batch)
hline1 = shapes.Line(100 + 300, 100 + 20, 800 + 300, 100 + 20, width = 10, color = (255, 255, 255), batch = base_batch)
hline2 = shapes.Line(100 + 300, 200 + 20, 800 + 300, 200 + 20, width = 10, color = (255, 255, 255), batch = base_batch)
hline3 = shapes.Line(100 + 300, 300 + 20, 800 + 300, 300 + 20, width = 10, color = (255, 255, 255), batch = base_batch)
hline4 = shapes.Line(100 + 300, 400 + 20, 800 + 300, 400 + 20, width = 10, color = (255, 255, 255), batch = base_batch)
hline5 = shapes.Line(100 + 300, 500 + 20, 800 + 300, 500 + 20, width = 10, color = (255, 255, 255), batch = base_batch)
hline6 = shapes.Line(100 + 300, 600 + 20, 800 + 300, 600 + 20, width = 10, color = (255, 255, 255), batch = base_batch)

# label columns

label1 = pyglet.text.Label('1', font_size = 36, x = 150 + 300, y = 600 + 20 + 40, anchor_x = 'center', anchor_y = 'center', batch = base_batch)
label2 = pyglet.text.Label('2', font_size = 36, x = 250 + 300, y = 600 + 20 + 40, anchor_x = 'center', anchor_y = 'center', batch = base_batch)
label3 = pyglet.text.Label('3', font_size = 36, x = 350 + 300, y = 600 + 20 + 40, anchor_x = 'center', anchor_y = 'center', batch = base_batch)
label4 = pyglet.text.Label('4', font_size = 36, x = 450 + 300, y = 600 + 20 + 40, anchor_x = 'center', anchor_y = 'center', batch = base_batch)
label5 = pyglet.text.Label('5', font_size = 36, x = 550 + 300, y = 600 + 20 + 40, anchor_x = 'center', anchor_y = 'center', batch = base_batch)
label6 = pyglet.text.Label('6', font_size = 36, x = 650 + 300, y = 600 + 20 + 40, anchor_x = 'center', anchor_y = 'center', batch = base_batch)
label7 = pyglet.text.Label('7', font_size = 36, x = 750 + 300, y = 600 + 20 + 40, anchor_x = 'center', anchor_y = 'center', batch = base_batch)


def draw_marker(position_list):
	for i in range(0, len(position_list)):
		if i % 2 == 0:
			marker_color = (255,0,0)
		else:
			marker_color = (255,255,0)

		column = int(position_list[i]) - 1
		row = int(position_list[0:i+1].count(position_list[i])) - 1

		shapes.Circle(x = (100 * column) + 150 + 300, y = (100 * row) + 50 + 20, radius = 45, color = marker_color).draw()


@win.event
def on_draw():
	base_batch.draw()
	position_list = '12214745'
	draw_marker(position_list)


def update(dt):
	win.clear()
	position_list = '122147456'	
	draw_marker(position_list)


pyglet.clock.schedule_interval(update, 1.0/1)



app.run()


# space dedicated for rows 100
# space dedicated for columns 160

#line = shapes.Line(320, 0, 320, 1120, width = 5, color = (255, 255, 255), batch = base_batch)


# label = pyglet.text.Label('Hello, world',
#                           font_name='Times New Roman',
#                           font_size=36,
#                           x=window.width//2, y=window.height//2,
#                           anchor_x='center', anchor_y='center')