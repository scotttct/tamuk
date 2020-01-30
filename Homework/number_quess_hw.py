#(number should be between 1 and 1000)
# guesscorrect = False
# number = 362
# intervalMin = 1 
# intervalMax = 1000
# # number = int(intervalMin + (intervalMin + intervalMax)/2)

# def get_computer_guess(intervalMin, intervalMax):
#     return  int(intervalMin + (intervalMin + intervalMax)/2)

# #650
# while(True):
#     #ask a number 
#     c = input("My guess is " + number + ". Is it correct, greater, or lesser than the number you thought of (E/L/G?" )
   
#     if (c == "L"):
#         intervalMax - number -1
#         number = get_computer_guess(intervalMin, intervalMax)
#     elif(c == "G"):
#         intervalMin = number +1
#         number = (number + intervalMin)/2
#     elif (c == "E"):
        
#         print("Yay!")
#         break

# guesscorrect = False
number = 650
intervalMin = 1 
intervalMax = 1000
# number = int(intervalMin + (intervalMin + intervalMax)/2)

def get_computer_guess(intervalMin, intervalMax):
    return  int(intervalMin + (intervalMin + intervalMax)/2)

#650
while(True):
    #ask a number 
    c = input("My guess is " + str(number) + ". Is it correct, greater, or lesser than the number you thought of (E/L/G?" )
   
    if (c == "L"):
        intervalMax - number -1
        number = get_computer_guess(intervalMin, intervalMax)
    elif(c == "G"):
        intervalMin = number +1
        number = (number + intervalMin)/2
    elif (c == "E"):
        
        print("Yay!")
        break