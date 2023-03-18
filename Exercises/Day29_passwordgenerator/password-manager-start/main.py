import json
import tkinter
from tkinter import messagebox
import json
import pyperclip


# ---------------------------- DATA SEARCH ------------------------------- #
def search_data():
    try:
        with open('data.json') as data_file:
            try:
                s_path = json.load(data_file)[entry_website.get().lower()]
                s_website = entry_website.get()
                s_email = s_path['email']
                s_password = s_path['password']
            except KeyError:
                messagebox.showinfo(title='Error', message='No details for the website exists.')
            else:
                messagebox.showinfo(s_website, f'Email: {s_email}\n Password: {s_password}')
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File found ')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    # Password Generator Project
    import random
    if len(entry_password.get()) != 0:
        entry_password.delete(0, tkinter.END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters= [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = entry_website.get().lower()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }

    if password != '' and email != '' and password != '':

        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email},\nPassword: {password}')

        if is_ok:
            try:
                with open('data.json', mode='r') as data_file:
                    #Reading old Data
                    data = json.load(data_file)
                    #Updating old data with new data
                    data.update(new_data)
            except json.decoder.JSONDecodeError:
                with open('data.json', mode='w') as data_file:
                    #Saving update date
                    json.dump(new_data, data_file, indent=4)
            except FileNotFoundError:
                with open('data.json', mode='w') as data_file:
                    # Saving update date
                    json.dump(new_data, data_file, indent=4)
            else:
                with open('data.json', mode='w') as data_file:
                    # Saving update date
                    json.dump(data, data_file, indent=4)
            finally:
                entry_password.delete(0, tkinter.END)
                entry_website.delete(0, tkinter.END)
    else:
        messagebox.showinfo(title='ALERT', message="Please make sure you haven't left any field empty")


# ---------------------------- UI SETUP ------------------------------- #
#window
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)


#canvas
canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#labels
website = tkinter.Label(text='Website:')
website.grid(column=0, row=1)
email_user = tkinter.Label(text='Email/Username:')
email_user.grid(column=0, row=2)
password = tkinter.Label(text='Password:')
password.grid(column=0, row=3)



#entry
entry_website = tkinter.Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()
entry_email = tkinter.Entry(width=35)
entry_email.insert(0, 'email@hotmail.com')
entry_email.grid(column=1, row=2, columnspan=2)
entry_password = tkinter.Entry(width=35)
entry_password.grid(column=1, row=3, columnspan=2)



#button
button_generate = tkinter.Button(text='Generate Password', command=pass_generator)
button_generate.grid(column=2, row=3, )
button_add = tkinter.Button(text='Add', width=36, command=save_password)
button_add.grid(column=1, row=4, columnspan=2, )
button_search = tkinter.Button(text='search', width=16, command=search_data)
button_search.grid(column=2, row=1)
window.mainloop()