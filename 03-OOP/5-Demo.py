# Question


class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,answer):
        return self.answer == answer



# Quiz
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    def getQuestion(self):
        return self.questions[self.questionIndex]
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex +1 }: {question.text}")

        for q in question.choices:
            print("-"+q)
        answer = input("cevap : ")  
        self.questions(answer)
        self.loadQuestion()
    def quess(self,answer):
        question = self.Questions()

        if question.checkAnswer(answer):
            self.score += 1

        self.questionIndex += 1
        
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayQuestion()

    def showScore(self):
        print("Score :", self.score)

q1 = Question("En iyi programlama dili hangisidir ? ", [
              "c#", "Python", "Javascript", "Java"], "Python")

q2 = Question("En popüler programlama dili hangisidir ? ", [
              "Python", "c#", "Java", "Javascript"], "Python")

q3 = Question("En çok kazandıran programlama dili hangisidir ? ", [
               "Java", "Javascript","c#", "Python"], "Python")
questions= [q1,q2,q3]
print(q1.checkAnswer("Python"))

quiz = Quiz(questions)
quiz.displayQuestion()

