from tkinter import Tk, PhotoImage, Label, Entry, Button, messagebox
import MainForm

def LoginForm():
    global window, txtUsername, txtPassword

    window = Tk()
    window.title("Login Form")
    window.geometry("250x165")
    window.config(background="#880e0e")
    window.resizable(0,0)

    img = PhotoImage(file="login-form-bg.png")
    Label(image=img, bd=0).place(x=75, y=10)
    Label(window, text="Username: ", bg="#880e0e", fg="#ffffff").place(x=30, y=67)
    Label(window, text="Password: ", bg="#880e0e", fg="#ffffff").place(x=30, y=90)

    txtUsername = Entry(window, relief="flat")
    txtUsername.place(x=95, y=65)
    txtPassword = Entry(window, relief="flat", show='*')
    txtPassword.place(x=95, y=90)   

    Button(window, text="Cancel", width=10, relief="flat", command=quit).place(x=45, y=120)
    Button(window, text="Login", width=10, relief="flat",command=loginVerify).place(x=129, y=120)

    window.mainloop()

def loginVerify():

    acc = []
    un = txtUsername.get()
    pwd = txtPassword.get()

    try:
        for line in open('account.txt', 'r'): acc.append(line)
        if un == acc[0].strip() and pwd == acc[1]:
            messagebox.showinfo(title="Login Success", message="Login Successfully")
            window.destroy()
            MainForm.setMainForm()
        else:
            messagebox.showwarning(title="Login Failed", message="Incorrect username or password.")
    except FileNotFoundError:
        messagebox.showerror(title="File Not Found", message="File not found.")
    except IndexError:
        messagebox.showerror(title="Account Not Found", message="Account not found.")
        window.destroy()
        MainForm.setMainForm()
#main
LoginForm()
