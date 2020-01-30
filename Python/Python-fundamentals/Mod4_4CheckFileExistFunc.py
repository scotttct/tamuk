import os
from os import path
#Function for checking OS 
def main():
    # Print the name of the OS
    print(os.name.upper())
#Check for item existence and type
print("Item exists:" + str(path.exists("guru99.txt")))
print("Item is a file: " + str(path.isfile("guru99.txt")))
print("Item is a directory: " + str(path.isdir("guru99.txt")))

if __name__ == "__main__":
    #Call the Function to check the OS
    main()

file_exists = path.exists("guru99.txt")
if file_exists:
    file = open('guru.txt', 'r+')
    #Do something here
else:
    file = open('guru.txt', 'w+')
    #Do something here



