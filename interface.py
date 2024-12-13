import QuiZZZ
import tkinter as tk
from tkinter import ttk

deffont = 'Helvetica'

def changetesttomenu():
    test_frame.pack_forget()
    frame_bottom.pack_forget()
    frame_top.pack_forget()
    intmenu()

def changemenutotest():
    menu_frame.pack_forget()
    intstart()

def changemenutosettings():
    menu_frame.pack_forget()
    settings()

def changesettingstomenu():
    settings_frame.pack_forget()
    intmenu()


def intmenu():
    menu_frame.pack()
    start_label.pack(side=tk.TOP)


    button_frame.pack(side=tk.BOTTOM, pady=150)
    start_button.pack(side=tk.TOP, ipady=20, ipadx=25)
    settings_button.pack(side=tk.TOP, ipady=20, ipadx=25)

def settings():
    settings_frame.pack()
    settings_label.pack()
    settings_button_frame.pack(pady=50)
    settings_radiobutton1.pack()
    settings_radiobutton2.pack()
    settings_radiobutton3.pack()
    settings_ok_button.pack()


def intstart():
    menu_frame.pack_forget()
    test_frame.pack(fill='x')

    test_label.pack(side=tk.TOP, anchor='center')
    menu_button.pack(anchor='ne', ipadx=20, ipady=10)


    frame_bottom.pack(side=tk.BOTTOM, anchor='center')
    frame_top.pack(side=tk.BOTTOM, anchor='center')


    test_button_1.pack(side=tk.LEFT, anchor='center', fill='x', ipadx=100, ipady=20)
    test_button_2.pack(side=tk.LEFT, anchor='center', fill='x', ipadx=100, ipady=20)
    test_button_3.pack(side=tk.LEFT, anchor='center', fill='x', ipadx=100, ipady=20)
    test_button_4.pack(side=tk.LEFT, anchor='center', fill='x', ipadx=100, ipady=20)


window = tk.Tk()
window.title("Quizzz")
window.geometry('640x480')

##All intmenu wingets
menu_frame = tk.Frame(window)
button_frame = tk.Frame(menu_frame,  bg='red')
start_label = ttk.Label(menu_frame, text='Добро пожаловать', font=(deffont, 20))
start_button = ttk.Button(button_frame, text='Начать тест', command=changemenutotest)
settings_button = ttk.Button(button_frame, text='Настройки', command=changemenutosettings)

##All settings widgets
settings_frame = tk.Frame(window)
settings_label = ttk.Label(settings_frame, text='Режим перевода', font=(deffont, 20))
settings_button_frame = tk.Frame(settings_frame)
settings_radiobutton1 = tk.Radiobutton(settings_button_frame, text='Английский - Русский')
settings_radiobutton2 = tk.Radiobutton(settings_button_frame, text='Русский - Английский')
settings_radiobutton3 = tk.Radiobutton(settings_button_frame, text='Случайно')
settings_ok_button = ttk.Button(settings_button_frame, text='OK', command=changesettingstomenu)


#All intstart wingets
var1, var2, var3, var4 = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
test_frame = tk.Frame()
test_label = ttk.Label(test_frame, text="Выберите правильный перевод слова", font=(deffont, 20))
frame_bottom = tk.Frame(window)
frame_top = tk.Frame(window)
test_button_1 = ttk.Button(frame_top, textvariable=var1)
test_button_2 = ttk.Button(frame_top, textvariable=var2)
test_button_3 = ttk.Button(frame_bottom, textvariable=var3)
test_button_4 = ttk.Button(frame_bottom, textvariable=var4)
menu_button = ttk.Button(test_frame, text='Menu', command=changetesttomenu)

window.minsize(640,480)
# window.maxsize(640,480)
intmenu()
window.mainloop()

