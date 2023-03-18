import tkinter

window = tkinter.Tk()

window.title('my first Gui application')
window.minsize(width=500, height=400)
window.config(padx=20, pady=20)


#label
label = tkinter.Label(text="I am a label", font=('Arial', 24, "bold"))
label.grid(column=0, row=0) #with this command just pack all the stuff from top to bottom. label.pack()
label.config(pady=50, padx=50)

#button
def i_was_clicked():
    new_text = entry.get()
    label.config(text=new_text)

button = tkinter.Button(text="i'm a button", command=i_was_clicked)
button.grid(column=1, row=1)#with this command i can specify the x and y cordenation in the gui. button.place(x=0,y=0)

new_button = tkinter.Button(text='new button')
new_button.grid(column=2, row=0)

#entry
entry = tkinter.Entry()
entry.grid(column=3, row=2)#this command i need to preenche from 0,0 to 1,1 then 2,2 if not have any object in 0,0 but
#i want to put in 1,1 the object will remain in 0,0


window.mainloop()