# TASK 3
# .SORT() & SORTED()
# [ ] print cites from visited_cities list in alphbetical order using .sort()
# [ ] only print cities that names start "Q" or earlier
# visited_cities = ["New York", "Shanghai", "Munich", "Toyko",
#                   "Dubai", "Mexico City", "São Paulo", "Hyderabad"]

# visited_cities.sort()
# print(visited_cities)
##########################################################
#2nd part of the task...
visited_cities = ["New York", "Shanghai", "Munich", "Toyko",
                  "Dubai", "Mexico City", "São Paulo", "Hyderabad", "Qatar"]
# visited_cities.sort()
# new_cities = []
# for cities in visited_cities:
#    if cities[0] <= "Q":
#        new_cities.append(cities)
# print(new_cities)
###############################################################
# [ ] make a sorted copy (sorted_cities) of visited_cities list

# sorted_cities = sorted(visited_cities)
# # print(visited_cities, "/n")
# # print(sorted_cities)
# ################################################################
# # [ ] remove city names 5 characters or less from sorted_cities
# sort_cities = sorted(visited_cities)
# for city in sort_cities:
#     if len(city) <= 5:
#         sort_cities.remove(city)
#     else:
#         pass
# print('visited_cities =', visited_cities, '\n\n', 'Cities with 5 or less characters: ',sort_cities)
# [ ] print visitied cites and sorted cities
# visited_cities = ["New York", "Shanghai", "Munich", "Toyko",
#                   "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
###############################################################################
# TASK 4
# PROGRAM: MERGE & SORT ANIMALS
# Create a program that

# takes user to build a list: add_animals
# merges add_animals with existing list: animals
# provides a sorted list to view in alpha or reverse alpha order
# step 1 get user input to build add_animals list

# [ ] build a list (add_animals) using a while loop, stop adding when an empty string is entered
###My First Go...
# add_animals = []

# animal = input("Add Animals to list: ")
# if animal is not "":
#     add_animals.append(animal)
# else: 
#     break   
# step 2 Merge the lists: add_animals into animals
add_animals = []
while True:
    animals = input('Enter a animal name: ')
    if animals.isalpha():
        add_animals.append(animals)
    elif animals == '':
        break
    else:
        print('Only animal name please!')
print(add_animals)
# [ ] extend the lists into animals, then sort
animals = ["Chimpanzee", "Panther", "Wolf", "Armadillo"]
add_animals.extend(animals)
print('unsorted:', add_animals)
add_animals.sort()
print('sorted:', add_animals)

# step 3 Allow animals list to be viewed alpha or reverse alpha order
animal_list = sorted(add_animals)
print("Sorted Animals: ", animal_list)

add_animals.reverse()
print("Reversed animal list: ", add_animals)
# [ ] get input if list should be viewed alpha or reverse alpha and display list
list_direction = input("Type in 'S' for Sorted list and 'R' for Reversed List: ")

if list_direction == "S":
    print("Sorted List:", animal_list)
elif list_direction == "R":
    print("Reverse Sorted List: ", add_animals)
else:
    print("Sorry this was and incorrect response and the program will stop!")
    pass


