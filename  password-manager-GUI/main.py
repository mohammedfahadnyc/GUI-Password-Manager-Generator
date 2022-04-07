import pandas
from tkinter import *
from tkinter import messagebox
import password_generator
import pyperclip
import json
FONT= ("Aerial",15,"normal")


window = Tk()
window.title("Welcome to Password Manager")
window.config(padx=50,pady=50)


def add_password():
    email = email_entry.get()
    password = password_entry.get()
    website = website_entry.get()
    new_data = {
        website.lower() : {
            "email" : email,
            "password" : password
        }
    }
    if len(password) <= 0 or len(email)  <= 0 :
        messagebox.showerror(title="Invalid Data",message="Please Enter Missing Data")
    else :
        # save = messagebox.askokcancel(title="Confrim",message=f"Email is {email}, password is {password}")
        try :
            with open(file="passwords.json", mode="r") as read_json :
                latest_data = json.load(read_json)
                latest_data.update(new_data)
        except :
            with open(file="passwords.json", mode="w") as write_json :
                json.dump(new_data,write_json,indent=4)
        else :
            with open(file="passwords.json",mode="w") as update_json :
                json.dump(latest_data,update_json,indent=4)
            website_entry.delete(0,END)
            password_entry.delete(0,END)


def generate_password():
    password = password_generator.generate_random_password()
    password_entry.insert(0,password)
    pyperclip.copy(password)


def search_password():
        try :
            with open(file="passwords.json", mode="r") as search_data:
                dict = json.load(search_data)
                website = website_entry.get().lower()
            database_email = dict[website]["email"]
            database_password = dict[website]["password"]
        except FileNotFoundError as file_not_found :
            messagebox.showerror(title="Error!",message="No Data Found")
        except KeyError as error :
            messagebox.showerror(title="Error!",message="Website data not Saved")
        else :
            messagebox.showinfo(title="Found!",message=f"For {website} : \n Email is {database_email},\npassword is {database_password}")


image = PhotoImage(file="logo.png")
canvas = Canvas(height=200,width=200)
logo = canvas.create_image(100,100,image=image)
canvas.grid(row=0,column=1)

website_label = Label(text="Website :",font=FONT)
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username :",font=FONT)
email_label.grid(row=2,column=0)

password_label = Label(text="Password:",font=FONT)
password_label.grid(row=3,column=0)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1,column=1)

email_entry = Entry(width=35)
email_entry.insert(0,"exampleemail.com")
email_entry.grid(row=2,column=1,columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)


password_button = Button(text="Generate Password",command=generate_password)
password_button.grid(row=3,column=2)

search_button = Button(text="Find Password",command=search_password,width=13)
search_button.grid(row=1,column=2)

add_button = Button(text="Add",width=36,command=add_password)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()


