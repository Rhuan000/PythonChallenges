import tkinter

#window
window = tkinter.Tk()
window.title('Mile to Km converter')
window.maxsize(width=250, height=120)
window.config(padx=20, pady=20)

#entry
input = tkinter.Entry(width=10)
input.insert(index=int(), string='0')
input.grid(column=1, row=0)

#mile_to_Km function
def mile_km():
    mile = int(input.get())
    km = mile * 1.609
    start_lebel.config(text=km)


#calculate buttom.
calculate = tkinter.Button(text='calculate', command=mile_km)
calculate.grid(column=1,row=3)

#labels
miles = tkinter.Label(text='miles')
is_equal = tkinter.Label(text='is equal to')
start_lebel = tkinter.Label(text=input.get())
km = tkinter.Label(text='Km')
miles.grid(column=2, row=0)
is_equal.grid(column=0, row=1)
start_lebel.grid(column=1, row=1)
km.grid(column=2, row=1)

window.mainloop()