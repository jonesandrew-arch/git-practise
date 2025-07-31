i=1
number=7
while i<=3:
    guess=int(input("Guess the number(0-10): "))
    if guess == number:
        print("You win")
        break
    i+=1
else:
    print("Sorry you failed")