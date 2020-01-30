# TASK 1
# RANGE(STOP)
# [ ] for x = 6, use range(x) to print the numbers 1 through 6
#x = 6
# # for count in range(x):
# #     print(count)
# digits =list(range(x))
# print("digits =", digits, "\n")

# for count in digits:
#     print(count)
#####################################################
# [ ] using range(x) multiply the numbers 1 through 7
# 1x2x3x4x5x6x7 = 5040
#str(number +1), "x", str(number +2), "x", str(number + 3), "x", str(number + 4)

# multiplication = 1

# for number in range(1,8):
#     multiplication *= number
# digits = list(range(1,8))

# print("Multiply these tumber in sequence: ", digits, "=", multiplication)
###############################################################

# spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

# item_index = 0

# for item in spell_list:
#     if item != "Annual":
#         item_index += 1
#     else:
#         break

# for item_num in range(item_index, int(len(spell_list))):
#     print(spell_list[item_num])
###################################################
# TASK 2
# RANGE(START,STOP)
# [ ] using range(start,stop), .append() the numbers 5 to 15 to the list: five_fifteen
# [ ] print list five_fifteen

# five_fiften = []

# for num in range(5, 15):
#     five_fiften.append(num)
#     print("Stepping through Numbers in Range 5 to 15 are: ", five_fiften)
########################################################################
# [ ] using range(start,stop) - print the 3rd, 4th and 5th words in spell_list
# output should include "February", "November", "Annual"
# spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
# for item_num in range(2, 5):
    # print(spell_list[item_num])
#####################################################
# spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

# item_index = 0

# for item in spell_list:
#     if item != "Annual":
#         item_index += 1
#     else:
#         break

# for item_num in range(item_index, int(len(spell_list))):
#     print(spell_list[item_num])
############################################################
# TASK 3
# RANGE(START,STOP,STEP)
# [ ] print numbers 10 to 20 by 2's using range
# for count in range(10,20,2):
#   print(count)
###########################################################
# [ ] print numbers 20 to 10 using range (need to countdown)
# Hint: start at 20
# for count in range(20, 9, -1):
#   print(count)
#########################################################
# [ ] print first and every third word in spell_list
# spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
# for index in range(0,len(spell_list),3):
#     print(spell_list[index])
##########################################################

# TASK 4
# Program: List of letters
# Input a word string (word)
# find the string length of word
# use range() to iterate through each letter in word (can use to range loops)
# Save odd and even letters from the word as lists
# odd_letters: starting at index 0,2,...
# even_letters: starting at index 1,3,...
# print odd and even lists
# [ ] complete List of letters program- test with the word "complexity"

# my_word = input("Enter a word: ")

# odd_letters = []
# even_letters = []

# for letter in range(len(my_word)):
#     if letter % 2 == 0:
#         even_letters.append(my_word[letter])
#     else:
#         odd_letters.append(my_word[letter])

# print(even_letters)
# print(odd_letters)
##############################################################
# TASK 5: FIX THE ERROR
# [ ] fix the error printing odd numbers 1 - 9
for num in range(0,10,2):
    print(num)
