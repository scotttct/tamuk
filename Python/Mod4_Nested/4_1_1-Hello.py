#Task 1
# [ ] Say "Hello" with nested if
# [ ] Challenge: handle input other than y/n

hello = input("Do you wnat to say hello? (y or n)")

if hello.lower() == "y":
    hi = input('do you want to say "Hello" and not just "Hi" (y = Hello, n = Hi) ')
    if hi.lower() == "y":
        print("Hello")
    else: 
            print("Hi")
else:
        print("You just nodded")