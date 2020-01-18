#Write a program that takes 5 numbers as an input, puts them into a list, then modifies that list so each element is replaced with its square. (2 becomes 4, 5 becomes 25) and such.
#(put it on your github, in the / homework folder)

#taken from stackoverflow:  https://stackoverflow.com/questions/56920836/how-to-replace-every-element-in-a-given-list-to-its-square-and-not-create-a-new
def square_list(list_1):
    for i in range(len(list_1)):
        list_1[i] = list_1[i]**2


my_list = [1, 2, 3, 4, 5]
square_list(my_list)
print(my_list)
