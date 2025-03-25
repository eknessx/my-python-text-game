import random

money = 3
points = 0
max_points = 0

def explain_rules():
    print("Welcome to the Gacha Game!")
    print("Rules:")
    print("1. You start with 3 dollars.")
    print("2. You can choose a number and the number of attempts.")
    print("3. If your attempts match, you win money equal to the difference of the attempts.")
    print("4. If your first attempt is greater than or equal to the second, you win points.")
    print("5. If your first attempt is less than the second, you win points.")
    print("6. Each attempt costs 1 dollar.")
    print("7. The game ends when you run out of money.")
    print("Good luck!\n")

def gacha():
    global money, points, max_points
    
    explain_rules()
    
    while money > 0:  
        enter = input(f"Would you like to gamble? Your current money is {money} $ (yes/no): ")
        if enter.lower() == "yes":
            try:
                chosen_number = int(input("Choose a number between 1 and 20: "))
                attempts = int(input("Enter the number of attempts: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            for _ in range(attempts):
                if money <= 0:
                    break
                x1 = random.randrange(1, 21)
                x2 = random.randrange(1, 21)
                print(f"Your first attempt is {x1}")
                print(f"Your second attempt is {x2}")

                if x1 == x2:
                    print(f"YOU GOT: {x1 - x2}")
                    money += x1 - x2 
                elif x1 >= x2:
                    points = x1 * x2 - 20 % 3
                    print(f"You got {points}")
                    money -= 1
                else:
                    points = x1 + x2 + max_points - 10
                    print(f"You got {points}")
                    money -= 1

                if points > max_points:
                    max_points = points
        else:
            print("You chose not to gamble.")
            print(f"Your current score is {points}")
            break

    print("You ran out of money")
    print(f"Your final score is {points}")

gacha()