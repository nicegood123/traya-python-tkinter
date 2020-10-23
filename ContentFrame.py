from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ButtonsFrame, InfoFrame, TopFrame

def setContentFrame():
	global athletelist_tv

	contentFrame = Frame(width="585", height="318", bg="#cc9090")
	contentFrame.place(x=245, y=50)
	athletelistForm = LabelFrame(contentFrame,
								 width="575",
								 height="308",
								 text="List of Athletes",
								 bg="#cc9090")
	athletelistForm.place(x=5, y=5)

	headings = ("ID", "Full Name", "Age", "Birth Date", "Gender", "Course", "Year Level", "Sport")

	athletelist_tv = ttk.Treeview(athletelistForm, columns=headings, show="headings")

	vertical_scrollbar = ttk.Scrollbar(athletelist_tv, orient="vertical")
	vertical_scrollbar.config(command=athletelist_tv.yview)
	horizontal_scrollbar = ttk.Scrollbar(athletelist_tv, orient="horizontal")
	horizontal_scrollbar.config(command=athletelist_tv.xview)

	athletelist_tv.config(yscrollcommand=vertical_scrollbar.set,
						  xscrollcommand=horizontal_scrollbar.set)

	vertical_scrollbar.pack(side=RIGHT, fill=Y)
	horizontal_scrollbar.pack(side=BOTTOM, fill=X)

	for heading in headings: athletelist_tv.heading(heading, text=heading)

	athletelist_tv.column(0, width=40, minwidth=40, stretch=NO)
	athletelist_tv.column(1, width=130, minwidth=100, stretch=NO)
	athletelist_tv.column(2, width=30, minwidth=30, stretch=NO)
	athletelist_tv.column(3, width=65, minwidth=65, stretch=NO)
	athletelist_tv.column(4, width=55, minwidth=55, stretch=NO)
	athletelist_tv.column(5, width=50, minwidth=50, stretch=NO)
	athletelist_tv.column(6, width=68,minwidth=68, stretch=NO)
	athletelist_tv.column(7, width=90, minwidth=90, stretch=NO)
	athletelist_tv.place(x=13, y=5, width=545, height=275)
	athletelist_tv.bind("<ButtonRelease-1>", selectedRow)
	viewList()

def selectedRow(self):
	try:
		global info
		info = []
		selected_row = athletelist_tv.selection()
		values = athletelist_tv.item(selected_row,"values")
		for val in values: info.append(val)

		ButtonsFrame.showButtonUpdate()
		InfoFrame.setValues()
	except IndexError: pass

def getLastIndex():
	for i in athletelist_tv.get_children():
		temp = athletelist_tv.item(i)["values"]
		for val in temp:
			lastIndex = val
			break
	return lastIndex
def save():
	global id

	id = getLastIndex() + 1
	InfoFrame.setID(str(id + 1))
	InfoFrame.getValues()
	get_info = InfoFrame.get_info

	athletelist_tv.insert("", "end", values=(id, get_info[1], get_info[2], get_info[3], get_info[4], get_info[5], get_info[6], get_info[7]))
	saveToTextFile()

def update():
	InfoFrame.getValues()
	get_info = InfoFrame.get_info
	selected_row = athletelist_tv.selection()
	athletelist_tv.item(selected_row, values=(get_info[0], get_info[1], get_info[2], get_info[3], get_info[4], get_info[5], get_info[6], get_info[7]))
	saveToTextFile()

def delete():
	try:
		selected_row = athletelist_tv.selection()[0]
		athletelist_tv.delete(selected_row)	
		saveToTextFile()
	except IndexError: 
		messagebox.showwarning(message="Select athlete to delete.")

def clear():
        try:
                InfoFrame.clearValues()
                ButtonsFrame.showButtonSave()
        except: pass

def saveToTextFile():
	athlete_list = []
	hold = ""

	for i in athletelist_tv.get_children():
		temp = athletelist_tv.item(i)["values"]
		for val in temp: hold += str(val) + "#"
		athlete_list.append(hold)
		hold = ""

	with open('AthleteList.txt', 'w') as file_write:
		for i in range(len(athlete_list)):
			file_write.write(athlete_list[i] + "\n")

def addRow(list):

	for i in range(len(list)):
		info = list[i].split("#")
		view = []
		for val in info: view.append(val)
		athletelist_tv.insert("", "end", values=(view[0], view[1], view[2], view[3], view[4], view[5], view[6], view[7]))
	return list

def viewList():
	athlete_list = []
	
	for data in open('AthleteList.txt'): athlete_list.append(data)
	addRow(athlete_list)

def clearList():
	data = athletelist_tv.get_children()
	athletelist_tv.delete(*data)

def search():
	clearList()
	athlete_list = []
	search = TopFrame.val_search

	for data in open('AthleteList.txt'):
		if search.lower() in data.lower():
			athlete_list.append(data)

	addRow(athlete_list)
