from tkinter import Tk, Frame, PhotoImage, Label
import InfoFrame, TopFrame, ButtonsFrame, ContentFrame

def setMainForm():
	window = Tk()
	window.title("Athlete Information System")
	window.configure(background="#880e0e", width=840, height=375)
	window.resizable(0,0)

	logoFrame = Frame(window, width="245", height="70", bg="#880e0e")
	logoFrame.place(x=0, y=1)

	img_logo = PhotoImage(file="umlogo.png")
	Label(logoFrame, image=img_logo, bd=0).place(x=43, y=5)

	InfoFrame.setInfoFrame()
	TopFrame.setTopFrame()
	ButtonsFrame.setButtonsFrame()
	ContentFrame.setContentFrame()

	window.mainloop()

#a56868
#880e0e
#0a101a
