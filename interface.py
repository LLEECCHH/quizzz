import QuiZZZ
import random
import tkinter as tk
from tkinter import ttk

deffont = 'Helvetica'
QuiZZZ.complexity_and_topic('A1', 'природа')


def changetesttomenu():
    global questionnumber
    test_frame.pack_forget()
    frame_bottom.pack_forget()
    frame_top.pack_forget()
    questionnumber = 0
    menu()
def changemenutotest():
    menu_frame.pack_forget()
    start()
def changemenutosettings():
    menu_frame.pack_forget()
    settings()
def changesettingstomenu():
    settings_frame.pack_forget()
    if test_mode.get() == 'Случайно':
        test_mode.set(value=random.choice(('Английский - Русский', 'Русский - Английский')))
    # print(test_complexity.get(), test_theme.get(), test_mode.get())
    QuiZZZ.complexity_and_topic(test_complexity.get(), test_theme.get())
    menu()
def changemenutodict():
    menu_frame.pack_forget()
    dictionary()
def changedicttomenu():
    dict_frame.pack_forget()
    menu()
def changeendtomenu():
    end_screen_frame.pack_forget()
    menu()
"""Функции для переключения между окнами"""


def menu():
    '''Функция отрисовки всех виджетов для главного меню'''
    menu_frame.pack()
    start_label.pack(side=tk.TOP)
    menu_buttom_frame.pack(side=tk.BOTTOM, pady=100)
    start_button.pack(side=tk.TOP, ipady=20, ipadx=50)
    dictionary_button.pack(ipady=20, ipadx=50)
    settings_button.pack(side=tk.TOP, ipady=20, ipadx=50)


def dictionary():
    '''Функция отрисовки всех виджетов для словаря'''
    dict_frame.pack(fill='both')
    dict_label.pack()
    dict_scroll.pack(side=tk.RIGHT, fill='y')
    dict_listbox.pack(fill='both', ipady=100)
    dict_button_frame.pack(side=tk.BOTTOM, anchor='s')
    dict_back_button.pack(pady=10, ipadx=10, ipady=5)

def settings():
    '''Функция отрисовки всех виджетов для настроек'''
    settings_frame.pack()
    settings_main_label.pack()

    settings_button_frame.pack(pady=10)
    settings_mode_label.pack(side=tk.TOP)

    settings_radiobutton1.pack(pady=3)
    settings_radiobutton2.pack(pady=3)
    settings_radiobutton3.pack(pady=3, side=tk.LEFT)

    settings_button_frame2.pack(pady=10)
    settings_comp_label.pack()
    settings_combobox1.pack()
    settings_theme_label.pack()
    settings_combobox2.pack()
    settings_count_label.pack()
    settings_spinbox.pack()
    settings_ok_button.pack(pady=10, ipadx=10, ipady=5)
    

def start():
    '''Функция отрисовки всех виджетов для теста'''
    global all_words_for_test, questionnumber
    all_words_for_test = [i for i in QuiZZZ.start(test_mode.get())]
    #print(all_words_for_test)
    nextword()
    menu_frame.pack_forget()
    test_frame.pack(fill='x')

    menu_button.pack(anchor='nw', ipadx=5, ipady=5)
    test_label.pack(side=tk.TOP, anchor='center')

    word_frame.pack(anchor='center', fill='x', pady=75)
    test_word_label.pack()

    frame_bottom.pack(side=tk.BOTTOM, anchor='center')
    frame_top.pack(side=tk.BOTTOM, anchor='center')
    next_word_button.pack(side=tk.TOP, anchor='center', pady=10, ipady=10, ipadx=10)
    test_button_1.pack(side=tk.LEFT, anchor='center', fill='x', ipadx=100, ipady=20)
    test_button_2.pack(side=tk.LEFT, anchor='center', fill='x', ipadx=100, ipady=20)
    test_button_3.pack(side=tk.LEFT, anchor='center', fill='x', ipadx=100, ipady=20)
    test_button_4.pack(side=tk.LEFT, anchor='center', fill='x', ipadx=100, ipady=20)


def selectword(arg, button):
    '''Функция проверки правильности ответа'''
    next_word_button['state'] = 'normal'
    if arg == rightanswer.title():
        button.config(style='Correct.TButton')
    else:
        button.config(style='Incorrect.TButton')
        for i in [test_button_1, test_button_2, test_button_3, test_button_4]:
            if i['text'] == rightanswer.title():
                i.config(style='Correct.TButton')




questionnumber = 0
def nextword():
    '''Функция выдачи следующего вопроса'''
    global rightanswer, questionnumber
    print(questionnumber)
    if questionnumber == test_count.get():
        test_label.configure(text='Тест закончен')
        next_word_button.pack_forget()
        test_word_label.pack_forget()

        return
    word, word1, word2, word3, word4, rightanswer_idex = all_words_for_test[questionnumber]
    print(word, word1, word2, word3, word4, rightanswer_idex)
    rightanswer = [word1, word2, word3, word4][rightanswer_idex]
    #Activate all buttons
    for i in [test_button_1, test_button_2, test_button_3, test_button_4]:
        i.config(state='normal')
        i.config(style='TButton')
    test_word.set(value=word.title())
    var1.set(value=word1.title())
    var2.set(value=word2.title())
    var3.set(value=word3.title())
    var4.set(value=word4.title())
    next_word_button.config(state='disabled')
    questionnumber += 1

