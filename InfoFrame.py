from tkinter import *
from tkinter import ttk
import ButtonsFrame, ContentFrame

def setInfoFrame():

	global course, year_level, sports
	global get_gender, get_course, get_year_level, get_sport
	global txtID, txtName, txtAge, txtBirthdate, rbMale, rbFemale, cboxCourse, cboxYearLevel, cboxSport

	infoFrame = Frame(width="230", height="230", bg="#cc9090")
	infoFrame.place(x=10, y=70)
	infoForm = LabelFrame(infoFrame,width="220",
									height="220",
									text="Athlete Information Form",
									bg="#cc9090")
	infoForm.place(x=5, y=5)
	#------------------------------------------------------------------#
	Label(infoForm, text="ID: ", bg="#cc9090").place(x=8, y=16)
	Label(infoForm, text="Name: ", bg="#cc9090").place(x=8, y=39)
	Label(infoForm, text="Age: ", bg="#cc9090").place(x=8, y=62)
	Label(infoForm, text="Birthdate: ", bg="#cc9090").place(x=8, y=85)
	Label(infoForm, text="Gender: ", bg="#cc9090").place(x=8, y=109)
	Label(infoForm, text="Course: ", bg="#cc9090").place(x=8, y=132)
	Label(infoForm, text="Year Level: ", bg="#cc9090").place(x=8, y=152)
	Label(infoForm, text="Sport: ", bg="#cc9090").place(x=8, y=172)
	#------------------------------------------------------------------#
	row_count = len(open('AthleteList.txt').readlines())

	set_ID = StringVar(value=row_count + 1)
	get_gender = StringVar()
	get_course = StringVar()
	get_year_level = StringVar()
	get_sport = StringVar()
	#------------------------------------------------------------------#
	txtID = Entry(infoForm, width=18, relief="flat", textvariable=set_ID)
	txtID.place(x=72, y=14)
	txtName = Entry(infoForm, width=18, relief="flat")
	txtName.place(x=72, y=37)
	txtAge = Entry(infoForm, width=18, relief="flat")
	txtAge.place(x=72, y=60)
	txtBirthdate = Entry(infoForm, width=18, relief="flat")
	txtBirthdate.place(x=72, y=83)
	#------------------------------------------------------------------#
	rbMale = Radiobutton(infoForm,text="Male",
						value="Male",
						bg="#cc9090",
						activebackground="#880e0e",
						highlightbackground="#cc9090",
						variable=get_gender)
	rbMale.place(x=72, y=109)

	rbFemale = Radiobutton(infoForm,text="Female",
						value="Female",
						bg="#cc9090",
						activebackground="#880e0e",
						highlightbackground="#cc9090",
						variable=get_gender)
	rbFemale.place(x=130, y=109)
	#------------------------------------------------------------------#
	course = ["BSCS", "BSIT", "BLIS", "BSIS"]
	cboxCourse = ttk.Combobox(infoForm,
						width=15,
						state="readonly",
						values=course,
						textvariable=get_course)
	cboxCourse.set("Select")
	cboxCourse.place(x=77, y=132)

	year_level = ["1st Year", "2nd Year", "3rd Year", "4th Year"]
	cboxYearLevel = ttk.Combobox(infoForm,
						width=15,
						state="readonly",
						values=year_level,
						textvariable=get_year_level)
	cboxYearLevel.set("Select")
	cboxYearLevel.place(x=77, y=152)

	sports = ["Sepak Takraw", "Volleyball", "Basketball", "Badminton"]
	cboxSport = ttk.Combobox(infoForm, 
						width=15,
						state="readonly",
						values=sports,
						textvariable=get_sport)
	cboxSport.set("Select")
	cboxSport.place(x=77, y=172)
	#------------------------------------------------------------------#

#Methods

def setID(text):
	txtID.delete(0, END)
	txtID.insert(0, text)
	return

def getValues():
	global get_info

	id = txtID.get()
	name = txtName.get()
	age = txtAge.get()
	birthdate = txtBirthdate.get()
	gender = get_gender.get()
	course = get_course.get()
	year_level = get_year_level.get()
	sport = get_sport.get()

	get_info = [id, name, age, birthdate, gender, course, year_level, sport]

def setValues():
	info = ContentFrame.info

	txtID.delete(0, END)
	txtID.insert(0, info[0])
	txtName.delete(0, END)
	txtName.insert(0, info[1])
	txtAge.delete(0, END)
	txtAge.insert(0, info[2])
	txtBirthdate.delete(0, END)
	txtBirthdate.insert(0, info[3])

	if info[4] == "Male": rbMale.invoke()
	elif info[4] == "Female": rbFemale.invoke()

	for i in range(len(course)):
		if course[i] == info[5]:
			cboxCourse.set(course[i])

	for i in range(len(year_level)):
		if year_level[i] == info[6]:
			cboxYearLevel.set(year_level[i])

	for i in range(len(sports)):
		if sports[i] == info[7]:
			cboxSport.set(sports[i])

def clearValues():
	id = ContentFrame.getLastIndex()

	txtID.delete(0, END)
	txtID.insert(0, id + 1)
	txtName.delete(0, END)
	txtAge.delete(0, END)
	txtBirthdate.delete(0, END)
	cboxCourse.set("Select")
	cboxYearLevel.set("Select")
	cboxSport.set("Select")
