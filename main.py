class Question():
    def __init__(self,text,diff,ans):
        self.text = text
        self.difficulty = diff
        self.answer = ans
        self.pos_count = 0

        self.ques_ask = False
        self.user_ans = None
        self.ques_score = self.score_calc()

    def score_calc(self):
        return int(self.difficulty)*10

    def is_correct(self):
        ans = input()
        self.user_ans = ans
        if ans == self.answer:
            self.ques_ask = True
            return True
        else:
            self.ques_ask = True
            return False

    def build_qustion(self):
        return f'Question: {self.text}\nDifficulty: {self.difficulty}'

    def question_reply_pos(self):
        return f'Your answer is correct, you resive {self.ques_score}'

    def question_reply_neg(self):
        return f'Your answer is incorrect, correct answer is {self.answer}'


