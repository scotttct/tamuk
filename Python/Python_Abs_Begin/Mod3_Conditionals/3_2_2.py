# Task 2 continued...
# create a functions using startswith('w')
# w_start_test() tests if starts with "w"
# function should have a parameter for test_string and print the test result
# test_string_1 = "welcome"
# test_string_2 = "I have $3"
# test_string_3 = "With a function it's efficient to repeat code"
# [ ] create a function w_start_test() use if & else to test with startswith('w')

# [ ] Test the 3 string variables provided by calling w_start_test()
def w_start_test(test_string_1, test_string_2, test_string_3):

        if test_string_1.startswith("w"):
                print ("the text starts with w")
        else:
                print ("the text does not starts with w")
               
        if test_string_2.startswith("w"):
                print ("the text starts with w")
        else:
                print ("the text does not starts with w")

        if test_string_3.startswith("w"):
                print ("the text starts with w")
        else:
                print ("the text does not starts with w")

# [ ] Test the 3 string variables provided by calling w_start_test()

w_start_test('welcome', 'I have $3', "With a function it's efficient to repeat code" )

