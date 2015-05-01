from curtsies import input
from curtsies.window import FullscreenWindow
from curtsies.formatstringarray import FSArray
from curtsies.formatstring import fmtstr
from random import randrange
from time import time
import sys

# Body and head ascii form of the snake and apple.
	# head, body, apple, space
theme = [ ' ', 'o', '0', '@' ]
sspeed = 3
acc = 1

# Moves the snake one step
# hcoor: Coordinates of the snake's head. [row, column]
# hcoor: Coordinates of the snake's last bit of tail. [row, column]
def step():
	global theme, screen, hcoor, tcoor, moves, length

	oldcoor = hcoor
	result = screen
	# Override body (previous head)
	result[hcoor[0], hcoor[1]] = theme[1]
	# Remove old tail
	result[tcoor[0], tcoor[1]] = theme[0]

	# Place head
	if moves[-1] == "up":
		hcoor[0] -= 1
	elif moves[-1] == "down":
		hcoor[0] += 1
	elif moves[-1] == "right":
		hcoor[1] += 1
	elif moves[-1] == "left":
		hcoor[1] -= 1
	else:
		return

	if result[hcoor[0], hcoor[1]][0] == theme[3]:
		apple()
		tdir = None
	else:
		tdir = moves.pop(0)

	result[hcoor[0], hcoor[1]] = theme[2]

	if tdir == "up":
		tcoor[0] -= 1
	elif tdir == "down":
		tcoor[0] += 1
	elif tdir == "right":
		tcoor[1] += 1
	elif tdir == "left":
		tcoor[1] -= 1

	screen = result

def apple():
	global theme, screen, points, length, rows, columns, speed, acc

	points += 1
	length += 1
	speed += acc

	coords = [randrange(0, rows), randrange(0, columns)]

	while screen[coords[0], coords[1]] == theme[0]:
		coords = [randrange(0, rows), randrange(0, columns)]

	screen[coords[0], coords[1]] = theme[3]

with FullscreenWindow(sys.stdout) as w:
	with input.Input(sys.stdin) as input_generator:
		rows, columns = w.t.height, w.t.width
		hcoor = [rows / 2 - 3, columns / 2]
		tcoor = [rows / 2, columns / 2]

		direction = "up"
		length = 3
		points = 0

		speed = sspeed
		last = time()
		moves = []

		for _ in range(length):
			moves.append(direction)

		screen = FSArray(rows, columns)

		coords = [randrange(0, rows), randrange(0, columns)]
		while screen[coords[0], coords[1]] == theme[0]:
			coords = [randrange(0, rows), randrange(0, columns)]
		screen[coords[0], coords[1]] = theme[3]

		while True:
			print points
			if time() - last >= 1.0 / speed:
				last = time()

				moves.append(direction)

				step()

			c = input_generator.next()
#
			if c == "w" and direction != "down":
				direction = "up"
			elif c == "s" and direction != "up":
				direction = "down"
			elif c == "d" and direction != "left":
				direction = "right"
			elif c == "a" and direction != "right":
				direction = "left"
			elif c == "q":
				sys.exit() # same as raise SystemExit()

			w.render_to_terminal(screen)
