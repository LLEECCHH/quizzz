import os
import random
from colorama import init
from colorama import Fore, Back


def menu():
	print()
	print('Приветствую в QuiZZZ!')
	print('Вот список доступных функций: (Введи одну или две буквы, чтобы выполнить соответствующую команду)')
	print('> m - Вернуться в главное меню')
	print('> st - Начать тестирование')
	print('> sp - Остановить тестирование (работает только при проведении тестирования)')
	print('> c - Выбрать сложность слов')
	print('> t - Выбрать тематику слов')
	print('> d - Повторить слова и их перевод')
	print('> h - Помощь')
	print('> e - Выйти из программы')
	command = input()
	commands = {'m': menu, 'st': start, 'c': complexity, 't': theme, 'd': dictionary, 'h': help_pls, 'e': exit}
	while command not in commands:
		command = input('Неизвестная команда, повтори ещё раз, пожалуйста: ')
	print()
	commands[command]()


settings = 'английский - русский'
def start():
	global settings
	change = input(f'Текущий режим перевода: {settings}. Поменять их местами? (Enter если нет, любой символ иначе)' )
	my_dict = {}
	with open('words.txt', 'r', encoding = 'utf-8') as file:
		words = file.readlines()
		for item in words:
			s = item.split(' - ')
			if change:
				my_dict[s[0]] = s[-1].rstrip()
				settings = 'русский - английский'
			else:
				my_dict[s[-1].rstrip()] = s[0]

	dict_keys = list(my_dict)
	dict_translations = list(my_dict.values())
	score = 0
	mistakes = []

	print('Начинаем!')
	for _ in range(len(dict_keys)):
		word = random.choice(dict_keys)
		s = dict_translations.copy()
		variants = [0] * 4
		right_answer = random.randint(0, 3)
		variants[right_answer] = my_dict[word]
		s.remove(my_dict[word])
		for i in range(4):
			if variants[i] == 0:
				variants[i] = s.pop(random.randint(0, len(s) - 1))
		var1, var2, var3, var4 = variants
		answer = input(f'Переведи слово: {word}. Варианты ответов: 1) {var1}; 2) {var2}; 3) {var3}; 4) {var4}. ')
		while answer not in ('1', '2', '3', '4', 'sp'):
			answer = input('Не понял тебя. Повтори, пожалуйста, ещё раз: (Подсказка: в ответе напиши одну из цифр 1, 2, 3 или 4, в зависимости от того, какая цифра стоит рядом с ответом, который ты считаешь правильным) ')
		if answer == 'sp':
			stop()
			return
		answer = int(answer)
		print(f'Правильный ответ: {Fore.BLACK}{Back.GREEN}{right_answer + 1}) {variants[right_answer]}{Fore.RESET}{Back.RESET}.')
		if answer == right_answer + 1:
			print(f'Твой ответ: {Fore.BLACK}{Back.GREEN}{answer}) {variants[answer - 1]}{Fore.RESET}{Back.RESET}.')
			score += 1
		else:
			print(f'Твой ответ: {Fore.BLACK}{Back.RED}{answer}) {variants[answer - 1]}{Fore.RESET}{Back.RESET}.')
			mistakes.append(word)
		print()
		dict_keys.remove(word)
	print('Тест окончен!')
	print(f'Правильных ответов: {score}/{len(my_dict)}.')
	print()
	ans = input('> m - Вернуться в главное меню ')
	while ans != 'm':
		ans = input('Неизвестная команда, повтори ещё раз, пожалуйста: ')
	menu()


def stop():
	print('Тестирование было прервано.')
	print()
	ans = input('> m - Вернуться в главное меню ')
	while ans != 'm':
		ans = input('Неизвестная команда, повтори ещё раз, пожалуйста: ')
	menu()


def complexity():
	print('В разработке :)')
	print()
	ans = input('> m - Вернуться в главное меню ')
	while ans != 'm':
		ans = input('Неизвестная команда, повтори ещё раз, пожалуйста: ')
	menu()


def theme():
	print('В разработке :)')
	print()
	ans = input('> m - Вернуться в главное меню ')
	while ans != 'm':
		ans = input('Неизвестная команда, повтори ещё раз, пожалуйста: ')
	menu()


def dictionary():
	print('Вот твой текущий словарь.')
	with open('words.txt', 'r', encoding = 'utf-8') as file:
		words = file.readlines()
		for item in words:
			print(item.rstrip())
	print()
	ans = input('> m - Вернуться в главное меню ')
	while ans != 'm':
		ans = input('Неизвестная команда, повтори ещё раз, пожалуйста: ')
	menu()


def help_pls():
	try:
		os.startfile('info.pdf')
		print(f'Вся необходимая информация представлена в файле info.pdf.')
	except Exception as e:
		print(f'Ошибка при открытии файла: {e}')
	print()
	ans = input('> m - Вернуться в главное меню ')
	while ans != 'm':
		ans = input('Неизвестная команда, повтори ещё раз, пожалуйста: ')
	menu()


def exit():
	print('До новых встреч!')


menu()