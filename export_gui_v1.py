"""Home Gui version 2
20/05/2022
By Caleb Giddy"""

from tkinter import *
from functools import partial
import re

# test command to see the buttons are working
def hi():
    print("hi")


class Home:
    def __init__(self):



        background_colour = "light blue"
        # setting frame for main gui
        self.home_frame = Frame(root, bg=background_colour, pady=10, padx=10)
        self.home_frame.pack(fill=BOTH, expand=YES)

        # heading label (row 0)
        self.home_heading_label = Label(self.home_frame,
                                        text="Maori Aotearoa Quiz",
                                        font="Arial 19 bold",
                                        bg=background_colour, padx=10, pady=10)
        self.home_heading_label.grid(row=0, sticky=EW, column=0)

        # instructions label (row 1)
        self.home_instructions_label = Label(self.home_frame,
                                             text="Welcome to the Te Reo Maori Quiz",
                                             font="Arial 10 italic", wrap=200,
                                             justify=CENTER, bg=background_colour,
                                             padx=10, pady=10, )
        self.home_instructions_label.grid(row=1, sticky=EW)
        # quiz button and instructions (row 2)
        self.quiz_button = Button(self.home_frame, font="Arial 12 bold",
                                  text="Quiz", width=10,
                                  command=hi)
        self.quiz_button.grid(row=2, sticky=W, column=0)

        self.quiz_instructions_label = Label(self.home_frame,
                                             text="Press this button to partake in the quiz",
                                             wrap=120,
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
                                               wrap=120,
                                               font="Arial 10 italic",
                                               justify=LEFT, bg=background_colour,
                                               padx=20, pady=10)
        self.export_instructions_label.grid(row=3, sticky=E, column=0)
        # results button and instructions (row=4)
        self.results_button = Button(self.home_frame, font="Arial 12 bold",
                                     text="Results", width=10,
                                     command=hi)
        self.results_button.grid(row=4, sticky=W, column=0)

        self.results_instructions_label = Label(self.home_frame,
                                                text="Press this button to see your previous results",
                                                wrap=120,
                                                font="Arial 10 italic",
                                                justify=LEFT, bg=background_colour,
                                                padx=20, pady=10)
        self.results_instructions_label.grid(row=4, sticky=E, column=0)

    def export(self):
        Export(self)
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
        self.how_heading = Label(self.export_frame, text="Export instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="Enter a file name in the box below and "
                                      "press the save button to save the Maori"
                                      "names to a file for revision",
                                 justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=2, pady=10)

        # Warning text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="If the file name you enter below "
                                      "already exists, it's content will"
                                      "be replaced with the answers for revision"
                                      "purposes",
                                 justify=LEFT, font="Arial 10 italic",
                                 bg="#ffafaf",  # Pink
                                 fg="maroon", wrap=225, padx=10, pady=10)
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
                                  command=partial(lambda: self.save_history(partner)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

    def save_history(self, partner):
        # Has expression to check file name. Can be upper or lower case letters
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
                ans = "{} is Maori For {}".format(item[0].title(),item[2].title())
                f.write(ans + "\n")
            macron_note = "Please Note that there are no macrons as python is unable to export macrons to .txt files"
            f.write("\n"+macron_note)
            # close file
            f.close()

            # Close dialogue
            self.close_export(partner)

# main routine
if __name__ == "__main__":
    # opens gui and sets size
    root = Tk()
    root.geometry("300x400")
    root.resizable(False, False)
    stuff = Home()
    root.title("Maori Aotearoa Quiz")
    root.mainloop()

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
