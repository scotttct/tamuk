# import the file into the Jupyter Notebook environment
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt

def get_names():
    element5 = []
    print("list any 5 of the first 20 elements in the Period table")
    while len(element5) < 5:
        name = input("Enter the name of an element: ")
        if name in element5:
            print(name, "was already entered")
        elif name == "":
            print("don't allow empty strings")
        else:
            element5.append(name)
    return element5


file = open('elements1_20.txt', 'r')

elements_list = []
ele_temp = file.readline()
while ele_temp:
    elements_list.append(ele_temp.strip().lower())
    ele_temp = file.readline()

# Call the get_names() function
responses_list = get_names()

# check if responses are in the list of elements
correct_list = []
incorrect_list = []

for n in range(5):
    if responses_list[n] in elements_list:
        correct_list.append(responses_list[n])
    else:
        incorrect_list.append(responses_list[n])

# calculate the % correct
correct = len(correct_list) * 20
    
# Print output    
print(correct, "% correct")

print("\nFound:", end = " ")
for item in correct_list:
    print(item.title(), end = " ")

print("\nNot Found:", end = " ")    
for item in incorrect_list:
    print(item.title(), end = " ")


file.close()