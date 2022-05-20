"""Home Gui version 1
19/05/2022
By Caleb Giddy"""

from tkinter import *


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
                                  command=sammy)
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
                                    command=sammy)
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
                                     command=sammy)
        self.results_button.grid(row=4, sticky=W, column=0)

        self.results_instructions_label = Label(self.home_frame,
                                                text="Press this button to see your previous results",
                                                wrap=120,
                                                font="Arial 10 italic",
                                                justify=LEFT, bg=background_colour,
                                                padx=20, pady=10)
        self.results_instructions_label.grid(row=4, sticky=E, column=0)


# main routine
if __name__ == "__main__":
    # opens gui and sets size
    root = Tk()
    root.geometry("300x400")
    root.resizable(False, False)
    stuff = Home()
    root.title("Maori Aotearoa Quiz")
    root.mainloop()
