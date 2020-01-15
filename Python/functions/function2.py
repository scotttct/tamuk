# Start with the below example code
# add a parameter period_3
# update function code to add period_3 to the schedule
# call student_schedule() with an additional argument such as 'science'
# print the schedule
# [ ] add a 3rd period parameter to make_schedule
# [ ] Optional - print a schedule for 6 classes (Tip: perhaps let the function make this easy)


def make_schedule(period1, period2, period3):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title()+", [3rd] " + period3.title())
    return schedule

student_schedule = make_schedule("mathematics", "history", "Physical Education")
print("SCHEDULE:", student_schedule)
