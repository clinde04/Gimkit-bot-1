import pprint

class AnswerPosition:
    #top left: x y
    tlX = 0
    tlY = 0
    #bottom right: x y
    brX = 0
    brY = 0
    pass

class QuestionPosition:
    #top left: x y
    tlX = 0
    tlY = 0
    #bottom right: x y
    brX = 0
    brY = 0

#for bruteforce mode
class Question:
    hasAnswer = False
    
    question = ""
    answer = ""

    redAnswer = False
    orangeAnswer = False
    greenAnswer = False
    blueAnswer = False
    pass

red_answer_position = AnswerPosition()
orange_answer_position = AnswerPosition()
green_answer_position = AnswerPosition()
blue_answer_position = AnswerPosition()

question_postion = QuestionPosition()

def study_mode():
    print("Starting Study mode!")

    pass

def brute_force_mode():
    print("Starting Bruteforce mode!")
    
    pass

choice = input("""Choose bot mode:
1 -> Study mode
2 -> Bruteforce mode
""")

print("Starting...")

if choice == 1:
    study_mode()
elif choice == 2:
    brute_force_mode()
else:
    print("Invalid choice!")