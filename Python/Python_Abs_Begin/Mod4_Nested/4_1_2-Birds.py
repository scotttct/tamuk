# Found answer on: https://www.codeproject.com/Questions/1247399/Calling-function-in-nested-IF-in-Python

bird_names=('crow', 'parrot', 'eagle')
def bird_guess():
    bird_guess1=input('Enter the bird guess :')
    return bird_guess1

guess = bird_guess()

if(guess not in bird_names):
    print('1st try fail, do 2nd try')
    guess = bird_guess()
    if(guess not in bird_names):
        print('2nd try fail, please do 3rd try')
        guess = bird_guess()
        if(guess not in bird_names):
            print('Sorry, exhausted tries')
        else:
           print('corect on 3rd try')
    else:
       print('good work! correct on 2nd try')
else:
    print('great work!, correct on 1st try itself')