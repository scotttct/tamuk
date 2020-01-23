# set values for maximum order variables
max_order = 113.0
# set values minimum order variables
min_order = 0.15
# set value for price variable
order_price = 7.99
#get order_amount input and cast to a number
order_amount = input ("How much cheese do you want? ")
#check order_amount and give message checking against
#over maximum
if float(order_amount) >= max_order:
      print ("Sorry our inventory is only " + max_order)
#under minimum
elif float(order_amount) <= min_order:
      print("Sorry you must order at least:" + min_order)
#else within maximum and minimum give message with calculated price
else:
      print("The total is $" , float (order_amount) * order_price)