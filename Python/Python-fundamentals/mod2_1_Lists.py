# TASK 1
# CREATE LISTS
# [ ] create team_names list and populate with 3-5 team name strings

# [ ] print the list


# [ ] Create a list mix_list with numbers and strings with 4-6 items

# [ ] print the list


# team_names = ["Celtics", "Lakers", "Suns", "Bulls", "Rapters", "Knicks", "Heat", "Hornets", "Magic", "Clippers"]
# print("Team Names:", type(team_names))

# print(team_names)

# mix_list = [1, 2, 3, "4", "5"]

# print("mix_list: ", type(mix_list))
# print(mix_list)

###################################################################

# TASK 2
# [ ] Create a list, streets, that lists the name of 5 street name strings

# [ ] print a message that there is "No Parking" on index 0 or index 4 streets
# streets = ["Comstock Ave", "Ivory Lane", "Baldwin Lane", "Main Street", "Timber Trail"]

# print("There is no Parking on", streets[0:4])

# [ ] Create a list, num_2_add, made of 5 different numbers between 0 - 25

# [ ] print the sum of the numbers
# 
###################################################################

# TASK 3
# FIX THE ERRORS
# [ ] Review & Run, but ***Do Not Edit*** this code cell
# [ ] Fix the error by only editing and running the block below
# pay_checks = [100, 1000, 10000, 100000]
# print(" Total of checks 3 & 4 = $", pay_checks[2] + pay_checks[3])

# [ ] Fix the error above by creating and running code in this cell
#####################################################################################
######################################################################################
#Appending Lists
# TASK 1
# .APPEND()
# Currency Values
# [ ] create a list of 3 or more currency denomination values, cur_values
# cur_values, contains values of coins and paper bills (.01, .05, etc.)
# cur_values = [.01, .05, .10, .25, .50, 1.00]


# # [ ] print the list
# print("list of coin values in USA: ", cur_values)

# # [ ] append an item to the list and print the list
# cur_values.append(10.00)

# print("currency values for USA are: ", cur_values)
# Currency Names
# [ ] create a list of 3 or more currency denomination NAMES, cur_names
# # cur_names contains the NAMES of coins and paper bills (penny, etc.)
# cur_names = ["penny", "nichole", "dime "]
# # # [ ] print the list
# # print(cur_names)

# # # [ ] append an item to the list and print the list
# cur_names.append("dollar")
# # print(cur_names)
# ##################################################################

# #Task 2
# #Append addition cur_names through user input
# user_input = input("Add to the list of USA Currency names: ")

# cur_names.append(user_input)

# print(cur_names)

###############################################################
# TASK 3
# WHILE LOOP .APPEND()
# define an empty list: bday_survey
# get user input, bday, asking for the day of the month they were born (1-31) or "q" to finish
# using a while loop (while user not entering "quit")
# append the bday input to the bday_survey list
# get user input, bday, asking for the day of the month they were born (1-31) or "q" to finish
# print bday_survey list
# [ ] complete the Birthday Survey task above
# bday_survey = []

# bday = input("Please enter the month your were born (1-31) or 'q' to finish: ")

# while bday != "q":
#   bday_survey.append(bday)
#   bday = input("Please enter the month your were born (1-31) or 'q' to finish: ")
# print(bday_survey)
#######################################################################

# TASK 4
# FIX THE ERROR
# [ ] Fix the Error
three_numbers = [1, 1, 2]
print("an item in the list is: ", three_numbers[2])
