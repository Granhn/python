class QuizBrain:
    def __init__(self,question_list) -> None:
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
    

    def has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        response = ""
        while(response != "true" or response != "false") :
            response = input(f"Q.{self.question_number + 1 }: {self.question_list[self.question_number].question} (True/False)?:").lower()
            if(response == "true" or response == "false"):
                self.check_answer(self.question_list[self.question_number].answer, response)
                self.question_number+=1     

                break
            else:
                print("Please type true or false")
                break
                


    def check_answer(self, answer, user_answer):
        if answer.lower() == user_answer.lower():
            print("Correct!!")
            self.score +=1
        else:
            print("Incorrect :/")
        print(f"The correct answer was {answer}")
        
