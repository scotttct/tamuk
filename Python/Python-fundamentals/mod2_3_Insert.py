# TASK 1
# REPLACE ITEMS IN A LIST
# create a list, three_num, containing 3 single digit integers
# print three_num
# check if index 0 value is < 5
# if < 5 , replace index 0 with a string: "small"
# else, replace index 0 with a string: "large"
# print three_num
# [ ] complete "replace items in a list" task
# three_num = [1, 2, 3]
# print(three_num)
# if three_num[0] < 5:
#     three_num[0] = "small"
#     print(three_num)
# else:
#     three_num[0] = "large"
#     print(three_num)

######################################################################
# def str_replace(int_list, index):
#     if index >= len(int_list):
#         return int_list;
#     first = int_list[index]
#     int_list[index] = "small" if first < 5 else "large"
#     return int_list

# print(str_replace([1,2,6,7], 1))
# print(str_replace([1,2,6,7], 2))
#######################################################################
# TASK 2
# MODIFY ITEMS IN A LIST
# create a list, three_words, containing 3 different capitalized word stings
# print three_words
# modify the first item in three_words to uppercase
# modify the third item to swapcase
# print three_words
# [ ] complete coding task described above

# three_words = ["One", "Two", "Three"]
# print(three_words)
# three_words[0] = three_words[0].upper()
# three_words[2] = three_words[2].swapcase()
# print(three_words)
##########################################################
# Task 3

# [ ] insert a name from user input into the party_list in the second position (index 1)
party_list = ["Joana", "Alton", "Tobias"]
user_input = input("Enter a name to invite to a party: ")
print("Your party list before the insert: ", party_list)
party_list.insert(1, user_input)
print("Your party list after insert: ", party_list)
# [ ] print the updated list
##########################################################################
# TASK 4
# FIX THE ERROR
# [ ] Fix the Error
# tree_list = ["oak"]
# print("tree_list before =", tree_list)
# tree_list.insert(1,"pine")
# print("tree_list after  =", tree_list)