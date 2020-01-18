def bird_available(bird):
    bird_types = 'crow robin parrot eagle sandpiper hawk pigeon'
    return bird.lower() in bird_types.lower()

a_bird = input("input a bird name to check for availability: ")
available = bird_available(a_bird)
print("available?", available)