from main import Question
import json
import random
with open('questions', 'r', encoding='utf-8') as file:

    data = json.loads(file.read())

score = 0
Q = []

for qwest in data:
    Q.append(Question(qwest['q'],qwest['d'],qwest['a']))

random.shuffle(Q)

for q in Q:
    q.build_qustion()
    q.get_score()
    if q.is_correct() == True:
        q.question_reply_pos()
        score += q.ques_score
    elif q.is_correct() == False:
        q.question_reply_neg()
