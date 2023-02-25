import csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('Daily Income/Expense')
GUI.geometry('750x400')

dateLabel = Label(GUI, text="Date")
dateLabel.grid(row=1, column=0)
dateInput = ttk.Entry(GUI, width=20)
dateInput.grid(row=2, column=0)

inexLabel = Label(GUI, text="IN/EX")
inexLabel.grid(row=1, column=1)
optionList = ["INCOME", "EXPENSE"]
value_inside = StringVar(GUI)
# Set the default value of the variable
value_inside.set("Select an Option")
inexOption = OptionMenu(GUI, value_inside, *optionList)
inexOption.grid(row=2, column=1)

itemNameLabel = Label(GUI, text="Item Name")
itemNameLabel.grid(row=1, column=2)
itemName = Entry(GUI, width=40)
itemName.grid(row=2, column=2)

amountLabel = Label(GUI, text="Amount")
amountLabel.grid(row=1, column=3)
amount = Entry(GUI, width=30)
amount.grid(row=2, column=3)

###################### CSV################################


def writecsv(datalist):
    with open('data.csv', 'a', encoding='utf-8', newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)
        messagebox.showinfo(f"Added Item Success", datalist)
    readcsv()


def readcsv():
    total = 0
    tree = ttk.Treeview(GUI, column=("c1", "c2", "c3", "c4",
                        "c5"), show='headings', height=8)
    tree.heading("# 1", text="ID")
    tree.column("c1", width=10)
    tree.heading("# 2", text="Date")
    tree.column("c2", width=100)
    tree.heading("# 3", text="IN/EX")
    tree.column("c3", width=100)
    tree.heading("# 4", text="Item Name")
    tree.column("c4", width=300)
    tree.heading("# 5", text="Amount")
    tree.column("c5", width=200)

    tree.grid(row=3, columnspan=5)
    with open('data.csv', encoding='utf-8', newline='') as file:
        fr = csv.DictReader(file)
        index = 0
        for row in fr:
            index = index+1
            date_r = row['date']
            inex_r = row['inex']
            name_r = row['name']
            amount_r = row['amount']
            if(inex_r == 'INCOME'):
              total = total+int(amount_r)
            if(inex_r == 'EXPENSE'):
              total = total-int(amount_r)
            tree.insert("", 0, value=(index, date_r, inex_r, name_r, amount_r))
    totalLabel = Label(GUI, text="Total: ")
    totalLabel.grid(row=5, column=1, columnspan=2)
    totalText = Label(GUI, text=total)
    totalText.grid(row=5, column=2, columnspan=2)
###################### CSV#################################

def addItem():
    date = dateInput.get()
    inex = value_inside.get()
    iname = itemName.get()
    amt = amount.get()
    text = [date, inex, iname, amt]
    writecsv(text)
    dateInput.delete(0,END)
    inexOption = OptionMenu(GUI, value_inside, *optionList)
    itemName.delete(0,END)
    amount.delete(0,END)

addBtn = Button(GUI, text="ADD", command=addItem)
addBtn.grid(row=2, column=4)
readcsv()

GUI.mainloop()
