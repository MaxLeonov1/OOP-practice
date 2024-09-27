from main import Question
import json
import random
with open('questions', 'r', encoding='utf-8') as file:
    data = json.loads(file.read())

user_ans_list = []
class Quiz():
    def __init__(self,data):
        self.score = 0
        self.Q = []
        self.data = data
        self.ans_list = []

    def Q_table(self):
        for qwest in self.data:
            self.Q.append(Question(qwest['q'], qwest['d'], qwest['a']))

    def Quizing(self):
        global user_ans_list
        self.Q_table()
        random.shuffle(self.Q)
        for q in self.Q:
            print(q.build_qustion())
            if q.is_correct() == True:
                print(q.question_reply_pos())
                self.score += q.ques_score
                self.ans_list.append(q.user_ans)
            else:
                print(q.question_reply_neg())
                self.ans_list.append(q.user_ans)
        user_ans_list.append((self.ans_list,self.score))



quiz = Quiz(data)
quiz.Quizing()
print(user_ans_list)


