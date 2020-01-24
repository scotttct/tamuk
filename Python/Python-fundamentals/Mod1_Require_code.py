# #quote "Wheresoever you go, go with all your heart"
# quote = str(input())
# word = ""
# for letter in quote:
#     if letter.isalpha():
#         word += letter
#     elif word.lower() >= "h":
#         print(word.upper())
#         word = ""
#     else:
#         word = ""
# if word.lower() >= "h":
#     print(word.upper())
quote = str(input())
word = ""
for letter in quote:
    if letter.isalpha():
        word += letter
    elif word.lower() >= "h":
        print(word.upper())
        word = ""
    else:
        word = ""
if word.lower() >= "h":
    print(word.upper())