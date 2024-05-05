import tkinter as tk
from tkinter.filedialog import askopenfilename
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image
from pyperclip import copy as copy_to_clipboard
from image_chunker import get_image_chunk_rows
from converter import chunks_to_braille, resize_image
from loadfont import loadfont

class OptionsMenu(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Image pick
        self.image = Image.new("RGBA", (30,30), (0,0,0,0))
        self.image_file_name = ""

        self.columnconfigure(0, weight=1)
        self.image_pick_frame = ttk.Frame(self)
        self.image_pick_frame.grid(row=0,column=0,sticky=N+S+W+E)

        self.image_pick_btn = ttk.Button(self.image_pick_frame, text="Open Image", bootstyle=SUCCESS, command=self.pick_image, padding=(15,2))
        self.image_pick_btn.pack(side=LEFT, padx=15,pady=10)
        self.image_pick_lbl = ttk.Label(self.image_pick_frame, bootstyle=INFO, text="No image selected")
        self.image_pick_lbl.pack(side=LEFT, padx=8,pady=10)



        #Copy output
        self.copy_frame = ttk.Frame(self)
        self.copy_frame.grid(row=1,column=0,sticky=N+S+W+E)

        self.copy_btn = ttk.Button(self.copy_frame, text="Copy text", bootstyle=PRIMARY, command=self.master.copy, padding=(22,3))
        self.copy_btn.pack(side=LEFT, padx=15,pady=10)

        self.char_count_lbl = ttk.Label(self.copy_frame, bootstyle=INFO, text="0 characters")
        self.char_count_lbl.pack(side=LEFT, padx=8,pady=10)



        #Options
        self.options = {
            "inverted": False,
            "threshold": 255//2,
            "size": 20
        }

        self.options_frame = ttk.Frame(self)
        self.options_frame.grid(row=2, column=0, sticky=N+S+W+E, pady=(10,0))
        self.rowconfigure(2, weight=1)

        


        #Inverted
        self.inverted = ttk.Checkbutton(master=self.options_frame, text="Inverted", bootstyle=SUCCESS+ROUND+TOGGLE, 
                                        command=lambda:[self.change_option("inverted", not self.options["inverted"]), 
                                                        self.master.update_output()])
        self.inverted.pack(padx=15, pady=(7,15), side=TOP, anchor=N+W)




        #Threshold
        self.threshold_lbl = ttk.Label(self.options_frame, text="Threshold - "+str(self.options["threshold"]))
        self.threshold_lbl.pack(padx=15, side=TOP, anchor=N+W)

        self.threshold_slider = ttk.Scale(master=self.options_frame, bootstyle="info", from_=0, to=255, length=255)
        self.threshold_slider.set(self.options["threshold"])
        self.threshold_slider.config(command=lambda value:[self.change_option("threshold", int(float(value))), 
                                                                self.master.update_output(), 
                                                                self.threshold_lbl.config(text="Threshold - "+str(int(float(value))))])
        self.threshold_slider.pack(padx=15, pady=(3,15), side=TOP, anchor=N+W)



        #Size
        self.size_lbl = ttk.Label(self.options_frame, text="Size - "+str(self.options["size"]))
        self.size_lbl.pack(padx=15, side=TOP, anchor=N+W)

        self.size_slider = ttk.Scale(master=self.options_frame, bootstyle="info", from_=0, to=100, length=255)
        self.size_slider.set(self.options["size"])
        self.size_slider.config(command=lambda value:[self.change_option("size", int(float(value))), 
                                                                self.master.update_output(), 
                                                                self.size_lbl.config(text="Size - "+str(int(float(value))))])
        self.size_slider.pack(padx=15, pady=(3,15), side=TOP, anchor=N+W)
    

    def change_option(self, option, new_value):
        self.options[option] = new_value


    def pick_image(self):
        image_dir = askopenfilename()
        self.image = Image.open(image_dir).convert("RGBA")
        self.image_file_name = image_dir.split("/")[-1]
        self.master.update_output()
        self.image_pick_lbl.config(text=self.image_file_name)
        

class OutputFrame(ttk.ScrolledText):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.config(state=DISABLED)

        self.output = ""
    
    def update_text(self, text):
        self.output = text

        self.config(state=NORMAL)
        self.delete('1.0', END)
        self.insert(INSERT, text)
        self.config(state=DISABLED)


class MainUi(ttk.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Load the custom monospaced font
        loadfont("fonts/Symbola.ttf")

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=10)
        self.rowconfigure(0, weight=1)

        self.options_menu = OptionsMenu(master=self, width=300)
        self.options_menu.grid(row=0, column=0, sticky=N+S+W+E)
        self.options_menu.grid_propagate(False)

        self.output_frame = OutputFrame(master=self, font=("Symbola", ))
        self.output_frame.grid(row=0, column=1, sticky=N+S+W+E)

    def update_output(self):
        options = self.options_menu.options

        image = self.options_menu.image
        image = resize_image(image, options["size"])

        image_chunks = get_image_chunk_rows(image)
        braille_image = chunks_to_braille(image_chunks, inverted=options["inverted"], threshold=options["threshold"])

        self.output_frame.update_text(braille_image)

        self.options_menu.char_count_lbl.config(text=str(len(braille_image.replace("\n", "")))+" characters")

    def copy(self):
        copy_to_clipboard(self.output_frame.output)