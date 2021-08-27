import random

class Winner:
    
    def __init__(self,comp,your):
        self.comp=comp
        self.your=your
        print("\n")
    
    def whosWinner(self):
        if self.comp == self.your:
            print("Its a tie.")
        elif self.comp == 's' and self.your == 'p':
            print("Computer is the Winner.")
        elif self.comp == 's' and self.your == 'r':
            print("Congratulations! You are the Winner.")
        elif self.comp == 'p' and self.your == 's':
            print("Congratulations! You are the Winner.")
        elif self.comp == 'p' and self.your == 'r':
            print("Computer is the Winner.")
        elif self.comp == 'r' and self.your == 'p':
            print("Congratulations! You are the Winner.")
        elif self.comp == 'r' and self.your == 's':
            print("Computer is the Winner.")

compTurn=random.randint(1,3)
if compTurn == 1:
    compTurn='r'
elif compTurn == 2:
    compTurn='p'
elif compTurn == 3:
    compTurn='s'

print("\nComputer turn done!.")
print('''Now its YOUR TURN: 
Enter 'r' for 'Rock' , 'p' for 'Paper' , 's' for 'Scissors' \n''')
yourTurn=input("Enter your option: ")

while yourTurn not in ('s','r','p'):
    yourTurn=input("Enter a valid option: ")
    if yourTurn in ('s','r','p'):
        break

evaluateWinner=Winner(compTurn,yourTurn)
evaluateWinner.whosWinner()
print(f'''\nComputer Chose: {compTurn}
You chose: {yourTurn} \n''')
    
