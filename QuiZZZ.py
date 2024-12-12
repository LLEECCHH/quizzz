import os
import random
import sqlite3
from unittest.mock import Mock


'''Есть база данных на 3000+ слов в файле words.db.'''
db = sqlite3.connect('words.db')
c = db.cursor()
c.execute("SELECT * FROM words")
all_words = c.fetchall()
for i in range(len(all_words)):
	all_words[i] = tuple(j.strip() for j in all_words[i])
db.commit()
db.close()


ask_count = 10
'''Задаёт количество вопросов в тесте.'''


def menu():
	'''Вот список доступных функций:
	> Вернуться в главное меню (menu) <
	> Настройки языка (settings) <
	> Начать тестирование (start) <
	> Остановить тестирование - только во время теста (stop) <
	> Выбрать сложность и тематику слов (complexity_and_topic) <
	> Повторить слова и их перевод (dictionary) <
	> Помощь (help_pls) <
	> Выйти из программы (exit) <'''
	funcs = (menu, settings, start, stop, complexity_and_topic, dictionary, help_pls, exit)
	func = Mock()
	func()


def settings():
	'''Выбери режим перевода:
	> Английский - Русский <
	> Русский - Английский <
	> Случайно <'''
	s = Mock()
	'''Если выбран варинат "Случайно":'''
	# s = random.choice('Английский - Русский', 'Русский - Английский')
	return s
setts = settings()
setts = 'Английский - Русский'

def complexity_and_topic():
	'''Выбери сложность и тему слов.
	Сложность:	Тема:
	> A1 <		> природа <
	> A2 <		> учёба <
	> B1 <		> наука <
	> B2 <		> спорт <
	> C1 <		> технологии <
	> C2 <		> черты характера <
				> животные <
				> политика и экономика <
				> домашний быт <
				> бизнес <'''
	global all_words
	c = 'B2'	# Выбранная сложность
	t = 'природа'	# Выбранная тема
	words = [item for item in all_words if (item[2] == c) and (item[3] == t)]
	processing = []
	on_fix = []
	repeat = []
	new = [item[1] if setts == 'Русский - Английский' else item[0] for item in words]
	return (words, new, processing, on_fix, repeat)


words, new, processing, on_fix, repeat = complexity_and_topic()
'''Имеется список: words = [(word, transl, compl, topic), (word, transl, compl, topic), (word, transl, compl, topic), ...].'''
def start():
	'''Применение настроек к тестировующей системе.'''
	dct = {}
	for item in words:
		s = [item[0], item[1]]
		if setts == 'Английский - Русский':
			dct[s[0]] = s[-1].rstrip()
		else:
			dct[s[-1].rstrip()] = s[0]
	dict_keys = list(dct)

	'''Распределение шансов выпадения слов.
	new: Новое - одинаковый шанс для всех (10%)
	processing: На отработке (выученное недавно) - повышенный шанс (15%)
	on_fix: На исправлении (больше всего ошибок) - сильно повышенный шанс (70%)
	repeat: На повторении (меньше всего ошибок) - пониженный шанс (5%)'''
	chances = []
	for k in dict_keys:
		if k in processing:
			chances.append(15)
		elif k in on_fix:
			chances.append(70)
		elif k in repeat:
			chances.append(5)
		else:
			chances.append(10)
	cnt_5 = chances.count(5)
	cnt_10 = chances.count(10)
	cnt_15 = chances.count(15)
	cnt_70 = chances.count(70)
	changes = {5: 5 / cnt_5 if cnt_5 > 0 else 0, \
			 10: 10 / cnt_10 if cnt_10 > 0 else 0, \
			 15: 15 / cnt_15 if cnt_15 > 0 else 0, \
			 70: 70 / cnt_70 if cnt_70 > 0 else 0}
	chances = [changes[i] for i in chances]

	'''Работа самой тестирующей системы.
	ask_count - количество вопросов в тесте. Задавалась в начале.'''
	dict_translations = list(dct.values())
	score = 0
	for _ in range(ask_count):
		word = random.choices(dict_keys, weights = chances, k = 1)[0]
		s = dict_translations.copy()
		variants = [0] * 4
		right_answer_index = random.randint(0, 3)
		variants[right_answer_index] = dct[word]
		s.remove(dct[word])
		for i in range(4):
			if variants[i] == 0:
				variants[i] = s.pop(random.randint(0, len(s) - 1))
		var1, var2, var3, var4 = variants	   # Варианты ответов
		# print(f'Переведи слово: {word}. 1) {var1}; 2) {var2}; 3) {var3}; 4) {var4}.')
		# answer = input()
		answer = Mock()
		# answer = int(answer)
		flag = 0
		if answer == right_answer_index + 1:
			score += 1
			if word in on_fix:
				on_fix.remove(word)
				processing.append(word)
				chances.remove(changes[70])
			elif word in processing:
				processing.remove(word)
				repeat.append(word)
				chances.remove(changes[15])
			elif word in new:
				new.remove(word)
				processing.append(word)
				chances.remove(changes[10])
			else:
				flag = 1

		else:
			if word in processing:
				processing.remove(word)
				chances.remove(changes[15])
				on_fix.append(word)
			elif word in repeat:
				repeat.remove(word)
				chances.remove(changes[5])
				on_fix.append(word)
			elif word in new:
				new.remove(word)
				chances.remove(changes[10])
				on_fix.append(word)
			else:
				flag = 1
		if flag != 1:
			dict_keys.remove(word)
	'''Нужно вывести:
	Правильных ответов: {score}/{ask_count}.'''
	menu()


def stop():
	'''Тестирование было остановлено. Уверен, что хочешь выйти?
	> Вернуться в главное меню <
	> Продолжить тест <'''
	menu()


def dictionary():
	'''Вот твой текущий словарь.
	Здесь выводится словарь слов (слова и переводы хранятся в списке words) по выбранной ранее сложности и тематике.
	> Вернуться в главное меню <'''
	menu()


def help_pls():
	try:
		os.startfile('info.pdf')
	except Exception as e:
		return f'Ошибка при открытии файла: {e}'
	'''Вся необходимая информация представлена в файле info.pdf.
	> Вернуться в главное меню <'''
	menu()


def exit():
	'''Не уверен, что она вообще нужна.
	Закрывает программу.'''


if __name__ == "__main__":
	menu()