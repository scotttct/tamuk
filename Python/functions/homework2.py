#A guessing game in Python: from https://www.w3resource.com/python-exercises/python-conditional-exercise-3.php
#Modified to 1-100
import random
target_num, guess_num = random.randint(1, 100), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 100 until you get it right : '))
print('Well guessed!')