from tkinter import *
from tkinter import ttk
import os
import shutil, errno

#ToDO: FIX THE PROBLEM THAT KEEPS HAPPENING

def premove():
	value = variable.get()
	print(value)
	if value == "SDVX 1 ~ Booth":
		source = r"~SKINS\Booth"
	elif value == "SDVX 2 ~ Infinite Infection":
		source = r"~SKINS\Infinite Infection"
	elif value == "SDVX 3 ~ Gravity Wars":
		source = r"~SKINS\Gravity Wars"
	elif value == "SDVX 4 ~ Heavenly Haven":
		source = r"~SKINS\Heavenly Haven"
	print(source + " was selected properly")
	move(source)

#moves the files
def move(source):
	print(source + " has started moving")

	print("#########################")

	#kshoot folder
	dirname = os.path.dirname(__file__)
	print(dirname + " is dirname")

	#skin folder
	source = os.path.join(dirname, source)
	print(source + " is source")

	#images folder
	imgs = os.path.join(dirname, "imgs")
	print(imgs + " is imgs")

	#cache folder
	cache = os.path.join(dirname, "cache")
	print(cache + " is cache")

	#se folder
	se = os.path.join(dirname, "se")
	print(se + " is se")
	print("#########################")

    #kill images
	if(os.path.exists(imgs)):
		shutil.rmtree(imgs)

	#kill cache
	if(os.path.exists(cache)):
		shutil.rmtree(cache)

    #kill sound effects
	if(os.path.exists(se)):
		shutil.rmtree(se)
	print("Folders were killed properly")
	#replace file destination
	try:
		shutil.copytree(source, dirname, symlinks=False, ignore=None, copy_function=shutil.copy2, ignore_dangling_symlinks=False)
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