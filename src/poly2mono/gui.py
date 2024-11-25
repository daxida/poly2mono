"""Tkinter interface for converting polytonic to monotonic."""

from tkinter import LEFT, Button, Text, Tk, ttk

from poly2mono.main import poly2mono


class MyFrame(ttk.Frame):
    def __init__(self, main_window: Tk) -> None:
        super().__init__(main_window)
        ttk.Frame(main_window, padding=10)
        main_window.title("Polytonic to Monotonic Converter")
        main_window.geometry("600x800")

        self.place(x=0, y=0, width=600, height=800)

        print("Initialized interface.")

    def run(self) -> None:
        print("Running...")

        self.input_text = "The polytonic text goes here."
        self.output_text = "You will see the result here."

        label = ttk.Label(self, text="Convert polytonic text to monotonic", font=("Helvetica", 16))
        label.pack(pady=5)

        self.input = Text(self, width=80, height=20)
        self.input.pack(pady=5)
        self.input.insert("1.0", self.input_text)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=5)

        self.convert_button = Button(button_frame, text="Convert", command=self.convert)
        self.convert_button.pack(side=LEFT, padx=5)

        self.copy_button = Button(button_frame, text="Copy", command=self.copy_text)
        self.copy_button.pack(side=LEFT, padx=5)

        self.clear_button = Button(button_frame, text="Clear", command=self.clear_text)
        self.clear_button.pack(side=LEFT, padx=5)

        self.output = Text(self, width=80, height=20)
        self.output.pack(pady=5)
        self.output.insert("1.0", self.output_text)

        self.check_for_interrupt()
        self.mainloop()

        print("Finished.")

    def convert(self) -> None:
        self.input_text = self.input.get("1.0", "end-1c")
        self.output_text = poly2mono(self.input_text)

        self.output.delete("1.0", "end")
        self.output.insert("1.0", self.output_text)

    def copy_text(self) -> None:
        self.output_text = self.output.get("1.0", "end-1c")
        self.clipboard_clear()
        self.clipboard_append(self.output_text)
        self.update()  # Keep the clipboard content after the window is closed

    def clear_text(self) -> None:
        self.input.delete("1.0", "end")
        self.output.delete("1.0", "end")
        self.input_text = ""
        self.output_text = ""

    def check_for_interrupt(self) -> None:
        try:
            self.after(ms=100, func=self.check_for_interrupt)
        except KeyboardInterrupt:
            self.quit()


def main() -> None:
    main_window = Tk()
    MyFrame(main_window).run()


if __name__ == "__main__":
    main()
