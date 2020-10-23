from tkinter import Frame, Label, Entry, Button, StringVar
import ContentFrame

def setTopFrame():
	topFrame = Frame(width="585", height="35", bg="#cc9090")
	topFrame.place(x=245, y=10)

	Label(topFrame, text="Search", padx=15, pady=2, bg="#cec2c2").place(x=7, y=6)

	global get_value
	get_value = StringVar()

	txtSearch = Entry(topFrame, width=29, bd=3, relief="flat", textvariable=get_value)
	txtSearch.bind("<KeyRelease>", onKeyRelease)
	txtSearch.place(x=76, y=6)

	btnClose = Button(topFrame, text="Close", width=8, relief="flat", command=quit)
	btnClose.place(x=512, y=5)

def onKeyRelease(self):
	global val_search
	val_search = get_value.get()
	ContentFrame.search()
