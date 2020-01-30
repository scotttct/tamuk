# TASK 4
# APPEND
# Open task4_file.txt in append plus mode ("a+")
# create a for item in range(5): loop, for each loop:
# write to the file: "append #"+ str(item)+"\n"
# use seek() to set the pointer to the beginning of the file
# print the file contents using file .read() method after exiting the loop
# in append mode the file should only write to the end of the file regardless of setting seek() location

# [ ] complete the task  
# Provided Code creates and populates task4_file.txt  
def inc_count(cnt_file):
    cnt_file.seek(0,0)
    cnt_line = cnt_file.readline().strip()
    cnt = int(cnt_line[10:])+1
    cnt_file.seek(10,0)
    cnt_file.write(str(cnt))
    return cnt

count_file = open('task4_file.txt', 'w+')
count_file.write("Line1\nLine2\nLine3\n")
count_file.close()
# [ ] code here
count_file = open('task4_file.txt', 'a+')
count_file.seek(0)
count_line = count_file.readline().strip()
print("BEFORE\n" + count_line)

# call inc_task4() to increase the task4 5 times
for i in range(5):
    count = inc_count(count_file)
    count_file.write("line" + count + '\n')
    count_file.seek(0)
    print("\nAFTER inc_count() call", i+1, "\n" + count_file.readline().strip())

count_file.close()