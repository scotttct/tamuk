# Task 2
# INCREMENTING IN A WHILE() LOOP
# Program: Shirt Count
# enter a sizes (S, M, L)
# tally the count of each size
# input "exit" when finished
# report out the purchase of each shirt size
# [ ] Create the Shirt Count program, run tests


# CHALLENGE: Shirt Register (optional)
# Update the Shirt Count program to calculate cost

# use shirt cost (S = 6, M = 7, L = 8)
# to calculate and report the subtotal cost for each size
# to calculate and report the total cost of all shirts
# [ ] Create the Shirt Register program, run tests

shirt = 5
type_s = 0
type_m = 0
type_l = 0
type_s_price = 6
type_m_price = 7
type_l_price = 8
total_shirt = 0
while True:
      type_shirt = input ("What size do you want 'small', 'medium' or large': ")
      if type_shirt.startswith("s") :
            type_s += 1
      elif type_shirt.startswith("m"):
            type_m += 1
      elif  type_shirt.startswith("l") :
            type_l += 1
      else:
            print("We do not have it")
      total_shirt += 1
      if total_shirt >= shirt:
            print("We do not have them any more")
            break
cost_s = type_s_price * type_s
cost_m = type_m_price * type_m
cost_l = type_l_price * type_l
total_cost = type_s * type_s_price + type_m_price * type_m + type_l_price * type_l
print("Number of shirt are" , total_shirt, "Total cost is $ " , total_cost, "\nSmall size price", cost_s , "\nMedium size price", cost_m , "\nLarge size price", cost_l)


