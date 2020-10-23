from tkinter import Frame, Button
import InfoFrame, ContentFrame

def setButtonsFrame():
	buttonsFrame = Frame(width="230", height="63", bg="#cc9090")
	buttonsFrame.place(x=10, y=305)

	global btnSave, btnUpdate, btnDelete, btnClear
	btnSave = Button(buttonsFrame, text="Save", width=14, relief="flat", command=ContentFrame.save)
	btnSave.place(x=6, y=4)

	btnUpdate = Button(buttonsFrame, text="Update", width=14, relief="flat", state='disabled', command=ContentFrame.update)
	btnUpdate.place(x=117, y=4)

	btnDelete = Button(buttonsFrame, text="Delete", width=14, relief="flat", state='disabled', command=ContentFrame.delete)
	btnDelete.place(x=6, y=33)

	btnClear = Button(buttonsFrame, text="Clear", width=14, relief="flat", state='disabled', command=ContentFrame.clear)
	btnClear.place(x=117, y=33)
	btnClear.lower()

def showButtonSave():
	btnSave.config(state='normal')
	btnUpdate.config(state='disabled')
	btnDelete.config(state='disabled')
	

def showButtonUpdate():
	btnUpdate.config(state='normal')
	btnDelete.config(state='normal')
	btnClear.config(state='normal')
	btnSave.config(state='disabled')

