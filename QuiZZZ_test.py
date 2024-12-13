import os
import random
import sqlite3
import unittest
from unittest.mock import Mock, patch
import QuiZZZ
from QuiZZZ import dict_db, settings, complexity_and_topic, start, stop, dictionary, help_pls, menu, exit

# ... (остальной код без изменений)

# Класс TestComplexityAndTopic содержит тесты для функции complexity_and_topic()
class TestComplexityAndTopic(unittest.TestCase):
    # Тестируем функцию complexity_and_topic() для случая "Английский - Русский"
    @patch('QuiZZZ.dict_db', return_value=[('word1', 'translation1', 'B2', 'природа'),
                                           ('word2', 'translation2', 'A1', 'учёба'),
                                           ('word3', 'translation3', 'B2', 'природа')])
    @patch('QuiZZZ.settings', return_value='Английский - Русский')
    def test_complexity_and_topic(self, mock_settings, mock_dict_db):
        # Вызываем тестируемую функцию
        import importlib
        c, t, words, new, processing, on_fix, repeat = importlib.reload(QuiZZZ).complexity_and_topic()

        # Перезагружаем модуль, чтобы изменения вступили в силу.
        importlib.reload(QuiZZZ)

        # Проверяем возвращаемые значения
        self.assertEqual(c, 'B2')
        self.assertEqual(t, 'природа')
        self.assertEqual(words, [('word1', 'translation1', 'B2', 'природа'),
                                 ('word3', 'translation3', 'B2', 'природа')])
        self.assertEqual(new, ['word1', 'word3'])
        self.assertEqual(processing, [])
        self.assertEqual(on_fix, [])
        self.assertEqual(repeat, [])

    # Тестируем функцию complexity_and_topic() для случая "Русский - Английский"
    @patch('QuiZZZ.dict_db', return_value=[('word1', 'translation1', 'B2', 'природа'),
                                           ('word2', 'translation2', 'A1', 'учёба'),
                                           ('word3', 'translation3', 'B2', 'природа')])
    @patch('QuiZZZ.settings', return_value='Русский - Английский')
    def test_complexity_and_topic_russian_english(self, mock_settings, mock_dict_db):
        # Вызываем тестируемую функцию
        import importlib
        c, t, words, new, processing, on_fix, repeat = importlib.reload(QuiZZZ).complexity_and_topic()

        # Перезагружаем модуль, чтобы изменения вступили в силу.
        importlib.reload(QuiZZZ)

        # Проверяем возвращаемые значения
        self.assertEqual(c, 'B2')
        self.assertEqual(t, 'природа')
        self.assertEqual(words, [('word1', 'translation1', 'B2', 'природа'),
                                 ('word3', 'translation3', 'B2', 'природа')])
        self.assertEqual(new, ['translation1', 'translation3'])
        self.assertEqual(processing, [])
        self.assertEqual(on_fix, [])
        self.assertEqual(repeat, [])

if __name__ == '__main__':
    unittest.main()

