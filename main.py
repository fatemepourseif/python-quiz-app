from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    new_question = Question(text=question["question"], answer=question['correct_answer'])
    question_bank.append(new_question)

quiz = QuizBrain(q_list=question_bank)
quiz_ui = QuizInterface(quiz)
