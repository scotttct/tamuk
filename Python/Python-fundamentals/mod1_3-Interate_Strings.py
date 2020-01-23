# TASK 1
# ITERATE A STRING
# one character at a time
# [ ] Get user input for first_name
# [ ] iterate through letters in first_name
#    - print each letter on a new line

# username = input("Enter a Username: (one word all alph) ")

# for name in username:
#     print(name)
######################################
# TASK 2
# PROGRAM: CAPITALIZE-IO
# get user input for first_name
# create an empty string variable: new_name
# iterate through letters in first_name
# add each letter in new_name
# capitalize if letter is an "i" or "o" * (hint: if, elif, else)
# print new_name

# first_name = input("Please enter your first name: ")
# new_name = ""

# for ltr in first_name:
#     if ltr.lower() == "i":
#         new_name += ltr.upper()
#     elif ltr.lower() == "o":
#         new_name += ltr.upper()
#     else:
#         new_name += ltr
# print(first_name, "to", new_name)

#Used Toni as first name worked

##############################################
# TASK 3
# String slicing and iteration
# [ ] create & print a variable, other_word, made of every other letter in long_word
# long_word = "juxtaposition"

# for other_word in long_word[::2]:
#     print(other_word)
###################
# 3.2

# Mirror Color
# [ ] get user input, fav_color
# [ ] print fav_color backwards + fav_color
# example: "Red" prints "deRRed"

# fav_color = input("Enter you favorite color: ")

# for clr in fav_color[::-1]:
#     print(clr + fav_color)

#My first try above printed the color with each letter on a new line + the fav_color
# dred
# ered
# rred
#2nd Try...Worked..I see what they did there, tricky...testing our resolve and problem solving skills I see...:()
# fav_color = input("Enter you favorite color: ")
# new_color = fav_color[::-1]

# print(new_color + fav_color)

# for fav_color = green, printed neerggreen
fav_color = input("Enter you favorite color: ")
new_color = ""

for letter in fav_color[::-1]:
    new_color += letter
print(new_color + fav_color)

#3rd try also printer neerggreen but with the correct iteration, both way worked however....:)
