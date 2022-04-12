

username = input("Please enter user name: ")
print("=================== Welcome to the Quiz!" + username + "! ===================")

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
          self.correct = False

question_prompts = [
     "Q1 \n|What colour are apples?|\n\n(a) Red/Green\n(b) Orange\n",
     "Q2 \n|What colour are bananas?|\n\n(a) Red\n(b) Green\n(c) Yellow\n",
     "Q3 \n|What colour is the pen?|\n\n(a) Red\n(b) Blue\n",
     "Q4 \n|Why is there a gnome in the garden?|\n\n (a) He defends the North.\n (b) He defends the South.\n (c) He defends the West.\n (d) He defends the East.\n", 
     "Q5 \n|Which is better Apple or Android?|\n\n(a) Apple\n(b) Android\n"
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "c"),
     Question(question_prompts[2], "a"),
     Question(question_prompts[3], "d"),
     Question(question_prompts[4], "b"),
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            question.correct = True
    #  print("you got", score, "out of", len(questions))

    index = 1
    correct_answers = 0
    for question in questions:
        if question.correct == True:
            print(f"Congratulations, you got question {index} right.")
            index += 1
            correct_answers += 1

        else:
            print(f"Unlucky, you got question {index} wrong")

        print(f"You got {correct_answers} points")
    
    print("\n=================== Thank you for playing " + username + " !===================")



run_quiz(questions)

#Code by Ash & Steve 
# adapted from this website
