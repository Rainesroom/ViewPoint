import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ViewPoint")
root.geometry("400x200")

label = tk.Label(root, text="ViewPoint", font=("Arial", 24))
label.pack(pady=20)

style = ttk.Style()
style.configure("blue.Horizontal.TProgressbar", troughcolor="white", background="blue", lightcolor="blue", darkcolor="blue")

progress = ttk.Progressbar(root, style="blue.Horizontal.TProgressbar", orient="horizontal", length=300, mode="indeterminate")
progress.pack(pady=10)

progress.start(10)

root.mainloop()
