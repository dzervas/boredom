from curtsies import input
from curtsies.window import FullscreenWindow
from curtsies.formatstringarray import FSArray
from curtsies.formatstring import fmtstr
from random import randrange
from time import time
import sys

# Body and head ascii form of the snake and apple.
	# head, body, apple, space
theme = [ ' ', fmtstr('o', "green", "on_green"), fmtstr('0', "blue", "on_green"), fmtstr('@', "red") ]
sspeed = 3
acc = 1

# Moves the snake one step
# hcoor: Coordinates of the snake's head. [row, column]
# hcoor: Coordinates of the snake's last bit of tail. [row, column]
def step():
	global theme, screen, hcoor, tcoor, moves, length

	oldcoor = hcoor
	# Override previous head with new body
	screen[hcoor[0], hcoor[1]] = theme[1]
	# Remove old tail
	screen[tcoor[0], tcoor[1]] = theme[0]

	# Place head (not really, just update the coords)
	if moves[-1] == "up":
		hcoor[0] -= 1
	elif moves[-1] == "down":
		hcoor[0] += 1
	elif moves[-1] == "right":
		hcoor[1] += 1
	elif moves[-1] == "left":
		hcoor[1] -= 1
	else:
		# Something is really wrong here...
		return

	# Check to see if out of bounds or ate yourself
	try:
		if screen[hcoor[0], hcoor[1]][0] == theme[1]:
			sys.exit()
	except IndexError:
		sys.exit()

	# Check for apple (we have the coords of the future head)
	# If we hit an apple, the body grows larger by one,
	# so we skip a pop to make the stack larger by one.
	# Maybe a way that would support growth apart from 1 would be nice
	if screen[hcoor[0], hcoor[1]][0] == theme[3]:
		apple()
		tdir = None
	else:
		tdir = moves.pop(0)

	# Place the head (for real this time)
	screen[hcoor[0], hcoor[1]] = theme[2]

	# Update the tail coords
	# We do not remove the tail yet, it will be remove in the next round
	# in order to let the possibility of apple hit.
	if tdir == "up":
		tcoor[0] -= 1
	elif tdir == "down":
		tcoor[0] += 1
	elif tdir == "right":
		tcoor[1] += 1
	elif tdir == "left":
		tcoor[1] -= 1

# You ate an apple! Bravo!
def apple():
	global theme, screen, points, length, rows, columns, speed, acc

	# Do the math...
	points += 1
	length += 1
	speed += acc

	# and spawn a new apple
	coords = [randrange(0, rows), randrange(0, columns)]

	while screen[coords[0], coords[1]] == theme[0]:
		coords = [randrange(0, rows), randrange(0, columns)]

	screen[coords[0], coords[1]] = theme[3]

with FullscreenWindow(sys.stdout) as w:
	with input.Input(sys.stdin) as input_generator:
		rows, columns = w.t.height, w.t.width
		hcoor = [rows / 2 - 3, columns / 2]
		tcoor = [rows / 2, columns / 2]

		# Some default values to start with...
		direction = "up"
		length = 3

		points = 0
		speed = sspeed
		last = time()
		moves = []
		# "moves" holds the stack of movements. When you move the head,
		# the tail should not move at the same time. It has "latency"
		# equal to the length of the snake's tail, so every time you
		# move (the head), the move is saved to be done later.

		for _ in range(length):
			moves.append(direction)

		screen = FSArray(rows, columns)

		# Spawn an apple for the first time
		coords = [randrange(0, rows), randrange(0, columns)]
		while screen[coords[0], coords[1]] == theme[0]:
			coords = [randrange(0, rows), randrange(0, columns)]
		screen[coords[0], coords[1]] = theme[3]

		# Main loop
		while True:
			print points

			# Movement routine
			if time() - last >= 1.0 / speed:
				last = time()

				moves.append(direction)

				step()

			# XXX: Find a non-blocking solution
			c = input_generator.next()
#
			# Key bindings
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
