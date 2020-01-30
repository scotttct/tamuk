# TASK 1
# combine lists
# [ ] extend the list common_birds with list birds_seen which you must create
# common_birds = ["chicken", "blue jay", "crow", "pigeon"]
# birds_seen = ["hawl", "jay", "eagle", "falcon"]

# common_birds.extend(birds_seen)
# print(common_birds)
# [ ] Create 2 lists zero_nine and ten_onehundred that contain 1-9, and 10 - 100 by 10's.
# [ ] use list addition to concatenate the lists into all_num and print

##My First Go
# zero_nine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ten_onehundred = range(10, 100, 10)

# all_num = zero_nine + ten_onehundred
# print("All Numbers 1 to 9 and 10 to 100 by 10")
# for num in all_num:
#     print(all_num)

##Second Try I will cast zero_nine and ten_onehundred from emply list to range
# zero_nine = []
# ten_onehundred = []

# for number in range(10):
#     zero_nine.append(number)
    
# for number in range(10, 101, 10):
#     ten_onehundred.append(number)
    
# all_num = zero_nine + ten_onehundred

# print(all_num)
####################################################
# TASK 2
# .REVERSE()
# [ ] create and  print a list of multiples of 5 from 5 to 100
# { ] reverse the list and print


# [ ] Create two lists: fours & more_fours containing multiples of four from 4 to 44
# [ ] combine and print so that the output is mirrored [44, 40,...8, 4, 4, 8, ...40, 44]
##--My Firt Try--Gave me a list of lists that increased by 5 to 100 and back again, then in reverse
# num_range = []
# num = range(5, 100, 5)
# for all_num in num:
#     num_range.append(all_num)
#     print("regular list",num_range, "\n")
#     num_range.reverse()
#     print("reverse list",num_range, "\n")

#---Output----
# regular list [5] 

# reverse list [5]

# regular list [5, 10]

# reverse list [10, 5] 

# regular list [10, 5, 15]

# reverse list [15, 5, 10]

# regular list [15, 5, 10, 20]

# reverse list [20, 10, 5, 15]

# regular list [20, 10, 5, 15, 25]

# reverse list [25, 15, 5, 10, 20]

# regular list [25, 15, 5, 10, 20, 30]

# reverse list [30, 20, 10, 5, 15, 25]

# regular list [30, 20, 10, 5, 15, 25, 35]

# reverse list [35, 25, 15, 5, 10, 20, 30]

# regular list [35, 25, 15, 5, 10, 20, 30, 40]

# reverse list [40, 30, 20, 10, 5, 15, 25, 35]

# regular list [40, 30, 20, 10, 5, 15, 25, 35, 45]

# reverse list [45, 35, 25, 15, 5, 10, 20, 30, 40]

# regular list [45, 35, 25, 15, 5, 10, 20, 30, 40, 50]

# reverse list [50, 40, 30, 20, 10, 5, 15, 25, 35, 45]

# regular list [50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55]

# reverse list [55, 45, 35, 25, 15, 5, 10, 20, 30, 40, 50]

# regular list [55, 45, 35, 25, 15, 5, 10, 20, 30, 40, 50, 60]

# reverse list [60, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55]

# regular list [60, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65]

# reverse list [65, 55, 45, 35, 25, 15, 5, 10, 20, 30, 40, 50, 60]

# regular list [65, 55, 45, 35, 25, 15, 5, 10, 20, 30, 40, 50, 60, 70]

# reverse list [70, 60, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65]

# regular list [70, 60, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75]

# reverse list [75, 65, 55, 45, 35, 25, 15, 5, 10, 20, 30, 40, 50, 60, 70] 

# regular list [75, 65, 55, 45, 35, 25, 15, 5, 10, 20, 30, 40, 50, 60, 70, 80]

# reverse list [80, 70, 60, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75]

# regular list [80, 70, 60, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85]

# reverse list [85, 75, 65, 55, 45, 35, 25, 15, 5, 10, 20, 30, 40, 50, 60, 70, 80]

# regular list [85, 75, 65, 55, 45, 35, 25, 15, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# reverse list [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85]

# regular list [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]

# reverse list [95, 85, 75, 65, 55, 45, 35, 25, 15, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90]

##############################################################

#--Second Try Worked, taken from: https://notebooks.azure.com/psp82/projects/Dev274x/html/Mod3_2-3.3_intro_Python.ipynb, and then modified
# num_range = []

# for num in range(0, 101):
#     if num * 5 < 101:
#         num_range.append(num * 5)
#     else:
#         break
    
# num_range.reverse()    
# print("Countdown by 10 from 100 to 5: ", num_range)
###############################################################
# [ ] Create two lists: fours & more_fours containing multiples of four from 4 to 44
# [ ] combine and print so that the output is mirrored [44, 40,...8, 4, 4, 8, ...40, 44]
#---My First Try only produced: None...Not good
# fours = []
# fours_reverse = []
# for number in range(1, 45):
#     if number * 4 < 45:
#         fours.append(number * 4)
        
#     else:
#         break
#     fours_revere = fours.reverse()

#     print(fours.append(fours_revere))
######## 2nd try worked taken from: https://notebooks.azure.com/twsteneo/projects/Dev274x/html/Mod3_2-3.3_intro_Python.ipynb
######## Simplier solution that I had thought...I like it!
# [ ] Create two lists: fours & more_fours containing multiples of four from 4 to 44
# more_fours = list(range(4,45,4))
# rev_fours = list(range(4,45,4))
# rev_fours.reverse()
# # [ ] combine and print so that the output is mirrored [44, 40,...8, 4, 4, 8, ...40, 44]
# print(rev_fours +more_fours)
###################################################
