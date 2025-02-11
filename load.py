import tkinter as tk
from tkinter import ttk
import threading
import subprocess

def stop_loading_and_open_viewer():
    progress.stop()
    root.destroy()
    subprocess.run(["python", "viewer.py"])

root = tk.Tk()
root.title("ViewPoint")
root.attributes('-fullscreen', True)

label = tk.Label(root, text="ViewPoint", font=("Arial", 48))
label.pack(expand=True)

style = ttk.Style()
style.theme_use('clam')
style.configure("blue.Horizontal.TProgressbar", troughcolor='#f0f0f0', background='#0078d7', thickness=30)

progress = ttk.Progressbar(root, style="blue.Horizontal.TProgressbar", orient="horizontal", length=400, mode="indeterminate")
progress.pack(pady=20)

progress.start(10)

threading.Timer(10, stop_loading_and_open_viewer).start()

root.mainloop()
