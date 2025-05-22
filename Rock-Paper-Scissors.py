import random
a=input("What do you want to choose? Type 0 for rock, 1 for paper or 2 for scissors")
if a =="0":
    print("You chose Rock")
    b=random.randint(1,3)
    if b:=1:
        print("Computer chose Scissors! You Won")
    elif b:=2:
        print("Computer chose paper! You lost")
    elif b:=3:
        print("Computer chose rock! It's a draw")
        
elif a =="1":
    print("You chose Paper")
    b=random.randint(1,3)
    if b:=1:
        print("Computer chose Scissors! You lost")
    elif b:=2:
        print("Computer chose paper! It's a draw")
    elif b:=3:
        print("Computer chose rock! You won")
        
elif a =="2":
    print("You chose Scissors")
    b=random.randint(1,3)
    if b:=1:
        print("Computer chose Scissors! It's a draw")
    elif b:=2:
        print("Computer chose paper! You Won")
    elif b:=3:
        print("Computer chose rock! You lost")