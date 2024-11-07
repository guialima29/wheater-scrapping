from core.wheater import Wheater
from tkinter import *
import tkinter as tk

cc = Wheater()

def process_text(input_text):
    return input_text

def on_button_click():
    user_input = entry.get()

    result = process_text(user_input)

    result_label.config(text=cc.wheater(cc.normalize(result)))


root = tk.Tk()
root.title("Wheater")

entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, pady=10, padx=10)

button = tk.Button(root, text="Submit", command=on_button_click)
button.grid(row=1, column=0, pady=5)

result_label = tk.Label(root, text="", width=40, height=2, bg="lightgray")
result_label.grid(row=2, column=0, pady=10, padx=10)

root.mainloop()