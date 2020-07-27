from tkinter import *

window=Tk()

def km_to_miles():
    miles = float(e1_value.get())*1.6
    t1.insert(END, str(miles) + " miles")
    meters = float(e1_value.get())*1000
    t2.insert(END, str(meters) + " m")
    cm = float(e1_value.get()) * 100000
    t3.insert(END, str(cm) + " cm")

b1=Button(window, text="Convert", command=km_to_miles)
b1.grid(row=0, column=2)

e2=Label(window,text="Km")
e2.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value);
e1.grid(row=0, column=1)

t1=Text(window, height=1, width=20)
t1.grid(row=1,column=0)

t2=Text(window, height=1, width=20)
t2.grid(row=1,column=1)

t3=Text(window, height=1, width=20)
t3.grid(row=1,column=2)

window.mainloop()
