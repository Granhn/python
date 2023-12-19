from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_array = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    pregunta = Question(question_text ,question_answer)
    question_array.append(pregunta)

probando = QuizBrain(question_array)

while(probando.has_questions()):
    probando.next_question()
print(f"Game ended. Youre score was : {probando.score}")