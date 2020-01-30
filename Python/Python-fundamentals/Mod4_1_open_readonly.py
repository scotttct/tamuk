# cities_file = open('cities.txt', 'r')
# print(cities_file)

# for cities in cities_file:
#     print(cities)

#######################################
# TASK 2
# REMOVE NEWLINE CHARACTERS FROM CITIES LISTS CREATED USING .READLINES()
# This task assumes that cites.txt has been imported in Task 1 above
# In task 1, the cities were printed with a blank line between each city - this task removes the blank lines
# [ ] re-open file and read file as a list of strings
# [ ] open cities.txt as cities_file and read the file as a list: cities_lines
# import https: // raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2.txt as poem2.txt
# cities_file = open('cities.txt', 'r')
# cities_lines = cities_file.readlines()
# print(cities_lines)


# [ ] remove the last character, "\n", of each cities_lines list item
# count = 0
# for line in cities_lines:
#     cities_lines[count] = line[:-1]
#     count += 1

# print(cities_lines)
# # [ ] print each list item
# for line in cities_lines:
#     print(line)
# for city in cities_lines:
#     if city[0:1] >= "D":
#         print(city[:-1], "starts with 'D' or greater")
#     else:
#         print(city[:-1], "doesn't start with 'D' or greater")

# print(cities_file)
# cities_file.close()
##############################################################
# TASK 4
# READLINES() POEM2
# write each item in its own cell

# open poem2.txt as poem2_file in read mode
# create a list of strings, called poem2_lines, from each line of poem2_text(use .readlines())
# remove the newline character for each list item in poem2_lines
# print the poem2 lines in reverse order
# [ ] import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2.txt as poem2.txt


# [ ] open poem2.txt as poem2_text in read mode
poem2 = open('poem2.txt', 'r')




# [ ] create a list of strings, called poem2_lines, from each line of poem2_text
poem2_lines = poem2.readlines()


# [ ] remove the newline character for each list item in poem2_lines
count = 0
for line in poem2_lines:
    poem2_lines[count] = line[:-1]
    count += 1

# [ ] print the poem2 lines in reverse order
poem2_lines.reverse()
print(poem2_lines)

poem2.close


