# import QuiZZZ
import tkinter as tk
from tkinter import ttk

deffont = 'Helvetica'
btnfont = ('Helvetica', 5)


def menu():
    global menufrm
    menufrm = tk.Frame(window)
    menufrm.pack()
    startlbl = ttk.Label(menufrm, text='Добро пожаловать', font=(deffont, 20))
    startlbl.pack(side=tk.TOP)
    startbtn = ttk.Button(menufrm, text='Начать тест', command=start)
    startbtn.pack(side=tk.BOTTOM, pady=50, ipady=20, ipadx=20)


def start():
    global frm_top, frm_bottom
    menufrm.destroy()
    testfrm = tk.Frame()
    testfrm.pack()
    testlbl = ttk.Label(window, text="Выберите правильный ответ", font=(deffont, 20))
    testlbl.place(relx=0.5, rely=0.1, anchor='center')

    frm_btm = tk.Frame(window)
    frm_btm.pack(side=tk.BOTTOM, anchor='center')

    frm_top = tk.Frame(window)
    frm_top.pack(side=tk.BOTTOM, anchor='center')

    btn1 = ttk.Button(frm_top, text='Вариант 1')
    btn1.pack(side=tk.LEFT, anchor='center', fill='x', ipadx=100, ipady=20)
    
    btn2 = ttk.Button(frm_top, text='Вариант 2')
    btn2.pack(side=tk.LEFT, anchor='center', fill='x', ipadx=100, ipady=20)

    btn3 = ttk.Button(frm_btm, text='Вариант 3')
    btn3.pack(side=tk.LEFT, anchor='center', fill='x', ipadx=100, ipady=20)

    btn4 = ttk.Button(frm_btm, text='Вариант 4')
    btn4.pack(side=tk.LEFT, anchor='center', fill='x', ipadx=100, ipady=20) 

window = tk.Tk()
window.title("Quizzz")
window.geometry('640x480')
window.minsize(640,480)
window.maxsize(640,480)
menu()
window.mainloop()
