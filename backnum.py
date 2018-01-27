import math

print("Give me a number: ")
number = input()

def check(a, b):
    if a > 9:
        check(a / math.pow(10, int(math.log(a, 10))), a % math.pow(10, int(math.log(a, 10))))
    if b > 9:
        check(b / math.pow(10, int(math.log(b, 10))), b % math.pow(10, int(math.log(b, 10))))
