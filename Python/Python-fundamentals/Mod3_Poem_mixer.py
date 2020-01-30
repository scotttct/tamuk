# index = 0
# user_input = input("Enter a saying or poem: ")
# words_list = user_input.split()
# words_new_list = []
# new_list = []

# while index < len(words_list):
#     if len(words_list[index]) < 4:
#         words_new_list.append(words_list[index].lower())
#         index += 1
#     elif len(words_list[index]) > 6:
#         words_new_list.append(words_list[index].upper())
#         index += 1
#     else:
#         words_new_list.append(words_list[index])
#         index += 1


# def word_mixer(words_new_list):
#     words_new_list.sort()
#     while len(words_new_list) > 5:
#         new_list.append(words_new_list.pop(-5))
#         new_list.append(words_new_list.pop(0))
#         new_list.append(words_new_list.pop()+"\n")
#         joined = " ".join(new_list)

#     print(joined)


# test = word_mixer(words_new_list)
###########################################################
#Next Try
def word_mixer(words_list1):
    new_words = []
    words_list1 = words_list1.split(" ")
    words_list1 = sorted(words_list1)
    while len(words_list1) > 5:
        f = words_list1.pop(-5)
        new_words.append(f)
        fp = words_list1.pop(0)
        new_words.append(fp)
        fpp = words_list1.pop(-1)
        new_words.append(fpp)
    new_words1 = " ".join(new_words)
    return(new_words1)


poem = input("enter a saying or poem: ")
words_list = poem.split()
p = len(words_list)
for x in range(p):
    y = len(words_list[x])
    if(y <= 3):
         words_list[x] = words_list[x].lower()
    if(y >= 7):
         words_list[x] = words_list[x].upper()
words_list = " ".join(words_list)
z = word_mixer(words_list)
print(z)
