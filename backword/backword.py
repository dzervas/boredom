from multiprocessing.dummy import Pool as ThreadPool

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
def generate(base, nolist = []):
	global wordlist, limit

	for word in wordlist:
		now = base + " " + word
		wordcount = now.count(" ")

		if wordcount == 1:
			nolist.append(base)

		if word in nolist:
			continue

		if check(now):
			print now

		if wordcount < limit:
			nolist.append(word)
			generate(now, nolist)
			nolist.pop()

wordlist = []
limit = 2
threads = 5

with open("wordlist.txt", "r") as f:
	for line in f:
		wordlist.append(line.strip())

pool = ThreadPool(threads)
pool.map(generate, wordlist)
