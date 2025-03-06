import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import subprocess
import os

def stop_loading_and_open_viewer():
    progress.stop()
    root.destroy()
    open_viewer()

def on_escape(event):
    root.destroy()

def show_loading_screen():
    global root, progress
    root = tk.Tk()
    root.title("ViewPoint - Launching")
    root.attributes('-fullscreen', True)

    root.bind("<Escape>", on_escape)

    label = tk.Label(root, text="ViewPoint", font=("Arial", 48))
    label.pack(expand=True)

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("blue.Horizontal.TProgressbar", troughcolor='#f0f0f0', background='#0078d7')

    progress = ttk.Progressbar(root, style="blue.Horizontal.TProgressbar", orient="horizontal", length=400, mode="indeterminate")
    progress.pack(pady=20)

    progress.start(10)

    root.after(10000, stop_loading_and_open_viewer)

    root.mainloop()

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        image = Image.open(file_path)
        image = image.resize((800, 600), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo  

def close_program():
    viewer_root.quit()

def open_viewer():
    global viewer_root, label
    viewer_root = tk.Tk()
    viewer_root.geometry("800x600")
    viewer_root.title("ViewPoint - Picture Viewing Software. Open Source. Free For all.")

    menu_bar = tk.Menu(viewer_root)
    viewer_root.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=close_program)

    label = tk.Label(viewer_root)
    label.pack(fill="both", expand=True)

    viewer_root.mainloop()

if __name__ == "__main__":
    show_loading_screen()
