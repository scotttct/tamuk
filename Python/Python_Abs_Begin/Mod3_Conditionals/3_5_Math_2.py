#Task 2
#PROGRAM: MULTIPLYING CALCULATOR FUNCTION
#define function multiply(), and within the function:
#gets user input() of 2 strings made of whole numbers
# #cast the input to int()

#multiply the integers and return the equation winth result as a str()

#return example
#9 * 13 = 117
# [ ] create and test multiply() function

num1 = input("Enter a whole number: ")
num2 = input("Enter a whole number: ")

def multiply2(x, y):
    return x * y

print(num1 + " * " + num2 + " =", multiply2(int(num1),int(num2)))


