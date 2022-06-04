"""Assembled Quiz Version 3
Incorporates the quiz gui, export gui and main home Gui and adds a new results gui
also incorporates user feedback and adds says māori instead of maori to be culturally appropriate.
4/06/2022
By Caleb Giddy"""

from tkinter import *
from functools import partial
import re
import random


class Home:
    def __init__(self):
        global rounds
        rounds = 0
        global score
        global best_score
        global total_score
        score = 0
        best_score = 0
        total_score = 0
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



        background_colour = "light blue"
        # setting frame for main gui
        self.home_frame = Frame(root, bg=background_colour, pady=10, padx=10)
        self.home_frame.pack(fill=BOTH, expand=YES)

        # heading label (row 0)
        self.home_heading_label = Label(self.home_frame,
                                        text="Māori Aotearoa Quiz",
                                        font="Arial 19 bold",
                                        bg=background_colour, padx=10, pady=10)
        self.home_heading_label.grid(row=0, sticky=EW, column=0)

        # instructions label (row 1)
        self.home_instructions_label = Label(self.home_frame,
                                             text="Welcome to the Te Reo Māori Quiz",
                                             font="Arial 10 italic", wraplength=200,
                                             justify=CENTER, bg=background_colour,
                                             padx=10, pady=10, )
        self.home_instructions_label.grid(row=1, sticky=EW)
        # quiz button and instructions (row 2)
        self.quiz_button = Button(self.home_frame, font="Arial 12 bold",
                                  text="Quiz", width=10,
                                  command=lambda: self.quiz(quiz_questions))
        self.quiz_button.grid(row=2, sticky=W, column=0)

        self.quiz_instructions_label = Label(self.home_frame,
                                             text="Press this button to partake in the quiz",
                                             wraplength=120,
                                             font="Arial 10 italic",
                                             justify=LEFT, bg=background_colour,
                                             padx=20, pady=10)
        self.quiz_instructions_label.grid(row=2, sticky=E, column=0)
        # export button and instructions (row 3)
        self.export_button = Button(self.home_frame, font="Arial 12 bold",
                                    text="Export", width=10,
                                    command=lambda: self.export())
        self.export_button.grid(row=3, sticky=W, column=0)

        self.export_instructions_label = Label(self.home_frame,
                                               text="Press this button to export the answers for revision",
                                               wraplength=120,
                                               font="Arial 10 italic",
                                               justify=LEFT, bg=background_colour,
                                               padx=20, pady=10)
        self.export_instructions_label.grid(row=3, sticky=E, column=0)
        # results button and instructions (row=4)
        self.results_button = Button(self.home_frame, font="Arial 12 bold",
                                     text="Results", width=10,
                                     command=lambda: self.results(score, rounds, best_score, total_score))
        self.results_button.grid(row=4, sticky=W, column=0)

        self.results_instructions_label = Label(self.home_frame,
                                                text="Press this button to see your previous results",
                                                wraplength=120,
                                                font="Arial 10 italic",
                                                justify=LEFT, bg=background_colour,
                                                padx=20, pady=10)
        self.results_instructions_label.grid(row=4, sticky=E, column=0)

    def export(self):
        Export(self)

    def quiz(self, quiz_questions):
        Quiz(self, quiz_questions)
        global rounds
        rounds += 1

    def results(self, score, rounds, best_score, total_score):
        Results(self, score, rounds, best_score, total_score)