window = tk.Tk()
window.title("Quizzz")
window.geometry('640x480+400+200')
window.minsize(640,480)
complexity_list = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
test_complexity = tk.StringVar(value='A1')
theme_list = list(set([i[3] for i in QuiZZZ.all_words]))
test_theme = tk.StringVar(value='природа')
test_mode = tk.StringVar(value='Английский - Русский')
test_count = tk.IntVar(value=QuiZZZ.ask_count())

##All menu wingets
menu_frame = tk.Frame(window)
menu_buttom_frame = tk.Frame(menu_frame)
start_label = ttk.Label(menu_frame, text='Добро пожаловать', font=(deffont, 20))
start_button = ttk.Button(menu_buttom_frame, text='Начать тест', command=changemenutotest)
dictionary_button = ttk.Button(menu_buttom_frame, text='Словарь', command=changemenutodict)
settings_button = ttk.Button(menu_buttom_frame, text='Настройки', command=changemenutosettings)

#All dict widgets
dict_words = tk.StringVar(value=[' -- '.join(word[:2]).title() for word in QuiZZZ.all_words])
dict_frame = tk.Frame(window)
dict_listbox = tk.Listbox(dict_frame, listvariable=dict_words, font=(deffont, 12))
dict_label = ttk.Label(dict_frame, text='Словарь', font=(deffont, 20))
dict_scroll = ttk.Scrollbar(dict_frame, orient='vertical', command=dict_listbox.yview)
dict_listbox['yscrollcommand']=dict_scroll.set
dict_button_frame = tk.Frame(dict_frame)
dict_back_button = ttk.Button(dict_button_frame, text='Назад', command=changedicttomenu)

#All settings widgets
settings_frame = tk.Frame(window)
settings_main_label = ttk.Label(settings_frame, text='Настройки', font=(deffont, 20))
settings_button_frame = tk.Frame(settings_frame)
settings_mode_label = ttk.Label(settings_button_frame, text='Режим перевода', font=(deffont, 12))
settings_radiobutton1 = ttk.Radiobutton(settings_button_frame, text='Английский - Русский', value='Английский - Русский', variable=test_mode)
settings_radiobutton2 = ttk.Radiobutton(settings_button_frame, text='Русский - Английский', value='Русский - Английский', variable=test_mode)
settings_radiobutton3 = ttk.Radiobutton(settings_button_frame, text='Случайно', value='Случайно', variable=test_mode)
settings_button_frame2 = tk.Frame(settings_frame)
settings_comp_label = ttk.Label(settings_button_frame2, text='Сложность слов', font=(deffont, 12))
settings_combobox1 = ttk.Combobox(settings_button_frame2, textvariable=test_complexity, values=complexity_list)
settings_theme_label = ttk.Label(settings_button_frame2, text='Тема слов', font=(deffont, 12))
settings_combobox2 = ttk.Combobox(settings_button_frame2, textvariable=test_theme, values=theme_list)
settings_count_label = ttk.Label(settings_button_frame2, text='Количество слов', font=(deffont, 12))
settings_spinbox = ttk.Spinbox(settings_button_frame2, from_=3, to=30, textvariable=test_count)
settings_ok_button = ttk.Button(settings_button_frame2, text='OK', command=changesettingstomenu)


#All start widgets
style = ttk.Style()
style.configure('TButton')
style.configure('Correct.TButton', foreground='green')
style.configure('Incorrect.TButton', foreground='red')

test_word = tk.StringVar()
var1, var2, var3, var4 = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
test_frame = tk.Frame()
test_label = ttk.Label(test_frame, text="Выберите правильный перевод слова", font=(deffont, 20))
word_frame = tk.Frame(test_frame)
test_word_label = ttk.Label(word_frame, textvariable=test_word, font=(deffont, 15))
frame_bottom = tk.Frame(window)
frame_top = tk.Frame(window)
test_button_1 = ttk.Button(frame_top, textvariable=var1, command=lambda: selectword(var1.get(), test_button_1))
test_button_2 = ttk.Button(frame_top, textvariable=var2, command=lambda: selectword(var2.get(), test_button_2))
test_button_3 = ttk.Button(frame_bottom, textvariable=var3, command=lambda: selectword(var3.get(), test_button_3))
test_button_4 = ttk.Button(frame_bottom, textvariable=var4, command=lambda: selectword(var4.get(), test_button_4))
next_word_button = ttk.Button(frame_top, text='Дальше', command=nextword)
menu_button = ttk.Button(test_frame, text='<<', command=changetesttomenu)

#All end screen widgets
stats = tk.StringVar()
end_screen_frame = tk.Frame()
end_screen_label = ttk.Label(end_screen_frame, text='Тест окончен', font=(deffont, 20))
end_screen_stat_label = ttk.Label(end_screen_frame, textvariable=stats, font=(deffont, 12))
end_screen_menu_button = ttk.Button(end_screen_frame, text='Меню', command=changeendtomenu)

menu()
window.mainloop()
