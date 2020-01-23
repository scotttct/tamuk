# cast to int at input
mother_age =  input ("How old is your mother (integer): ")
father_age= input ("How old is your father (interger): ")
if mother_age.isdigit() and father_age.isdigit() :
      print("Ok, family age" , int(mother_age) + int(father_age) + 1)
else:
      print ("Please input number")