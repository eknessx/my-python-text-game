#this code is my for alan Turning tribute for his birthday!
import json
import random
import os

#function to load the game data
def Getdata():
    path = os.path.join(os.path.dirname(__file__), "Turing_facts.json")#gets the file path for the json data
    try:
        with open("c:/Users/Admin/Desktop/New folder/Turining_facts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Could not find Turing_facts.json")
        return []

#main fucntion to run the game it will ask the user about facts and questions about him
def runGame():
    questions = Getdata()#it gets the data and question stored in the json file
    if not questions:
        return


    score = 0
    random.shuffle(questions)  # Shuffle question order

    print("Type your answer and press Enter.\n")

    #game for loop and iterate throught the questions
    for q in questions:
        print(q["question"])
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = q["answer"].strip().lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The right answer was: {q['answer']}\n")

    print(f"Quiz complete! Your score: {score}/{len(questions)}")
runGame()
