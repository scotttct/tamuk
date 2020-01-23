# set values for maximum order variables
max_order = 50.0
# set values minimum order variables
min_order = 0.5
# set value for price variable
order_price = 2
#get order_amount input and cast to a number
order_amount = input ("How much icream do you want? ")
#check order_amount and give message checking against
#over maximum
if float(order_amount) >= max_order:
      print ("Sorry but we can't")
#under minimum
elif float(order_amount) <= min_order:
      print("Sorry we do not small protion take away, maybe you would like a cone")
#else within maximum and minimum give message with calculated price
else:
      print("The total is $" , float (order_amount) * order_price)
