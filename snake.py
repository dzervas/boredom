from curtsies import input
from curtsies.window import FullscreenWindow
from curtsies.formatstringarray import FSArray
#from curtsies.termhelpers import Cbreak, Nonblocking
from time import time
import sys

# Body and head ascii form of the snake and apple.
	# head, body, apple, space
theme = [ ' ', 'o', '0', '@' ]
sspeed = 1
acc = 0.25
accevery = 5

# Moves the snake one step
# hcoor: Coordinates of the snake's head. [row, column]
# hcoor: Coordinates of the snake's last bit of tail. [row, column]
def step(current, hcoor, tcoor, direction, length):
	global theme, rows, columns

	result = current
	# Override body (previous head)
	result[hcoor[0], hcoor[1]] = theme[1]
	# Remove old tail
	result[tcoor[0], tcoor[1]] = theme[0]

	# Place head
	if direction[-1] == "up":
		result[hcoor[0] - 1, hcoor[1]] = theme[2]
		hcoor[0] -= 1
	elif direction[-1] == "down":
		result[hcoor[0] + 1, hcoor[1]] = theme[2]
		hcoor[0] += 1
	elif direction[-1] == "right":
		result[hcoor[0], hcoor[1] + 1] = theme[2]
		hcoor[1] += 1
	elif direction[-1] == "left":
		result[hcoor[0], hcoor[1] - 1] = theme[2]
		hcoor[1] -= 1
	else:
		return current

	tdir = direction.pop(0)

	if tdir == "up":
		tcoor[0] -= 1
	elif tdir == "down":
		tcoor[0] += 1
	elif tdir == "right":
		tcoor[1] += 1
	elif tdir == "left":
		tcoor[1] -= 1
	else:
		return current

	return result

with FullscreenWindow(sys.stdout) as w:
	with input.Input(sys.stdin) as input_generator:
		rows, columns = w.t.height, w.t.width
		speed = sspeed
		stage = last = time()
		hcoor = [rows / 2 - 3, columns / 2]
		tcoor = [rows / 2, columns / 2]
		direction = "up"
		length = 3
		moves = []
		for _ in range(length):
			moves.append(direction)

		screen = FSArray(rows, columns)

		while True:

			if time() - stage >= accevery:
				stage = time()
				#speed += acc

			if time() - last >= 1.0 / speed:
				print time() - last
				last = time()

				# TODO: Manage the length change
				moves.append(direction)

				screen = step(screen, hcoor, tcoor, moves, length)

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
