# TASK 1
# Iterate through Lists using in
# [ ] create a list of 4 to 6 strings: birds
# print each bird in the list


# [ ]  create a list of 7 integers: player_points
# [ ] print double the points for each point value


# [ ] create long_string by concatenating the items in the "birds" list previously created
# print long_string - make sure to put a space betweeen the bird names

# birds = ["robin", "crow", "hawk", "owl", "eagle"]

# for bird in birds:
#     print(bird)

# player_points = [1, 29, 2, 23, 4, 18, 22, 22, 28]

# for points in player_points:
#     print(points)

# birds = ["robin", "crow", "hawk", "owl", "eagle"]

# long_string = ""
# for bird in birds:
#     long_string += " " + bird

# print(long_string)
################################################################
# TASK 2
# SORT AND FILTER
# [ ] Using cities from the example above iterate throught the list using "for"/"in"
# [ ] Print only cities starting with "m"
# cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
# for city in cities:
#     if city[0].lower() == "e":
#         print(city)

# [ ] Using cities, from the example in previous page. iterate through the list using "for"/"in"
# cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
# [ ] sort into lists with "A" in the city name and without "A" in the name: a_city & no_a_city

# a_city = []
# no_a_city = []
# for city in cities:
#     if "a" in city.lower():
#         a_city.append(city)
#     else:
#         no_a_city.append(city)

# print(cities)
# print(a_city)
# print(no_a_city)
################################################################################

# TASK 3
# PROGRAM: PAINT STOCK
# check a list for a paint color request and print status of color "found"/"not found"

# create list, paint_colors, with 5+ colors
# get user input of string:color_request
# iterate through each color in paint_colors to check for a match with color_request
# [ ] complete paint stock

# paint_colors = ["red", "green", "blue", "purple", "pink"]



# def color_search(color_request, paint_colors = ["red", "green", "blue", "purple", "pink"] ):
#     for paint in paint_colors:
#         if paint.lower() ==color_request.lower():
#             return True
#         else:
#             # go to the next item
#             pass
#     # no more items in list
#     return False
    
# paint_colors = ["red", "green", "blue", "purple", "pink"]
# color_request = input("Check to see if you color is in our inventory: ")

# print(color_request.title(), "is in our inventory", color_search(color_request))

# search the list visited_cities using 2nd argument
## print(color_requet, "is in our inventory", color_search(color_requet, paint_colors))

#####################################################################################



# TASK 4
# PROGRAM: FOOT BONES QUIZ
# Create a function that will iterate through foot_bones looking for a match of a string argument

# Call the function 2 times with the name of a footbone
# print immediate feedback for each answer (correct - incorrect)
# print the total # of foot_bones identified
# The program will use the foot_bones list:

# foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform",
#              "intermediate cuneiform", "medial cuneiform"]
# Bonus: remove correct response item from list if correct so user cannot answer same item twice
# foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform","intermediate cuneiform", "medial cuneiform"]

# def bone_sorter(bone_in):
#     bone_num = 0
#     for bone in foot_bones:
#         if bone_in.lower() == bone:
#             print("Your bone,", bone_in +",","is in the list of foot bones.\n")
#             bone_num += 1
            
#         else:
#             bone_num += 1
#     print("The number of bones in the list is", bone_num, "\n")

# bone_in = input("Type in a foot bone: ")
# bone_sorter(bone_in)
# [ ] Complete Foot Bones Quiz
# foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform",
#             "intermediate cuneiform", "medial cuneiform"]

# [ ] bonus version
#Copied from: https://notebooks.azure.com/ericf/projects/Dev274x/html/Mod3_2-3.1_intro_Python.ipynb
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", "intermediate cuneiform", "medial cuneiform"]

def bone_search(search_item):
    for i in foot_bones:
        if i == search_item:
            nd = "correct"
            return nd
        else:
            nc = "incorrect"
            pass
    return nc


search = input("Guess a Foot Bone? ")

var = bone_search(search)

num = 0

if var == "correct":
    num += 1
    print("Your guess,",search, "which was", bone_search(search), "\n")
    pass
else:
    num += 0
    search = input("Your guess was incorrect, sorry!")
    pass

print(num, "foot bone(s) identified \n")

# if var == "correct":
    # num += 1

# print("Congrats! you have selected",search, "which is", bone_search(search), "\n")

