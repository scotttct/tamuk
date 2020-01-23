# Task 1
# WHILE TRUE
# [ ] Program: Get a name forever ...or until done
# create variable, familar_name, and assign it an empty string ("")
# use while True:
# ask for user input for familar_name (common name friends/family use)
# keep asking until given a non-blank/non-space alphabetical name is received (Hint: Boolean string test)
# break loop and print a greeting using familar_name
# [ ] create Get Name program

# familar_name = ""

# while True:

#     familiar_name = input ("Enter your commonly used name,something your friends or family use: ")


#     if familiar_name.isalpha():

#       print ("Hi",familiar_name.capitalize() + "!", "I am glad you are alive and well!")

#       break


#     elif not familiar_name.isalpha:
#       print("keep going\n")
#     else:
#         break

#################################33
#2nd Try

def familiar_name():

    while True:

        name_input = input("What's a common name your friends and family use?")

        if name_input.isalpha():
            break

        else:
            print()
    
    print()
    print("Hey " + name_input.capitalize())
    
familiar_name()