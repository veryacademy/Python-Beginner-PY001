import random
x = random.randint(1,20)
for i in range(0,4):
    y = int(input("Guess the number between (1-20): "))
    if i == 2:
        print("This is your last guess!...")
    if x == y:
        print("You guessed correctly! ")
        print(f"The right number was {x}")
        break
if y != x:
    print(f"====\nSorry! The number was {x}\n====")