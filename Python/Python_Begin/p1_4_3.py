import sys

print("Hel" + "lo" == "Hello")
print()

msg = 'say "Hello"'
print(msg)
print()

answer = 21
new_msg = input('What is 8 + 13? : ')



if int(new_msg) == answer:
    print("That is the correct answer")
else:
    print("Try again")

# Define and use tf_quiz() function
# tf_quiz() has 2 parameters which are both string arguments
# question: a string containg a T/F question like "Should save your notebook after edit?(T/F): "
# correct_ans: a string indicating the correct answer, either "T" or "F"
# tf_quiz() returns a string: "correct" or "incorrect"
# Test tf_quiz(): create a T/F question (or several!) to call tf_quiz()