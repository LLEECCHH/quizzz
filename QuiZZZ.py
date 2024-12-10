import os
import random
from unittest.mock import Mock


def menu():
	yield 'Приветствую в QuiZZZ!\n\
	Вот список доступных функций:\n\
	> Вернуться в главное меню <\n\
	> Настройки языка <\n\
	> Начать тестирование <\n\
	> Выбрать сложность слов <\n\
	> Выбрать тематику слов <\n\
	> Повторить слова и их перевод <\n\
	> Помощь <\n\
	> Выйти из программы <'
	funcs = (menu, settings, start, stop, complexity, theme, dictionary, help_pls, exit)
	func = Mock()
	func()


def settings():
	yield 'Выбери режим перевода:\n\
	> Английский - Русский <\n\
	> Русский - Английский <\n\
	> Случайно <'
	s = Mock()
	return s


def start():
	setts = settings()
	my_dict = {}
	with open('words.txt', 'r', encoding = 'utf-8') as file:
		words = file.readlines()
		for item in words:
			s = item.split(' - ')
			if setts == 'Английский - Русский':
				my_dict[s[0]] = s[-1].rstrip()
			elif setts == 'Русский - Английский':
				my_dict[s[-1].rstrip()] = s[0]
			else:
				num = random.randint(0, 1)
				if num == 0:
					my_dict[s[0]] = s[-1].rstrip()
				else:
					my_dict[s[-1].rstrip()] = s[0]

	dict_keys = list(my_dict)
	dict_translations = list(my_dict.values())
	score = 0
	mistakes = []

	yield 'Начинаем!'
	for _ in range(len(dict_keys)):
		word = random.choice(dict_keys)
		s = dict_translations.copy()
		variants = [0] * 4
		right_answer_index = random.randint(0, 3)
		variants[right_answer_index] = my_dict[word]
		s.remove(my_dict[word])
		for i in range(4):
			if variants[i] == 0:
				variants[i] = s.pop(random.randint(0, len(s) - 1))
		var1, var2, var3, var4 = variants
		answer = Mock()		# Переведи слово: {word}. Варианты ответов: 1) {var1}; 2) {var2}; 3) {var3}; 4) {var4}.
		answer = int(answer)
		yield f'Правильный ответ: {right_answer_index + 1}) {variants[right_answer_index]}.'
		if answer == right_answer_index + 1:
			yield f'Твой ответ: {answer}) {variants[answer - 1]}.'
			score += 1
		else:
			yield f'Твой ответ: {answer}) {variants[answer - 1]}.'
			mistakes.append(word)
		dict_keys.remove(word)
	yield 'Тест окончен!'
	yield f'Правильных ответов: {score}/{len(my_dict)}.'
	menu()


def stop():
	yield 'Тестирование было остановлено. Уверен, что хочешь выйти?\n\
	> Вернуться в главное меню <\n\
	> Продолжить тест <'
	menu()


def complexity():
	pass


def theme():
	pass


def dictionary():
	yield 'Вот твой текущий словарь.'
	with open('words.txt', 'r', encoding = 'utf-8') as file:
		words = file.readlines()
		for item in words:
			yield item.rstrip()
	yield '> Вернуться в главное меню <'
	menu()


def help_pls():
	try:
		os.startfile('info.pdf')
		yield f'Вся необходимая информация представлена в файле info.pdf.'
	except Exception as e:
		yield f'Ошибка при открытии файла: {e}'
	yield '> Вернуться в главное меню <'
	menu()


def exit():
	return 'До новых встреч!'

if __name__ == "__main__":
	menu()