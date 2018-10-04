from tkinter import *
from tkinter import ttk
import os
import shutil, errno

def premove():
	value = variable.get()
	print(value)
	if value == "SDVX 1 ~ Booth":
		source = r"/~SKINS/1 ~ Booth"
	elif value == "SDVX 2 ~ Infinite Infection":
		source = r"/~SKINS/2 ~ Infinite Infection"
	elif value == "SDVX 3 ~ Gravity Wars":
		source = r"/~SKINS/3 ~ Gravity Wars"
	elif value == "SDVX 4 ~ Heavenly Haven":
		source = r"/~SKINS/4 ~ Heavenly Haven"
	print(source + " was selected properly")
	move(source)

#moves the files
def move(source):
	print(source + " has started moving")
	#if file destination exists, murder it
	print("#########################")
	dirname = os.path.dirname(__file__)
	print(dirname)
	imgs = os.path.join(r"\imgs", dirname)
	print(imgs)
	cache = os.path.join(r"\cache", dirname)
	print(cache)
	se = os.path.join(r"\se", dirname)
	print(se)
	print("#########################")
	shutil.rmtree(imgs)
	shutil.rmtree(cache)
	shutil.rmtree(se)
	#replace file destination
	try:
		shutil.copytree(source, r"C:\Users\minno\Desktop\kshootBACKUP", symlinks=False, ignore=None, copy_function=shutil.copy2, ignore_dangling_symlinks=False)
	except OSError as exc:
		if exc.errno == errno.ENOTDIR:
			shutil.copy(src, dst)
		else: raise
	print(source + " was moved properly")


#main window
root = Tk()
root.title("K-Shoot Mania Skin Swapper")
root.resizable(False, False)

#padding n stuff
mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#force size of 250x25
sizer = ttk.Frame(mainframe, width=250, height=25)

options = [
	"Select one",
	"SDVX 1 ~ Booth",
	"SDVX 2 ~ Infinite Infection",
	"SDVX 3 ~ Gravity Wars",
	"SDVX 4 ~ Heavenly Haven"
]
variable = StringVar(mainframe)
variable.set(options[0])
dropdown = OptionMenu(mainframe, variable, *options)
dropdown.grid(column=1, row=1)

#move button
buttun = ttk.Button(mainframe, text="Move", command=premove).grid(column=0, row=1)

#pads around the items in the window
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#enter event loop (makes everything run)
root.mainloop()