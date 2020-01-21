# Task 3
# PROJECT: IMPROVED MULTIPLYING CALCULATOR FUNCTION
# putting together conditionals, input casting and math
# update the multiply() function to multiply or divide
# single parameter is operator with arguments of * or / operator
# default operator is "*" (multiply)
# return the result of multiplication or division
# if operator other than "*" or "/" then return "Invalid Operator"
# [ ] create improved multiply() function and test with /, no argument, and an invalid operator ($)

def multiply(operator):

    x = float(input('Enter number 1: '))

    y = float(input('Enter number 2: '))

    if operator == "*":

        return x * y

    elif operator == "/":
        return x / y

    else:
        return "invalid operator"

print(multiply(input("Enter '/' or '*': ")))

