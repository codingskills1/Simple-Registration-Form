from tkinter import *
from tkinter.ttk import *
import tkinter as tk 
from tkinter import messagebox

window = Tk()

window.title("Login")

window.geometry("800x800")

number_list = "2 + 2 + 3 + 7 + 8 + 5"
result = 28

# Pictures
canvas = Canvas(window)
img = PhotoImage(file = "contacts.png")
canvas.create_image(0,0, anchor=NW, image = img)
canvas.place(x = 0, y = 146)

canvas_password = Canvas(window)
img_password = PhotoImage(file = "password.png")
canvas_password.create_image(0,0, anchor=NW, image = img)
canvas_password.place(x = 0, y = 260)

# Labels
lbl = Label(window, text = "Registration", background = "black", foreground = "white",font=("Arial Bold",40))
lbl1 = Label(window, text = "Full Name: ",font=("Arial Bold",24))
lbl2 = Label(window, text = "FirstName")
lbl3 = Label(window, text = "LastName")
email = Label(window, text = "Email:", font=("Arial Bold",24))
lbl4 = Label(window, text = "Email")
lbl5 = Label(window, text = "Password")
lbl_age = Label(window, text = "Age:", font=("Arial Bold",24))

# Label Places
lbl.pack(side=TOP)

lbl1.place(x = 10, y =100)

lbl2.place(x = 38, y = 170)

lbl3.place(x = 280, y = 170)

lbl4.place(x = 10,y = 280)

lbl5.place(x = 280, y= 280)

lbl_age.place(x = 10, y = 320)

email.place(x = 10, y = 220)





# SpinBox
spin_state =IntVar()

spin_state.set(36)

spin = Spinbox(window,from_ = 10, to_ = 40, textvariable = spin_state)

spin.place(x = 10,y = 370)


# Entries
entry = Entry(window, width = 40)
entry1 = Entry(window, width = 40)
email_entry = Entry(window, width = 40)
password_entry = Entry(window, width = 40)
entry_valid = Entry(window, width = 8)

entry.focus()

entry.get()

# Entry Places
entry.place(x = 40, y = 150)
entry1.place(x = 300, y = 150)
email_entry.place(x = 10, y = 260)
password_entry.place(x = 280,y = 260)



# Button
def clicked():
	if entry.get() == "":
		messagebox.showerror("Error", "Enter Your name")

	elif len(entry.get()) < 6:
		messagebox.showerror("Error", "Enter Valid Name")

	elif entry.get() == "hhhhhhhhhh" or entry.get() == "aaaaaaaaaa":
		messagebox.showerror("Error", "Please Enter Valid Name")

	elif entry1.get() == "":
		messagebox.showerror("Error", "Enter Your LastName")

	elif len(entry1.get()) < 7:
		messagebox.showerror("Error", "Enter Valid LastName")

	elif email_entry.get() == "":
		messagebox.showerror("Error", "Enter Your Email Address")

	elif len(email_entry.get()) < 4:
		messagebox.showerror("Error", "Enter Valid Email Address")

	elif "@gmail.com" not in email_entry.get() and "@email.com" not in email_entry.get():
		messagebox.showerror("Error", "Please Enter Valid Email Address")

	elif password_entry.get() == "":
		messagebox.showerror("Error","Enter Your password")

	elif len(password_entry.get()) < 7:
		messagebox.showerror("Error", "Lenght of Your password is low")

	elif "@" not in password_entry.get():
		messagebox.showerror("Error", "use @ in your password")

	elif spin.get() == "":
		messagebox.showerror("Error", "Enter Your Age")

	else:
		messagebox.showinfo("Successful", "Registration Completed Successfully")
		quit()

 
btn = tk.Button(window, text = "Registre", background = "white", foreground = "black", width = 5, height = 2, command = clicked)

btn.place(x = 10, y = 460)


window.mainloop()
