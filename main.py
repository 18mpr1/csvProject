from tkinter import *
import csv

root = Tk()

# Labels
label_1 = Label(root,text="First Name")
label_2 = Label(root,text="Last Name")
label_3 = Label(root,text="Email")
label_4 = Label(root,text="Student Number")

# User input
entry_1 = Entry(root)
entry_2 = Entry(root)
entry_3 = Entry(root)
entry_4 = Entry(root)

# Display
label_1.grid(row=0,sticky=E)
label_2.grid(row=1,sticky=E)
label_3.grid(row=2,sticky=E)
label_4.grid(row=3,sticky=E)

entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)
entry_3.grid(row=2,column=1)
entry_4.grid(row=3,column=1)

def onclick():
    print("Button clicked")
    entries = [entry_1.get(),entry_1.get(),entry_1.get(),entry_1.get()]
    return entries

# Buttons
button1 = Button(text="Submit",fg="green",command=onclick)
button1.grid(row=4,column=2)

# CSV
with open('names.csv','a') as csvfile:
    fieldnames = {"First Name","Last Name","Email",'Student Number'}
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"First Name": entries[0],"Last Name": entries[1],"Email": entries[2],"Student Number": entries[3]})

root.mainloop()
