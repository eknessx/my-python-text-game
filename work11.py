import random


def explain():
    print("welcome to buckshot roulete game")
    print("Rules:")
    print("The rules are simple, you have a revelover and 6 chambers with 6 bullets")
    print("You have to spin the chamber and pull the trigger")
    print("If you survive,you win the game")
    print("as i said before, 6 bullets 6 chambers 3 lives")
    print("if you lose, you die")
    print("Good luck!\n")

def roulete():
    chambers = 6
    bullets = random.randint(1, 7)
    lives = 3
    cylinder = [0]*chambers
    bullet_position = random.sample(range(chambers), bullets)

    for position in bullet_position:
        cylinder[position] = 1

    random.shuffle(cylinder)

    explain()

    while True:
        input("Press Enter to spin the chamber....")
        shot=cylinder.pop(0)

        if shot == 1:
            print("BANG! You're shooted!")
            lives -= 1
            print(f"You have {lives} lives left")
            if lives == 0:
                print("You died!")
                break           
        else:
            print("Click! You survived!")
        if len(cylinder) == 0:
            print("You survived the game!")
            break
roulete()    