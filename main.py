from tkinter import *
from tkinter import ttk
import tkinter as tk
from poly2mono import poly2mono


# Tkinter interface for converting polytonic to monotonic


class myFrame(ttk.Frame):
    def __init__(self, main_window=tk.Tk()):
        super().__init__(main_window)
        ttk.Frame(main_window, padding=10)
        main_window.title("Polytonic to monotonic converter")
        main_window.geometry("600x800")

        self.place(x=0, y=0, width=600, height=800)

        print("Initialized interface.")

    def run(self):
        print("Running...")

        self.input_text = 'The polytonic text goes here.'
        self.output_text = 'You will see the result here.'

        label = ttk.Label(self, text='Convert polytonic text to monotonic', 
            font=("Helvetica", 16))
        label.pack(pady=5)

        self.input = Text(self, width=80, height=20)
        self.input.pack(pady=5)
        self.input.insert('1.0', self.input_text)

        self.button = Button(self, text="Convert", command=self.action)
        self.button.pack(pady=5)

        self.output = Text(self, width=80, height=20)
        self.output.pack(pady=5)
        self.output.insert('1.0', self.output_text)
        self.mainloop()

        print("Finish.")

    def action(self):
        self.input_text = self.input.get('0.0', 'end')
        self.output_text = poly2mono(self.input_text)

        self.output.delete('1.0', "end")
        self.output.insert('1.0', self.output_text)


if __name__ == "__main__":
    myFrame().run()
