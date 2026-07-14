from tkinter import *
from datetime import date

def calculate_age():
    birth_year = int(year_entry.get())
    birth_month = int(month_entry.get())
    birth_day = int(day_entry.get())

    today = date.today()
    age = today.year - birth_year

    if (today.month, today.day) < (birth_month, birth_day):
        age -= 1

    result.config(text="Present Age: " + str(age) + " years")

window = Tk()
window.title("Age Calculator")
window.geometry("300x250")

Label(window, text="Enter Birth Day:").pack()
day_entry = Entry(window)
day_entry.pack()

Label(window, text="Enter Birth Month:").pack()
month_entry = Entry(window)
month_entry.pack()

Label(window, text="Enter Birth Year:").pack()
year_entry = Entry(window)
year_entry.pack()

Button(window, text="Calculate Age", command=calculate_age).pack()

result = Label(window, text="")
result.pack()

window.mainloop()