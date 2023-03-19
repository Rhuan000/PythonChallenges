import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizGUI:
    def __init__(self, quiz: QuizBrain):
        #get the information from the quiz_brain:
        self.quiz = quiz
        self.q_text: str
        #creating a window.
        self.window = tkinter.Tk()
        self.window.title('Quizz Game')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #creating label
        self.label = tkinter.Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR)
        self.label.grid(column=1, row=0)

        #creating canvas
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text='test', font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2)

        #Export png to img and creating button with this img
        false_img = tkinter.PhotoImage(file='images/false.png')
        true_img = tkinter.PhotoImage(file='images/true.png')
        self.right_button = tkinter.Button(image=true_img, highlightthickness=0, command=self.right_answer)
        self.wrong_button = tkinter.Button(image=false_img, highlightthickness=0, command=self.wrong_answer)
        self.right_button.grid(column=1, row=2)
        self.wrong_button.grid(column=0, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=self.q_text)
        self.label.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg="white")

    def right_answer(self):
        user_answer = "True"
        if self.quiz.check_answer(user_answer):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def wrong_answer(self):
        user_answer = "False"
        if self.quiz.check_answer(user_answer):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)