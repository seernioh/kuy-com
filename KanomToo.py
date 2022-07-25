"""main"""
def main():
    """input"""
    money = int(input())
    water = int(input())
    snack1 = int(input())
    snack2 = int(input())
    snack3 = int(input())
    money_left = money - water
    print("Now you have %d left."% (money_left))
    if money_left % 3 = 0:
            money_left - (snack1*10)
            print("Snack number1 : %d baht"% (snack1*10))
    elif money_left % 3 = 1:
        money_left - (snack1*15)
            print("Snack number1 : %d baht"% (snack1*15))
    elif money_left % 3 = 2:
        money_left - (snack1*20)
            print("Snack number1 : %d baht"% (snack1*20))
    else:
        print("You don't have enough money!")
        if money_left % 3 = 0:
            money_left - (snack2*12)
                print("Snack number1 : %d baht"% (snack2*12))
        elif money_left % 3 = 1:
            money_left - (snack2*15)
                print("Snack number1 : %d baht"% (snack2*15))
        elif money_left % 3 = 2:
            money_left - (snack2*18)
                print("Snack number1 : %d baht"% (snack2*18))
        else:
            print("You don't have enough money!")
            if money_left % 3 = 0:
                money_left - (snack3*5)
                print("Snack number1 : %d baht"% (snack3*5))
            elif money_left % 3 = 1:
                money_left - (snack3*7)
                print("Snack number1 : %d baht"% (snack3*7))
            elif money_left % 3 = 2:
                money_left - (snack3*9)
                print("Snack number1 : %d baht"% (snack3*9))
            else:
                print("You don't have enough money!")
main()
