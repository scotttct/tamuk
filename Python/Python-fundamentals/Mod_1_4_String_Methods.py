# Module 1 Section 4: String Methods

# STRING METHODS: RETURN STRING INFORMATION
# len()
# returns a strings length

# .count()
# returns number of times a character or sub-string occur

# .find()
# returns index of first character or sub-string match
# returns - 1 if no match found
#########################################################
# TASK 1
# LEN()
# [ ] use len() to find the midpoint of the string
# [ ] print the halves on separate lines

# random_tip = "wear a hat when it rains"
# mid_tip = int(len(random_tip)/2)
# print(random_tip[:mid_tip])
# print(random_tip[mid_tip:])
#########################################################
# TASK 2
# .COUNT()
# for letters: "e" and "a" in random_tip
# [ ] print letter counts
# [ ] BONUS: print which letter is most frequent
# random_tip = "wear a hat when it rains"
# a_count = random_tip.count("a")
# e_count = random_tip.count("e")

# print( a_count, " = a count")
# print(e_count, " = a count")

# if a_count > e_count:
#   print("The letter a appears", a_count, "times which is greater than the letter e appears only",e_count,"times")
# elif e_count > a_count:
#     print("The letter e appears", e_count, "times which is greater than the letter a appears only",a_count,"times")
# else:
#     print("Both a and e appear equally")
###########################################################
# TASK 3
# .find()
# [ ] print long_word from the location of the first and second "t"
# long_word = "juxtaposition"
# first_t = long_word.find("t")
# second_t = long_word.find("t",first_t+1)
# print(long_word[first_t:second_t+1])

###############################################################


    # code to print word (index slice start:space_index)

# [ ] Print each word in the quote on a new line
quote = "they stumble who run fast"
start = 0
space_index = quote.find(" ")
while space_index != -1:
    print (quote[start:space_index])
    start = space_index+1
    space_index = quote.find(" ", space_index+1)
else:
    print (quote[start::1])
    
