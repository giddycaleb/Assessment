"""quiz gui version 4
fully updated and working with comments
2/06/2020
Caleb Giddy"""

# imports for gui and to randomise whether its english to maori or maori to english
from tkinter import *
import random


# class for the quizz to be set up
class quiz:
    def __init__(self, quiz_questions):
        # declaring global variables and resetting variables
        questions = quiz_questions
        global num_in_list
        num_in_list = 0
        global correct
        correct = 0

        # function which changes the question
        def question():
            question_changed = False
            self.question_entry.delete(0, END)
            self.question_entry.configure(bg="white")
            while not question_changed:
                global num_in_list
                # gives results when quiz is over
                if num_in_list == 10:
                    self.question_label.configure(text="The Quiz is over\n"
                                                       "you got a total of {} out of 10".format(correct))

                # asks question
                else:
                    global eng_or_maori
                    global place
                    place = questions[num_in_list]
                    num_in_list += 1

                    eng_or_maori = random.randint(1, 2)
                    # randomises whether the question is asking for the maori or english word
                    if eng_or_maori == 1:
                        self.question_label.configure(text="What is the English Word for {}".format(place[1].title()))
                    else:
                        self.question_label.configure(text="What is the Maori Word for {}".format(place[2].title()))
                break

        # function for the submit button
        def submit():
            guess = self.question_entry.get()
            guess = str(guess)
            global correct
            # if question is correct the box goes green for two seconds and add 1 to the correct total
            # otherwise box goes red for two seconds
            if eng_or_maori == 1:
                if guess.lower() == place[2]:
                    self.question_entry.config(bg="lime")
                    self.question_entry.after(2000, question)
                    correct += 1

                else:
                    self.question_entry.config(bg="red")
                    self.question_entry.after(2000, question)
            else:
                if guess.lower() == place[1] or guess.lower() == place[0]:
                    self.question_entry.config(bg="lime")
                    self.question_entry.after(2000, question)
                    correct += 1
                else:

                    self.question_entry.config(bg="red")

                    self.question_entry.after(2000, question)

        background_colour = "light green"
        # setting frame for main gui
        self.quiz_frame = Frame(root, bg=background_colour, pady=10, padx=10)
        self.quiz_frame.pack(fill=BOTH, expand=YES)

        # heading label (row 0)
        self.quiz_heading_label = Label(self.quiz_frame,
                                        text="Maori Aotearoa Quiz",
                                        font="Arial 19 bold",
                                        bg=background_colour, padx=10, pady=10)
        self.quiz_heading_label.grid(row=0, sticky=EW, column=0)

        # instructions label (row 1)
        self.quiz_instructions_label = Label(self.quiz_frame,
                                             text="Please enter the answer in the box with a space in between words\n"
                                                  "'-' and '_' will not be accepted",
                                             font="Arial 10 italic", wrap=200,
                                             justify=CENTER, bg=background_colour,
                                             padx=10, pady=10)
        self.quiz_instructions_label.grid(row=1, sticky=EW)
        # question label (row 2)
        self.question_label = Label(self.quiz_frame,
                                    text="",
                                    font="Arial 10 italic", wrap=200,
                                    justify=LEFT, bg=background_colour,
                                    padx=10, pady=10)
        self.question_label.grid(row=2, sticky=EW)
        # entry box(row=3)
        self.question_entry = Entry(self.quiz_frame,
                                    font="Arial 14 italic",
                                    justify=LEFT, bg="white", width=20
                                    )
        self.question_entry.grid(row=3, sticky=EW)
        # blank label to leave a space
        self.blank = Label(self.quiz_frame,
                           text="",
                           bg=background_colour)
        self.blank.grid(row=4)
        # submit button
        self.submit_button = Button(self.quiz_frame, font="Arial 12 bold",
                                    text="SUBMIT", width=10,
                                    command=submit, pady=20)
        self.submit_button.grid(row=5, sticky=EW, column=0)
        #runs question 1
        question()

# set of quiz questions
# 1st item in list is maori without the macrons for when entering
# 2nd item is with macrons for when asking questions
# 3rd item is the english
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
stuff = quiz(quiz_questions)
# sets the name of the window
root.title("Maori Aotearoa Quiz")
root.mainloop()
