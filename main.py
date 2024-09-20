class Question():
    def __init__(self,text,diff,ans):
        self.text = text
        self.difficulty = diff
        self.answer = ans

        self.ques_ask = False
        self.user_ans = None
        self.ques_score = self.score_calc()

    def score_calc(self):
        return self.difficulty*10

    def get_score(self):
        if input() == 'get score':
            print(f'Your score is ')

    def is_correct(self):
        if input() == self.answer:
            self.ques_ask = True
            return True
        else:
            self.ques_ask = True
            return False

    def build_qustion(self):
        print(f'Question: {self.text}'
              f'Difficulty: {self.difficulty}')

    def question_reply_pos(self):
        print(f'Your answer is correct, you resive {self.ques_score}')

    def question_reply_neg(self):
        print(f'Your answer is incorrect, correct answer is {self.answer}')
