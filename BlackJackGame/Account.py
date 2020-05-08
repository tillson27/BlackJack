class Account():

    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return f"Current account balance: {self.balance}"

    def place_bet(self):
        while True:
            user_bet = int(input("How much would you like to bet on this hand?: "))
            if self.balance == 0:
                print("You have no money, please add funds")
                add = int(input("How much would you like to add?"))
                while True
                    if deposit > 0:
                        self.balance += deposit
                        print(f"You have succesfully added {deposit} dollars to your account")
                        break
                    else:
                        print("Error! You may only deposit positive amounts")
                        conti
                continue
            elif user_bet > self.balance:
                print(f"Insufficient funds! You only have {self.balance}. Please choose again.")
                continue
            else:
                print(f"You have succesfully bet {user_bet} dollars on this game")
                break
        return user_bet

    def add_funds(self, deposit):
        if deposit > 0:
            self.balance += deposit
            print(f"You have succesfully added {deposit} dollars to your account")
        else:
            print("Error! You may only deposit positive amounts")

    def lose_funds(self, amount):
        self.balance -= amount
