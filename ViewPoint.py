import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import subprocess
import os
import webbrowser

def stop_loading_and_open_viewer():
    if hasattr(root, 'progress'):
        root.progress.stop()
    root.destroy()
    open_viewer()

def on_escape(event):
    root.destroy()

def show_loading_screen():
    global root
    root = tk.Tk()
    root.title("ViewPoint - Launching")
    root.attributes('-fullscreen', True)
    root.bind("<Escape>", on_escape)

    frame = tk.Frame(root)
    frame.pack(expand=True)

    label = tk.Label(frame, text="ViewPoint", font=("Arial", 48))
    label.pack(pady=20)

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("blue.Horizontal.TProgressbar", 
                   troughcolor='#f0f0f0', 
                   background='#0078d7')

    progress = ttk.Progressbar(frame, 
                             style="blue.Horizontal.TProgressbar", 
                             orient="horizontal", 
                             length=400, 
                             mode="indeterminate")
    progress.pack(pady=20)
    progress.start(10)

    root.progress = progress

    root.after(10000, stop_loading_and_open_viewer)
    root.mainloop()

def open_file():
    file_types = [
        ("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif"),
        ("All files", "*.*")
    ]
    file_path = filedialog.askopenfilename(filetypes=file_types)
    if not file_path:
        return

    try:
        image = Image.open(file_path)

        width, height = image.size
        ratio = min(800/width, 600/height)
        new_size = (int(width * ratio), int(height * ratio))

        image = image.resize(new_size, Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        if hasattr(viewer_root, 'label'):
            viewer_root.label.config(image=photo)
            viewer_root.label.image = photo
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image:\n{str(e)}")

def go_to_source():
    webbrowser.open("https://github.com/Rainesroom/ViewPoint/blob/main/ViewPoint.py")

def go_to_license():
    webbrowser.open("https://github.com/Rainesroom/ViewPoint/blob/main/LICENSE.md")

def close_program():
    if 'viewer_root' in globals():
        viewer_root.destroy()

def open_viewer():
    global viewer_root
    viewer_root = tk.Tk()
    viewer_root.title("ViewPoint - Picture Viewing Software. Open Source. Free For all.")
    viewer_root.geometry("800x600")

    menu_bar = tk.Menu(viewer_root)
    viewer_root.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=close_program)

    info_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Info", menu=info_menu)
    info_menu.add_command(label="Source Code", command=go_to_source)
    info_menu.add_command(label="License", command=go_to_license)

    label = tk.Label(viewer_root)
    label.pack(fill="both", expand=True)

    viewer_root.label = label

    viewer_root.protocol("WM_DELETE_WINDOW", close_program)
    viewer_root.mainloop()

if __name__ == "__main__":
    show_loading_screen()
