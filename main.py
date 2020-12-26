from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_bank = []

for question in question_data:
    q_text = question["text"]
    q_ans = question["answer"]
    new_question = Question(q_text, q_ans)
    questions_bank.append(new_question)

quizee = QuizBrain(questions_bank)

while(quizee.has_question()):
    quizee.next_question()


print("hurra! you have completed the quiz!!!")
print(f"Your final score is  : {quizee.score} / {len(quizee.question_list)}")
