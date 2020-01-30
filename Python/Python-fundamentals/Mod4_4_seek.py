# TASK 3
# SEEK() WITH OPTIONAL WHENCE ARGUMENT
# open a new file days.txt in write plus read mode 'w+'
days = open("days.txt", 'w+')
# write week days (Monday - Friday) on separate lines
days.write("Monday\nTuesday\nWednesday\nThursday\nFriday")
# use .seek() to move the pointer to the start of the file
days.seek(0)
# use .read() to read the entire file contents
week_days = days.read().strip("()\n")

# print the entire file contents and close the file
print(week_days)
# use .seek() to move the pointer to the end of the file and write the weekend days (Saturday & Sunday)
days.seek(0,2)
days.write("\nSaturday\nSunday")
# use .seek() to move the pointer to the start of the file
days.seek(0,0)
# use .read() to read the entire file contents
all_days = days.read().strip("()\n")
# print the entire file contents and close the file
print(all_days)
days.close()
