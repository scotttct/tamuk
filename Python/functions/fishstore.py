
def fishstore():
    fish_entry = input("Input fish ")
    price_entry = input("Input price ")
    return "Fish Type: A " + str(fish_entry) + " costs $" + str(price_entry)


a = fishstore()
print(a)
