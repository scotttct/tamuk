# total = 0
# items = ""

# while True:
#     request = input("Choose Report Type (\"A\" or \"T\"): ")
#     if request == "A":
#         break
#     elif request == "T":
#         break
#     else:
#         print(request, "is invalid input")

# print("Input an integer to add to the total or \"Q\" to quit")
# while True:
#     item = input("Enter an integer or \"Q\": ")
#     if item.isdigit():
#         if request == "A":
#             items = items + item + "\n"
#             total = total + int(item)
#         elif request == "T":
#             items = items + item + "\n"
#             total = total + int(item)
#     elif item.startswith("Q"):
#         if request == "A":
#             print("\nItems")
#             print(items)
#             print("Total")
#             print(total)
#         elif request == "T":
#             print("\nTotal")
#             print(total)
#         break
#     elif item == "":
#         pass
#     else:
#         print(item, "is invalid input")

total = 0
items = ""


while True:
    request = input("Choose Report Type (\"A\" or \"T\"): ")
    if request == "A":
        break
    elif request == "T":
        break
    else:
        print(request, "is invalid input")


def adding_report(report):
    if report == "A":
        print("\nItems")
        print(items)
        print("Total")
        print(total)
    elif report == "T":
        print("\nTotal")
        print(total)


print("Input an integer to add to the total or \"Q\" to quit")
while True:
    item = input("Enter an integer or \"Q\": ")
    if item.isdigit():
        if request == "A":
            items = items + item + "\n"
            total = total + int(item)
        elif request == "T":
            items = items + item + "\n"
            total = total + int(item)
    elif item.startswith("Q"):
        if request == "A":
            adding_report(request)
        elif request == "T":
            adding_report(request)
        break
    elif item == "":
        pass
    else:
        print(item, "is invalid input")
