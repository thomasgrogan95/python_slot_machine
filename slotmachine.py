import emoji
from random import choice

class Purse:
    def __init__(self):
        self.balance = 10

    def credit(self, winnings):
        self.winnings = winnings
        self.balance += winnings

    def debit(self, bet):
        self.bet = bet
        self.balance -= bet

    def get_balance(self):
        print(self.balance)
class Slot:
    def __init__(self):
        self.slots = []
        self.winnings = 0
    def take_bet(self, bet):
        self.bet = bet
        purse.debit(bet)
        slot.pull_handle()

    def pull_handle(self):
        col1.change_face()
        col2.change_face()
        col3.change_face()

    def show_slot(self):
        print(col1.face, col2.face, col3.face)

    def score_slot(self, bet):
        self.bet = bet
        if col1.face == col2.face == col3.face:
            self.winnings = bet * 2
            purse.credit(self.winnings)
        elif col1.face != col2.face != col3.face != col1.face:
            self.winnings = 0
        else:
            self.winnings = bet * 1.5
            purse.credit(self.winnings)



class Column:
    def __init__(self):
        self.face = []
    def change_face(self):
        self.faces = [emoji.emojize(':red_apple:'),
                 emoji.emojize(':pear:'),
                 emoji.emojize(':tangerine:')
                 ]
        self.face = choice(self.faces)


purse = Purse()
slot = Slot()
col1 = Column()
col2 = Column()
col3 = Column()


def looper():
    if purse.balance < 2:
        print("Thank you for playing. You are leaving with ", purse.balance)
    else:
        while True:
            try:
                bet = input("How much do you bet? ")
                if bet == "N":
                    print("Thank you for playing. You are leaving with", purse.balance)
                    break
                else:
                    bet = int(bet)
                    if bet >= 2 and bet <= purse.balance:
                        slot.take_bet(bet)
                        slot.show_slot()
                        slot.score_slot(bet)
                        print("You Score", slot.winnings, "- you have", purse.balance)
                        print()
                        looper()
                    else:
                        looper()
            except ValueError:
                continue
            else:
                break

def run_slot_machine():
    print("========== SLOT MACHINE ===========")
    print("Minimum bet is 2. Type 'N' to exit.")
    print("You have 10.00")
    print()
    looper()

run_slot_machine()
