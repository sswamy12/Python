'''
Created on Nov 5, 2018
From https://www.youtube.com/watch?v=rfscVS0vtbw&t=605s
@author: skanda
'''
from Question import Question

question_prompt = [
    "What color are apples?\n a) red\n b) blue\n c) orange\n\n",
    "What color are bananas?\n a) red\n b) blue\n c) yellow\n\n",
    "What color are grapes?\n a) white\n b) green\n c) yellow\n\n",    
]

questions = [
    Question(question_prompt[0],"a"),
    Question(question_prompt[1],"c"),
    Question(question_prompt[2],"b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got "+ str(score) + "/" + str(len(questions)) + " correct!")

run_test(questions)
