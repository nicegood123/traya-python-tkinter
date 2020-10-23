from tkinter import Frame, PhotoImage

def setLogoFrame():
	logoFrame = Frame(width="245", height="70", bg="#880e0e")
	logoFrame.place(x=0, y=1)

	img_logo = PhotoImage(file="umlogo.png")
	lblLogo = Label(logoFrame, image=img_logo, bd=0)
	lblLogo.place(x=43, y=5)