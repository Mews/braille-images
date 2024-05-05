import tkinter as tk
import pyglet
from tkextrafont import Font
from loadfont import loadfont

#pyglet.font.add_file("C:\\Users\\Public\\codg\\braille images\\unifont.ttf")
#pyglet.font.add_file("eversonmono.ttf")
loadfont("eversonmono.ttf")

root = tk.Tk()

lbl = tk.Label(root, text="test")
lbl.pack()

lbl2 = tk.Label(root, text="test", font="unifont")
lbl2.pack()

lbl3 = tk.Label(root, text="test", font="bahahyidgwajhdfgsjgh")
lbl3.pack()

lbl4 = tk.Label(root, text="test", font=("Everson Mono", ))
lbl4.pack()

root.mainloop()