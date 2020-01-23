# Program: Animal Names
# Use while to get the user input, animal_name, of 4 animals
# use a counter, num_animals, in the while loop condition
# append the names to a string variable, all_animals
# User can exit early by typing "exit" (check if animal_name is "exit" and break)
# when the loop finishes, print the names of all_animals
# -bonus: print "no animals" if animal_name is empty after exiting the loop


# [ ] Create the Animal Names program, run tests

#########My Try
# # review and run GREET COUNT
# num_animals = 0

# # loop while count is greater than 0
# while num_animals >= 4:
#     animal_name = input("Enter an animals name: ")

#     print(animal_name + " " + num_animals)
#     num_animals += 1
# else:
#     print("No more animals names please!")

##########from: https://notebooks.azure.com/taiku16/projects/DEV236x/html/MOD04_1-7.2_Intro_Python.ipynb
num_animals = 4
all_animals = ""

while num_animals > 0:
    animal_name = input("Enter an animal: ").lower()
    if animal_name == "exit":
        break
    else:
        all_animals = all_animals + animal_name.capitalize() + " "
    num_animals -= 1

# print(all_animals)    
if all_animals.istitle():
    print(all_animals)
else:
    print('"no animals"')