#Rooster Shrimp Crab Fish Deer Gourd
from random import randint
balance = 100
Dice = ["Rooster", "Shrimp", "Crab", "Fish", "Deer", "Gourd"]
def rngDice(bet, amount):
    x = randint(0,5)
    y = randint(0,5)
    z = randint(0,5)
    
    print("The result:",Dice[x],Dice[y],Dice[z])

    Dicex = Dice[x]
    Dicey = Dice[y]
    Dicez = Dice[z]
    total = 0
    global balance
    amountint = int(amount)
    if bet == Dicex or bet == Dicey or bet == Dicez:
        total = total + amountint
    if bet == Dicex: 
        total = total + amountint
    if bet == Dicey:
        total = total + amountint
    if bet == Dicez:
        total = total + amountint

    print()

    if total > 0:
        balance = balance + total

def main():
    global balance
    while balance > 0:
        print("Total balance is:",balance)
        print("What do you want to place your bet on?")
        print("[Rooster] [Shrimp] [Crab] [Fish] [Deer] [Gourd]\n")
        bet = input()
        bet = bet.capitalize()
        while bet not in Dice:
            print("ERROR: That is not a valid bet.")
            print("What do you want to place your bet on?")
            print("[Rooster] [Shrimp] [Crab] [Fish] [Deer] [Gourd]\n")
            bet = input()
            bet = bet.capitalize()        

        print("How much do you want to bet?\n")
        amount = input()
        try:
            amountint = int(amount)
            if amountint < 1:
                print("You can't bet negative values or zero.\n")
                main()
            elif amountint > balance:
                print("You can't bet more than you own.\n")
                main()
            balance = balance - amountint
            print()
            rngDice(bet, amount)
        except ValueError:
            print("ERROR: That is not an integer.\n")    

        if balance >= 200:
            print("Congrats You WIN! \nPlay again?(y/n)")
            decision = input()
            if decision == "y":
                balance = 100
                main()
            else:
                exit()
            
        elif balance <= 0:
            print("You lose. \nTry again?(y/n)")
            decision = input()
            if decision == "y":
                balance = 100
                main()
            else:
                exit()

main()
    

