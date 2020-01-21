#Task 4
#FIX THE ERRORS
# Review, run, fix ***in the elseif statement had to have a colon :
student_name = input("enter name: ").capitalize()
if student_name.startswith("F"):
    print(student_name,"Congratulations, names starting with 'F' get to go first today!")
elif student_name.startswith("G"):
    print(student_name,"Congratulations, names starting with 'G' get to go second today!")
else:
    print(student_name, "please wait for students with names staring with 'F' and 'G' to go first today.")
