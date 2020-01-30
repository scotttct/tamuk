# TASK 3
# .READLINE() WITH .STRIP() RAINBOW COLORS
# assumes rainbow.tx has been imported in task 1

# open rainbow.txt as rainbow_file as read-only
# read a color from each line of rainbow_file in a while loop
# use .strip to remove the whitespace
# print each color upper case
# close rainbow_file
# [ ] open rainbow.txt as rainbow_text as read-only  


# [ ] read a color from each line of rainbow_text in a while loop  
# use .strip to remove the whitespace '\n' character 
# print each color upper case 
# rainbow = open('rainbow.txt', 'r')
# rainbow_line = rainbow.readline().strip()

# while rainbow_line:
#     print(rainbow_line.capitalize())
#     rainbow_line = rainbow.readline().strip()
    
# rainbow.close()
#####################################################
#Task 4 Spit :
# [ ] run to read the file into memory
# cities_messy = open('cities_messy.txt', 'r')

# line = cities_messy.readline().strip(':\n')

# while line:
#     print(line)
#     line = cities_messy.readline().strip(':\n')

# cities_messy.close()
########################################################
# TASK 5
# .STRIP() PARENTHESES FROM POEM2_MESSY
# import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2_messy as poem2_messy.txt
# open poem2_messy.txt as poem2_messy in read mode
# edit while loop to strip the leading and trailing parentheses & print the poem without blank lines
# close poem2_messy
# [ ] import https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2_messy as poem2_messy.txt
# [ ] open poem2_messy.txt as poem2_messy in read mode
# [ ] edit while loop to strip the leading and trailing parentheses, and newlines
# [ ] print the poem 
poem2_messy = open("poem2_messy.txt", 'r')
line = poem2_messy.readline()

while line:
    print(line)
    line = poem2_messy.readline().strip('(\)\n')