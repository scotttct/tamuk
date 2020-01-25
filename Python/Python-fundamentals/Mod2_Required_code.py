def list_o_matic(animal_input):
    if not animal_input:
        popped = animal_list.pop()
        return popped + " popped from list"
    else:
        if animal_input in animal_list:
            animal_list.remove(animal_input)
            return "1 instance of " + animal_input + " removed from list"
        else:
            animal_list.append(animal_input)
            return "1 instance of " + animal_input + " appended to list"



animal_list = ['cat', 'goat', 'cat']
while animal_list:
    print("Look at all the animals", animal_list)
    animal_input = input("Enter the name of an animal: ")
        
    if not animal_input.upper() == "QUIT":
        print(list_o_matic(animal_input))
    else:
        print("Goodbye!")
        break