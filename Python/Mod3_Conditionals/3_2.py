# create evaluations for .islower()
# print output describing if each of the 2 strings is all lower or not
# test_string_1 = "welcome"
# test_string_2 = "I have $3"
# # [ ] use if, else to test for islower() for the 2 strings

test_string_1 = "welcome"
test_string_2 = "I have $3"

if test_string_1.islower(): #and test_string_2.islower():
    print("The first string was written in lower case.")
else:
    print("The first string was not in lower case.")

if test_string_2.islower():
    print("The second string was written in lower case.")
else:
    print("The second string was not written in lower case.")
