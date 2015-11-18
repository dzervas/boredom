import random

sentences = [
    "No",
    "Yes",
    "Maybe"
]

i = 0
while i < 3:
    print sentences[random.randint(0, 2)]
    i += 1
