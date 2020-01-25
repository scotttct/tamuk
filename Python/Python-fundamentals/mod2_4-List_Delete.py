#Tasks for Delete, Pop and Empty list to false


# TASK 1
# DEL STATEMENT
# [ ] print ft_bones list
# [ ] delete "cuboid" from ft_bones
# [ ] reprint list
# ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
#             "intermediate cuneiform", "medial cuneiform"]
# print("List before: ", ft_bones)
# del ft_bones[2]
# print("List after: ", ft_bones)
#######################################
#Task 2
# TASK 2
# MULTIPLE DEL STATEMENTS
# [ ] print ft_bones list
# [ ] delete "cuboid" from ft_bones
# [ ] delete "navicular" from list
# [ ] reprint list
# [ ] check for deletion of "cuboid" and "navicular"
# ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
#             "intermediate cuneiform", "medial cuneiform"]
# print("Before: ",ft_bones)

# del ft_bones[2]
# del ft_bones[3]

# print("After: ", ft_bones)
##############################################
# TASK 3
# POP()#####
# [ ] pop() and print the first and last items from the ft_bones list
# ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
#             "intermediate cuneiform", "medial cuneiform"]
# print("before: ", ft_bones)
# first = ft_bones.pop(0)
# last = ft_bones.pop(-1)

# print("After: ", ft_bones)


# [ ] print the remaining list
####################################################
# EMPTY LIST TO FALSE

# TASK 4 PT 1
# Cash Register Input
# create a empty list purchase_amounts
# populate the list with user input for the price of items
# continue adding to list with while until "done" is entered
# can use while True: with break
# print purchase_amounts
# continue to pt 2
#[ ] complete the Register Input task above

# purchase_amounts = []
# user_input = input("Input a price for the item: ")

# purchase_amounts = purchase_amounts.extend(user_input)
# print(purchase_amounts)

# purchase_amounts = []
# price = ''

# while True:
#     price = input('Enter the price: ')
#     if price.lower() != 'done':
#         purchase_amounts.append(price)
#     else:
#         break
    
# print("Here are the mounts of each sale = ", purchase_amounts) # Not Done: need to break each one of the sale items into its own line print a double line then subtotals...

# # Cash Register Total¶
# # create a subtotal variable = 0 create a while loop that runs while purchase_amount (is not empty)
# # inside the loop
# # pop() the last list value cast as a float type
# # add the float value to a subtotal variable
# # after exiting the loop print subtotal

# # be sure to populate purchase_amounts by running pt 1 above

# # In [3]:
# # [ ] complete the Register Total task above

# subtotal = 0

# while purchase_amounts:
#     subtotal += float(purchase_amounts.pop()) # Here we remove the input 'done' from the list before printing

# print("Your Subtotal for today is = ", subtotal)
##############################################################
# TASK 5
# .REMOVE()
# [ ] remove one "Poodle" from the list: dogs , or print "no Poodle found"
# [ ] print list before and after
dogs = ["Lab", "Pug", "Poodle", "Poodle", "Pug", "Poodle"]
print("Before: ", dogs)
if "Poodle" in dogs:
    dogs.remove("Poodle")
    print("After: ", dogs)
else:
    print("no Poodle found")
# print(dogs)
