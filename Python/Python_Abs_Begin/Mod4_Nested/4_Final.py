def str_analysis(io):
      io = input("Input a letter or number: ")
      return (io)


while True:
      user = input("Input a letter or number: ")
      print()
      if user.isdigit():
            if int(user) >= 99:
                  print("It is a Big Number")
            elif int(user) <= 99:
                  print("It is a Small Number")
      elif user.isalpha():
            print("It is all alphabetical")
      else:
            print("Wow, is not a number or a letter!")
            break
