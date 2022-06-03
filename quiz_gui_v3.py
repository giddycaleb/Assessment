from tkinter import *
import random
import time


class Home:
    def __init__(self, quiz_questions):
        questions = quiz_questions
        global num_in_list
        num_in_list = 0
        def question():
            question_changed = False
            self.question_entry.delete(0,END)
            self.question_entry.configure(bg="white")
            while not question_changed:

                global num_in_list
                global eng_or_maori
                global place
                place = questions[num_in_list]
                num_in_list+=1


                eng_or_maori = random.randint(1, 2)

                if eng_or_maori == 1:
                    self.question_label.configure(text="What is the English Word for {}".format(place[1].title()))
                else:
                    self.question_label.configure(text="What is the Maori Word for {}".format(place[2].title()))
                break

        def x():
            num = 1
        def submit():
            guess = self.question_entry.get()
            guess = str(guess)

            if eng_or_maori == 1:
                if guess.lower() == place[2]:
                    self.question_entry.config(bg="lime")
                    self.question_entry.after(2000,question)

                else:
                    self.question_entry.config(bg="red")
                    self.question_entry.after(2000,question)
            else:
                if guess.lower() == place[1] or guess.lower() == place[0]:
                    self.question_entry.config(bg="lime")
                    self.question_entry.after(2000,question)
                else:

                    self.question_entry.config(bg="red")

                    self.question_entry.after(2000,question)

        def reset_box(color):
            self.question_entry.configure(bg=color)

        background_colour = "light green"
        # setting frame for main gui
        self.home_frame = Frame(root, bg=background_colour, pady=10, padx=10)
        self.home_frame.pack(fill=BOTH, expand=YES)

        # heading label (row 0)
        self.quiz_heading_label = Label(self.home_frame,
                                        text="Maori Aotearoa Quiz",
                                        font="Arial 19 bold",
                                        bg=background_colour, padx=10, pady=10)
        self.quiz_heading_label.grid(row=0, sticky=EW, column=0)

        # instructions label (row 1)
        self.quiz_instructions_label = Label(self.home_frame,
                                             text="Please enter the answer in the box with a space in between words\n"
                                                  "'-' and '_' will not be accepted",
                                             font="Arial 10 italic", wrap=200,
                                             justify=CENTER, bg=background_colour,
                                             padx=10, pady=10)
        self.quiz_instructions_label.grid(row=1, sticky=EW)
        # quiz button and instructions (row 2)
        self.question_label = Label(self.home_frame,
                                    text="",
                                    font="Arial 10 italic", wrap=200,
                                    justify=LEFT, bg=background_colour,
                                    padx=10, pady=10)
        self.question_label.grid(row=2, sticky=EW)

        self.question_entry = Entry(self.home_frame,
                                    font="Arial 14 italic",
                                    justify=LEFT, bg="white", width=20
                                    )
        self.question_entry.grid(row=3, sticky=EW)

        self.blank = Label(self.home_frame,
                           text="",
                           bg=background_colour)
        self.blank.grid(row=4)

        self.submit_button = Button(self.home_frame, font="Arial 12 bold",
                                    text="SUBMIT", width=10,
                                    command=submit, pady=20)
        self.submit_button.grid(row=5, sticky=EW, column=0)

        question()



quiz_questions = [["tamaki makau rau", "tāmaki makau rau", "auckland"],
                  ["otautahi", "ōtautahi", "christchurch"],
                  ["te whanganui a tara", "te whanganui a tara", "wellington"],
                  ["whakatu", "whakatū", "nelson"],
                  ["otepoti", "о̄tepoti", "dunedin"],
                  ["aotearoa", "aotearoa", "new zealand"],
                  ["te waipounamu", "te waipounamu", "south island"],
                  ["te ika a maui", "te ika a māui", "north island"],
                  ["waihopai", "waihōpai", "invercargil"],
                  ["ngamotu", "ngāmotu", "new plymouth"]]

# opens gui and sets size
root = Tk()
root.geometry("300x400")
root.resizable(False, False)
stuff = Home(quiz_questions)
root.title("Maori Aotearoa Quiz")
root.mainloop()


