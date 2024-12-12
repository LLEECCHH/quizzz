import os
import random
import sqlite3
from unittest.mock import Mock


db = sqlite3.connect('test_words.db')
c = db.cursor()

'''Какая-то тестовая база данных.

c.execute("""CREATE TABLE test_words (
	word VARCHAR,
	translation VARCHAR,
	complexity CHAR,
	theme VARCHAR
	)""")

c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Apple	", "	Яблоко	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	House	", "	Дом	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Book	", "	Книга	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Table	", "	Стол	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Chair	", "	Стул	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Window	", "	Окно	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Door	", "	Дверь	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Car	", "	Машина	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Tree	", "	Дерево	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Sun	", "	Солнце	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Water	", "	Вода	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Fire	", "	Огонь	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Sky	", "	Небо	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Cloud	", "	Облако	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Rain	", "	Дождь	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Snow	", "	Снег	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Wind	", "	Ветер	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Earth	", "	Земля	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Moon	", "	Луна	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Star	", "	Звезда	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Road	", "	Дорога	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	River	", "	Река	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Lake	", "	Озеро	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Sea	", "	Море	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Ocean	", "	Океан	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Mountain	", "	Гора	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Forest	", "	Лес	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Field	", "	Поле	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Flower	", "	Цветок	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Grass	", "	Трава	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Garden	", "	Сад	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Animal	", "	Животное	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Dog	", "	Собака	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Cat	", "	Кот	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Fish	", "	Рыба	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Bird	", "	Птица	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Horse	", "	Лошадь	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Cow	", "	Корова	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Pig	", "	Свинья	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Chicken	", "	Курица	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Fox	", "	Лиса	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Wolf	", "	Волк	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Bear	", "	Медведь	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Snake	", "	Змея	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Lion	", "	Лев	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Tiger	", "	Тигр	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Elephant	", "	Слон	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Parrot	", "	Попугай	", "	?complexity?	", "	?theme?	")')
c.execute('INSERT INTO test_words (word, translation, complexity, theme) VALUES ("	Monkey	", "	Обезьяна	", "	?complexity?	", "	?theme?	")')'''

c.execute("SELECT * FROM test_words")
words = c.fetchall()
for i in range(len(words)):
	words[i] = tuple(j.strip() for j in words[i])

db.commit()
db.close()


ask_count = 10
'''Задаёт количество вопросов в тестировании'''


def menu():
	'''Вот список доступных функций:
	> Вернуться в главное меню (menu) <
	> Настройки языка (settings) <
	> Начать тестирование (start) <
	> Остановить тестирование - только во время теста (stop) <
	> Выбрать сложность и тематику слов (complexity_and_theme) <
	> Повторить слова и их перевод (dictionary) <
	> Помощь (help_pls) <
	> Выйти из программы (exit) <'''
	funcs = (menu, settings, start, stop, complexity_and_theme, dictionary, help_pls, exit)
	func = Mock()
	func()


def settings():
	'''Выбери режим перевода:
	> Английский - Русский <
	> Русский - Английский <
	> Случайно <'''
	s = Mock()
	return s


def complexity_and_theme():
	global words
	processing = []
	on_fix = []
	repeat = []
	new = [item[1] for item in words]
	return (words, new, processing, on_fix, repeat)


words, new, processing, on_fix, repeat = complexity_and_theme()
'''Имеется список: words = [(word, transl, compl, theme), (word, transl, compl, theme), (word, transl, compl, theme), ...].
В тестовом файле все слова одних пока что неопределённых сложности и темы.'''
def start():
	setts = 'Русский - Английский'
	dct = {}
	for item in words:
		s = [item[0], item[1]]
		if setts == 'Английский - Русский':
			dct[s[0]] = s[-1].rstrip()
		elif setts == 'Русский - Английский':
			dct[s[-1].rstrip()] = s[0]
		else:
			num = random.randint(0, 1)
			if num == 0:
				dct[s[0]] = s[-1].rstrip()
			else:
				dct[s[-1].rstrip()] = s[0]
	dict_keys = list(dct)
	'''new: Новое - одинаковый шанс для всех (10%)
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
	'''f'Правильных ответов: {score}/{ask_count}.'''
	menu()


def stop():
	'''Тестирование было остановлено. Уверен, что хочешь выйти?
	> Вернуться в главное меню <
	> Продолжить тест <'''
	menu()


def dictionary():
	'''Вот твой текущий словарь.
	Здесь выводится словарь слов по выбранной ранее сложности и тематике.
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