'''
# Класс TestStart содержит тесты для функции start()
class TestStart(unittest.TestCase):

	# Тестируем функцию start() для случая "Английский - Русский"
	@patch('__main__.words', [('word1', 'translation1', 'A1', 'природа'),
							  ('word2', 'translation2', 'B2', 'природа'),
							  ('word3', 'translation3', 'A1', 'природа')])
	@patch('__main__.ask_count', 2) # Количество вопросов
	@patch('__main__.menu')
	@patch('random.choices')
	@patch('random.randint')
	def test_start_english_russian(self, mock_randint, mock_choices, mock_menu):
		# Имитируем результаты random.randint (индекс правильного ответа)
		mock_randint.side_effect = [0, 1]
		# Имитируем результаты random.choices (выбор слов)
		mock_choices.side_effect = [['word1'], ['word3']]
		# Имитируем ответы пользователя
		mock_answer = Mock()
		mock_answer.side_effect = [1, 1]
		# Заменяем Mock в тестируемой функции на нашу имитацию
		with patch('__main__.Mock', mock_answer):
		  # Вызываем функцию start() как генератор
		  gen = start(setts='Английский - Русский')

		  # Получаем первый вопрос
		  word, var1, var2, var3, var4, right_answer = next(gen)
		  self.assertEqual(word, 'word1')
		  self.assertEqual(right_answer, 0)

		  # Получаем второй вопрос
		  word, var1, var2, var3, var4, right_answer = next(gen)
		  self.assertEqual(word, 'word3')
		  self.assertEqual(right_answer, 1)

	# Тестируем функцию start() для случая "Русский - Английский"
	@patch('__main__.words', [('word1', 'translation1', 'A1', 'природа'),
							  ('word2', 'translation2', 'B2', 'природа'),
							  ('word3', 'translation3', 'A1', 'природа')])
	@patch('__main__.ask_count', 2)
	@patch('__main__.menu')
	@patch('random.choices')
	@patch('random.randint')
	def test_start_russian_english(self, mock_randint, mock_choices, mock_menu):
		mock_randint.side_effect = [0, 1]
		mock_choices.side_effect = [['translation1'], ['translation3']]
		mock_answer = Mock()
		mock_answer.side_effect = [1, 1]

		with patch('__main__.Mock', mock_answer):
			gen = start(setts='Русский - Английский')

			word, var1, var2, var3, var4, right_answer = next(gen)
			self.assertEqual(word, 'translation1')
			self.assertEqual(right_answer, 0)

			word, var1, var2, var3, var4, right_answer = next(gen)
			self.assertEqual(word, 'translation3')
			self.assertEqual(right_answer, 1)

	# Тестируем правильный ответ для нового слова
	@patch('__main__.words', [('word1', 'translation1', 'A1', 'природа')])
	@patch('__main__.ask_count', 1)
	@patch('__main__.new', ['word1'])
	@patch('__main__.processing', [])
	@patch('__main__.on_fix', [])
	@patch('__main__.repeat', [])
	@patch('__main__.menu')
	@patch('random.choices')
	@patch('random.randint')
	def test_start_correct_answer_new(self, mock_randint, mock_choices, mock_menu, mock_repeat, mock_on_fix,
									   mock_processing, mock_new):
		mock_randint.return_value = 0
		mock_choices.return_value = ['word1']
		mock_answer = Mock()
		mock_answer.return_value = 1

		with patch('__main__.Mock', mock_answer):
		  gen = start(setts='Английский - Русский')
		  next(gen)

		  self.assertEqual(mock_new, [])
		  self.assertEqual(mock_processing, ['word1'])

	# Тестируем правильный ответ для слова на отработке
	@patch('__main__.words', [('word1', 'translation1', 'A1', 'природа')])
	@patch('__main__.ask_count', 1)
	@patch('__main__.new', [])
	@patch('__main__.processing', ['word1'])
	@patch('__main__.on_fix', [])
	@patch('__main__.repeat', [])
	@patch('__main__.menu')
	@patch('random.choices')
	@patch('random.randint')
	def test_start_correct_answer_processing(self, mock_randint, mock_choices, mock_menu, mock_repeat, mock_on_fix,
											  mock_processing, mock_new):
		mock_randint.return_value = 0
		mock_choices.return_value = ['word1']
		mock_answer = Mock()
		mock_answer.return_value = 1

		with patch('__main__.Mock', mock_answer):
			gen = start(setts='Английский - Русский')
			next(gen)

			self.assertEqual(mock_processing, [])
			self.assertEqual(mock_repeat, ['word1'])

	# Тестируем правильный ответ для слова на исправлении
	@patch('__main__.words', [('word1', 'translation1', 'A1', 'природа')])
	@patch('__main__.ask_count', 1)
	@patch('__main__.new', [])
	@patch('__main__.processing', [])
	@patch('__main__.on_fix', ['word1'])
	@patch('__main__.repeat', [])
	@patch('__main__.menu')
	@patch('random.choices')
	@patch('random.randint')
	def test_start_correct_answer_on_fix(self, mock_randint, mock_choices, mock_menu, mock_repeat, mock_on_fix,
										 mock_processing, mock_new):
		mock_randint.return_value = 0
		mock_choices.return_value = ['word1']
		mock_answer = Mock()
		mock_answer.return_value = 1

		with patch('__main__.Mock', mock_answer):
			gen = start(setts='Английский - Русский')
			next(gen)

			self.assertEqual(mock_on_fix, [])
			self.assertEqual(mock_processing, ['word1'])

	# Тестируем правильный ответ для слова на повторении
	@patch('__main__.words', [('word1', 'translation1', 'A1', 'природа')])
	@patch('__main__.ask_count', 1)
	@patch('__main__.new', [])
	@patch('__main__.processing', [])
	@patch('__main__.on_fix', [])
	@patch('__main__.repeat', ['word1'])
	@patch('__main__.menu')
	@patch('random.choices')
	@patch('random.randint')
	def test_start_correct_answer_repeat(self, mock_randint, mock_choices, mock_menu, mock_repeat, mock_on_fix,
										 mock_processing, mock_new):
		mock_randint.return_value = 0
		mock_choices.return_value = ['word1']
		mock_answer = Mock()
		mock_answer.return_value = 1

		with patch('__main__.Mock', mock_answer):
		  gen = start(setts='Английский - Русский')
		  next(gen)

		  self.assertEqual(mock_repeat, ['word1'])
		  self.assertEqual(mock_processing, [])
		  self.assertEqual(mock_on_fix, [])
		  self.assertEqual(mock_new, [])

	# Тестируем неправильный ответ для нового слова
	@patch('__main__.words', [('word1', 'translation1', 'A1', 'природа')])
	@patch('__main__.ask_count', 1)
	@patch('__main__.new', ['word1'])
	@patch('__main__.processing', [])
	@patch('__main__.on_fix', [])
	@patch('__main__.repeat', [])
	@patch('__main__.menu')
	@patch('random.choices')
	@patch('random.randint')
	def test_start_incorrect_answer_new(self, mock_randint, mock_choices, mock_menu, mock_repeat, mock_on_fix,
										 mock_processing, mock_new):
		mock_randint.return_value = 0
		mock_choices.return_value = ['word1']
		mock_answer = Mock()
		mock_answer.return_value = 2

		with patch('__main__.Mock', mock_answer):
			gen = start(setts='Английский - Русский')
			next(gen)
			self.assertEqual(mock_new, [])
			self.assertEqual(mock_on_fix, ['word1'])

	# Тестируем неправильный ответ для слова на отработке
	@patch('__main__.words', [('word1', 'translation1', 'A1', 'природа')])
	@patch('__main__.ask_count', 1)
	@patch('__main__.new', [])
	@patch('__main__.processing', ['word1'])
	@patch('__main__.on_fix', [])
	@patch('__main__.repeat', [])
	@patch('__main__.menu')
	@patch('random.choices')
	@patch('random.randint')
	def test_start_incorrect_answer_processing(self, mock_randint, mock_choices, mock_menu, mock_repeat, mock_on_fix,
											  mock_processing, mock_new):
		mock_randint.return_value = 0
		mock_choices.return_value = ['word1']
		mock_answer = Mock()
		mock_answer.return_value = 2

		with patch('__main__.Mock', mock_answer):
		  gen = start(setts='Английский - Русский')
		  next(gen)
		  self.assertEqual(mock_processing, [])
		  self.assertEqual(mock_on_fix, ['word1'])

	# Тестируем неправильный ответ для слова на повторении
	@patch('__main__.words', [('word1', 'translation1', 'A1', 'природа')])
	@patch('__main__.ask_count', 1)
	@patch('__main__.new', [])
	@patch('__main__.processing', [])
	@patch('__main__.on_fix', [])
	@patch('__main__.repeat', ['word1'])
	@patch('__main__.menu')
	@patch('random.choices')
	@patch('random.randint')
	def test_start_incorrect_answer_repeat(self, mock_randint, mock_choices, mock_menu, mock_repeat, mock_on_fix,
										 mock_processing, mock_new):
		mock_randint.return_value = 0
		mock_choices.return_value = ['word1']
		mock_answer = Mock()
		mock_answer.return_value = 2

		with patch('__main__.Mock', mock_answer):
		  gen = start(setts='Английский - Русский')
		  next(gen)
		  self.assertEqual(mock_repeat, [])
		  self.assertEqual(mock_on_fix, ['word1'])

	# Тестируем неправильный ответ для слова на исправлении
	@patch('__main__.words', [('word1', 'translation1', 'A1', 'природа')])
	@patch('__main__.ask_count', 1)
	@patch('__main__.new', [])
	@patch('__main__.processing', [])
	@patch('__main__.on_fix', ['word1'])
	@patch('__main__.repeat', [])
	@patch('__main__.menu')
	@patch('random.choices')
	@patch('random.randint')
	def test_start_incorrect_answer_on_fix(self, mock_randint, mock_choices, mock_menu, mock_repeat, mock_on_fix,
										 mock_processing, mock_new):
		mock_randint.return_value = 0
		mock_choices.return_value = ['word1']
		mock_answer = Mock()
		mock_answer.return_value = 2

		with patch('__main__.Mock', mock_answer):
		  gen = start(setts='Английский - Русский')
		  next(gen)
		  self.assertEqual(mock_on_fix, ['word1'])
		  self.assertEqual(mock_processing, [])
		  self.assertEqual(mock_repeat, [])
		  self.assertEqual(mock_new, [])

# Класс TestStop содержит тесты для функции stop()
class TestStop(unittest.TestCase):
	@patch('__main__.menu')
	def test_stop(self, mock_menu):
		stop()
		mock_menu.assert_called_once()

# Класс TestDictionary содержит тесты для функции dictionary()
class TestDictionary(unittest.TestCase):
	@patch('__main__.menu')
	def test_dictionary(self, mock_menu):
		dictionary()
		mock_menu.assert_called_once()

# Класс TestHelpPls содержит тесты для функции help_pls()
class TestHelpPls(unittest.TestCase):
	@patch('os.startfile')
	@patch('__main__.menu')
	def test_help_pls_success(self, mock_menu, mock_startfile):
		result = help_pls()
		self.assertIsNone(result)
		mock_startfile.assert_called_once_with('info.pdf')
		mock_menu.assert_called_once()

	@patch('os.startfile', side_effect=Exception('Test Exception'))
	@patch('__main__.menu')
	def test_help_pls_failure(self, mock_menu, mock_startfile):
		result = help_pls()
		self.assertEqual(result, 'Ошибка при открытии файла: Test Exception')
		mock_startfile.assert_called_once_with('info.pdf')
		mock_menu.assert_not_called()

# Класс TestMenu содержит тесты для функции menu()
class TestMenu(unittest.TestCase):
	@patch('__main__.menu')
	@patch('__main__.settings')
	@patch('__main__.start')
	@patch('__main__.stop')
	@patch('__main__.complexity_and_topic')
	@patch('__main__.dictionary')
	@patch('__main__.help_pls')
	@patch('__main__.exit')
	def test_menu(self, mock_exit, mock_help, mock_dict, mock_comp, mock_stop, mock_start, mock_settings, mock_menu):
		mock_func = Mock()
		with patch('__main__.Mock', return_value=mock_func):
			menu()
			mock_func.assert_called_once()
'''