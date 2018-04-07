# Chandler Supple, 4/7/2018, 3:21 AM
# Developed for Python 2.7

from Tkinter import *
import ttk

root = Tk()

global x
x = 0
def main():
    root.geometry('500x350')
    root.title('Report an Issue')
    root.config(bg = 'black')
        
    back = Canvas(root, height = 330, width = 480)
    back.config(bg = 'black')
    back.pack(pady = 10, padx = 1)

    name_ = Label(back, text = 'Name: ', font = (20))
    name_.config(bg = 'black', fg = 'white')
    name_.place(x = 20, y = 20)
    buisness_ = Label(back, text = 'Buisness: ', font = (20))    
    buisness_.config(bg = 'black', fg = 'white')
    buisness_.place(x = 20, y = 60)
    email_ = Label(back, text = 'Email: ', font = (20))
    email_.config(bg = 'black', fg = 'white')
    email_.place(x = 20, y = 100)
    issue_ = Label(back, text = 'Issue: ', font = (20))
    issue_.config(bg = 'black', fg = 'white')
    issue_.place(x = 20, y = 140)

    name = ttk.Entry(back, width = 42, font=('Courier New', 10))
    name.place(x = 120, y = 20)
    buisness = ttk.Entry(back, width = 42, font=('Courier New', 10))
    buisness.place(x = 120, y = 60)
    email = ttk.Entry(back, width = 42, font=('Courier New', 10))
    email.place(x = 120, y = 100)
    issue = Text(back, width = 42, height = 8)
    issue.place(x = 120, y = 143)

    global name_m
    global buisness_m
    global email_m
    global issue_m
    name_m = []
    buisness_m = []
    email_m = []
    issue_m = []
    sum_m = []

    def callback():
        n = name.get()
        b = buisness.get()
        e = email.get()
        i = issue.get("1.0",'end-1c')
        global x
        name_m.append(n)
        buisness_m.append(b)
        email_m.append(e)
        issue_m.append(i)
        x_ = str(x)
        sum_ = n + ', ' + b + ', ' +  e + ', ' + i 
        sum_m.append(sum_)
        print(sum_m[x])
        root.destroy()

    send = Button(back, text="Send", width=10, bg = 'black', fg = 'white', command=callback)
    send.place(x = 250, y = 290)
        
main()
root.mainloop()