class Results:
    def __init__(self, partner, score, rounds, best_score, total_score):
        self.score = score
        self.rounds = rounds
        self.best_score = best_score
        self.total_score = total_score

        background = "#FFCCCB"

        partner.results_button.config(state=DISABLED)

        self.results_box = Toplevel()

        self.results_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_results, partner))

        self.results_frame = Frame(self.results_box, width=300, bg=background)
        self.results_frame.grid()

        # Set up results heading (row 0)
        self.results_heading = Label(self.results_frame, text="Export instructions",
                                     font="arial 10 bold", bg=background)
        self.results_heading.grid(row=0)
        total_score = round(total_score, 2)
        # Export text (label, row 1)
        if rounds != 0:
            average_score = total_score/rounds
        else:
            average_score = 0
        self.results_text = Label(self.results_frame,
                                  text="BELOW ARE THE RESULTS FOR THE QUIZZES YOU HAVE COMPLETED\n"
                                       "BEST SCORE: {}\n"
                                       "AVERAGE SCORE: {}\n"
                                       "LATEST SCORE: {}\n".format(best_score, average_score, score),
                                  justify=LEFT, width=40, bg=background, wraplength=250)
        self.results_text.grid(row=2, pady=10)

    def close_results(self, partner):
        # Put export button back to normal...
        partner.results_button.config(state=NORMAL)
        self.results_box.destroy()


