def how_long(hobby):
    loop = True
    while loop == True:
        time = int(input("\nHow long for? (Enter number of minutes)\n> "))
        if type(time) != int:
            print("\nERROR: please enter a number\n")
        else:
            loop = False
    if time <= 30:
        print("\nWell Done! It's important to practise everyday,\n")
        print("Even a small amount each day will build up over time!\n")
        print("Keep Going!\n")
    else:
        print("\nAmazing work! Keep up the practise and watch yourself improve!\n")

def have_done(hobby):
    loop = True
    answers = ['y', 'Y', 'n', 'N']
    while loop == True:
        done_today = input(f"\nHave you done any {hobby} today? (y/n)\n> ")
        if done_today not in answers:
            print("\ninvalid input, enter 'y' or 'n'\n")
        else:
            loop = False
    if done_today == 'Y' or done_today == 'y':
        how_long(hobby)
    else:
        print("\nGet practising! Even doing a little everyday helps!\n")

def what_hobby():
    hobby = input("\nWhat is your hobby?\n> ")
    have_done(hobby)