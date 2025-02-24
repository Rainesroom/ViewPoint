import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("800x600")
root.title("ViewPoint - Picture Viewing Software. Open Source. Free For all.")
Default_Image = Image.open('Default_ViewPoint_Image.jpg')
Default_Image = Default_Image.resize((800, 600), Image.Resampling.LANCZOS)

Default = ImageTk.PhotoImage(Default_Image)

label = tk.Label(root, image=Default)
label.pack(fill="both", expand=True)

root.mainloop()