class Export:
    def __init__(self, partner):

        background = "#FFD580"  # Light Orange

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (export box)
        self.export_box = Toplevel()

        # If users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # Set up export heading (row 0)
        self.export_heading = Label(self.export_frame, text="Export instructions",
                                    font="arial 10 bold", bg=background)
        self.export_heading.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="Enter a file name in the box below and "
                                      "press the save button to save the Māori"
                                      "names to a file for revision",
                                 justify=LEFT, width=40, bg=background, wraplength=250)
        self.export_text.grid(row=2, pady=10)

        # Warning text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="If the file name you enter below "
                                      "already exists, it's content will"
                                      "be replaced with the answers for revision"
                                      "purposes",
                                 justify=LEFT, font="Arial 10 italic",
                                 bg="#ffafaf",  # Pink
                                 fg="maroon", wraplength=225, padx=10, pady=10)
        self.export_text.grid(row=1)

        # Filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20, font="Arial 14 bold",
                                    justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Save / Cancel Frame (row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_answers(partner)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

    def save_answers(self, partner):
        # Has expression to check file name. Can be upper or lower case letters
        global problem
        valid_char = "[A-Za-z0-9_]"  # Letters or underscores
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue  # If the letter is valid, goes back and checks the next

            elif letter == " ":  # Otherwise, find problems
                problem = "(no spaces allowed)"
            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":  # Describe problem
            self.save_error_label.config(text=f"Invalid filename - {problem}")
            # Change entry box background to light red
            self.filename_entry.config(bg="#ffafaf")
            print()
        else:
            # If there are no errors, generate text file and then close
            # Dialogue. Add .txt suffix!

            filename += ".txt"

            # create file to hold data
            f = open(filename, "w+")

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

            # add new line at end of each item
            for item in quiz_questions:
                ans = "{} is Māori For {}".format(item[0].title(), item[2].title())
                f.write(ans + "\n")
            macron_note = "Please Note that there are no macrons as python is unable to export macrons to .txt files"
            f.write("\n" + macron_note)
            # close file
            f.close()

            # Close dialogue
            self.close_export(partner)


# class for the quizz to be set up
class Quiz:
    def __init__(self, partner, quiz_questions):
        # declaring global variables and resetting variables

        partner.quiz_button.config(state=DISABLED)

        # Sets up child window (export box)
        self.quiz_box = Toplevel()

        # If users press cross at top, closes export and 'releases' export button
        self.quiz_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_quiz, partner))

        questions = quiz_questions
        global num_in_list
        num_in_list = 0
        global correct
        correct = 0

        # function which changes the question
        def question():
            self.submit_button.config(state=NORMAL)
            question_changed = False
            self.question_entry.delete(0, END)
            self.question_entry.configure(bg="white")
            self.correct_answer.config(text="")
            while not question_changed:
                global num_in_list
                # Give results when quiz is over
                if num_in_list == 10:
                    self.question_label.configure(text="The Quiz is over\n"
                                                       "you got a total of {} out of 10".format(correct))

                    def close_quiz():
                        global score
                        global best_score
                        global total_score
                        score = correct
                        total_score += score
                        if score > best_score:
                            best_score = score
                        print(score + best_score + total_score)
                        partner.quiz_button.config(state=NORMAL)
                        self.quiz_box.destroy()

                    self.question_entry.after(3000, close_quiz)

                # asks question
                else:
                    global eng_or_māori
                    global place
                    place = questions[num_in_list]
                    num_in_list += 1

                    eng_or_māori = random.randint(1, 2)
                    # randomises whether the question is asking for the māori or english word
                    if eng_or_māori == 1:
                        self.question_label.configure(text="What is the English Word for {}".format(place[1].title()))
                    else:
                        self.question_label.configure(text="What is the Māori Word for {}".format(place[2].title()))
                break

        # function for the submit button
        def submit():
            guess = self.question_entry.get()
            guess = str(guess)
            has_errors = False
            if guess == "":
                has_errors = True
            if has_errors == False:
                self.submit_button.config(state=DISABLED)

                global correct
                # if question is correct the box goes green for two seconds and add 1 to the correct total
                # otherwise box goes red for two seconds
                if eng_or_māori == 1:
                    if guess.lower() == place[2]:
                        self.question_entry.config(bg="lime")
                        self.question_entry.after(2000, question)
                        correct += 1

                    else:
                        self.question_entry.config(bg="red")
                        self.correct_answer.config(text="The correct answer was {}".format(place[2].title()))
                        self.question_entry.after(2000, question)
                else:
                    if guess.lower() == place[1] or guess.lower() == place[0]:
                        self.question_entry.config(bg="lime")
                        self.question_entry.after(2000, question)
                        correct += 1
                    else:

                        self.question_entry.config(bg="red")
                        self.correct_answer.config(text="The correct answer was {}".format(place[1].title()))
                        self.question_entry.after(2000, question)
            else:
                self.correct_answer.config(text="Sorry it cannot be blank")
        background_colour = "light green"
        # setting frame for main gui
        self.quiz_frame = Frame(self.quiz_box, bg=background_colour, pady=10, padx=10)
        self.quiz_frame.pack(fill=BOTH, expand=YES)

        # heading label (row 0)
        self.quiz_heading_label = Label(self.quiz_frame,
                                        text="Māori Aotearoa Quiz",
                                        font="Arial 19 bold",
                                        bg=background_colour, padx=10, pady=10)
        self.quiz_heading_label.grid(row=0, sticky=EW, column=0)

        # instructions label (row 1)
        self.quiz_instructions_label = Label(self.quiz_frame,
                                             text="Please enter the answer in the box with a space in between words\n"
                                                  "'-' and '_' will not be accepted",
                                             font="Arial 10 italic", wraplength=200,
                                             justify=CENTER, bg=background_colour,
                                             padx=10, pady=10)
        self.quiz_instructions_label.grid(row=1, sticky=EW)
        # question label (row 2)
        self.question_label = Label(self.quiz_frame,
                                    text="",
                                    font="Arial 10 italic", wraplength=200,
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
        # runs question 1


        self.correct_answer = Label(self.quiz_frame,
                                    font="Arial 10 bold",
                                    text="",justify=LEFT,bg=background_colour)
        self.correct_answer.grid(row=6, sticky=EW, column=0)

        question()
    def close_quiz(self, partner):
        # Put quiz button back to normal...
        global score
        global best_score
        global total_score
        score = correct
        total_score += score
        if score > best_score:
            best_score = score
        print(score + best_score + total_score)
        partner.quiz_button.config(state=NORMAL)
        self.quiz_box.destroy()


# main routine
if __name__ == "__main__":
    # opens gui and sets size
    root = Tk()
    root.geometry("300x400")
    root.resizable(False, False)
    stuff = Home()
    root.title("Māori Aotearoa Quiz")
    root.mainloop()


