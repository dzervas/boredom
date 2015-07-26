import numpy

# Check if the sentence is the same backwards
def check(sentence):
#	print sentence
	nospace = sentence.replace(" ", "")
	i = 0

	while i < len(nospace):
		if nospace[i] != nospace[len(nospace) - i - 1]:
			return False
		i += 1

	return True

# Recursive function that generates sentences of given length
def generate(base):
	global wordlist, nolist, limit
	for word in wordlist:
		if word in nolist:
			continue

		now = base + " " + word
		if check(now):
			print now

		if now.count(" ") < limit:
			nolist.append(word)
			generate(now)
			nolist.pop()

wordlist = []
nolist = []
limit = 1

with open("wordlist.txt", "r") as f:
	for line in f:
		wordlist.append(line.strip())

	# We do not want single word sentences, so do the first word loop outside
	for word in wordlist:
		nolist[0] = word
		generate(word)
