# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print “Fizz” instead of the number
#  and for the multiples of five print “Buzz”.
#  For numbers which are multiples of both three and five print “FizzBuzz”."

# for i in range(0, 101):
#     print(i)

# print()

# for t in range(0, 101, 3):
#     print(t)

# print()

# for f in range(0, 101, 5):
#     f="fizz"
#     print(f)
###################################################################
# prints odd numbers as a template for creating a function to perform the task of printing by 3 and replace
# def even_numbers(number):
# 	for i in range(number):
# 		if i == 0:
# 			continue
# 		elif i%2 == 0:
# 			print(i)
# 		else:
# 			continue
 
# print(even_numbers(101))

#create a function that prints all the necessary assignment parameters
#This attempt printed biff only
# def nums(number1, number2):
# 	for i in range(number1, number2):
# 		While i in range(number1, number2, 3)	
	
# 			print("biff")
# 		elif:
# 			continue
 
# print(nums(1,101))

#another attempt that printed all 1's
# i = 1
# while i < 101:
#   print(i)
# if (i == 3):
#     print("biff")
# elif (1==5):
#     print("baff")
# elif (i==3 or i==5):
#     print("biffbaff")  
# i += 1

# trying for nested for loops, taking from python documentation and modified
for n in range(1, 101):
	print(n)
	if n in range(1,101,3):
		print("biff")
	elif n in range(1,101,5):
		print('baff')
	elif n in range(1, 101, 3) or n in range(1,101,5): #this line does not work
		print("biffbaff")
         
        
           
# ...     else:
# ...         # loop fell through without finding a factor
# ...         print(n, 'is a prime number')