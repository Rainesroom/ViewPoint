import tkinter as tk
import os
from PIL import Image, ImageTk

current_dir = os.path.dirname(os.path.abspath(__file__)) # Get the install loaction
Default_Image_Path = os.path.join(current_dir, "Default_ViewPoint_Image.jpg") # Connect it to the image.

root = tk.Tk()
root.geometry("800x600")
root.title("ViewPoint - Picture Viewing Software. Open Source. Free For all.")
Default_Image = Image.open(Default_Image_Path)
Default_Image = Default_Image.resize((800, 600), Image.Resampling.LANCZOS)

Default = ImageTk.PhotoImage(Default_Image)

label = tk.Label(root, image=Default)
label.pack(fill="both", expand=True)

root.mainloop()
