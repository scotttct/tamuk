#Implement an algorithm to determine if a string has all unique characters.

#DID NOT WORK
# def unique(s):
#     uchars = set()
#     for c in s:
#         if c in uchars:
#             return False
#         uchars.add(c)
#     return True

#This worked from Stack Overflow: https://stackoverflow.com/questions/17357370/implementing-an-algorithm-to-determine-if-a-string-has-all-unique-characters
def isUniqueChars2(string):
  uchars = []
  for c in string:
    if c in uchars:
      return False
    else:
      uchars.append(c)
  return True
  
statement = input("Place you sentence here: ", )
print(isUniqueChars2(statement))
