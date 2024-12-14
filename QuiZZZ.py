import os
import random
import sqlite3
from unittest.mock import Mock


'''Есть база данных на 3000+ слов в файле words.db.'''
def dict_db():
        '''
        Подключается к базе данных words.db, берет из нее все строки и возвращает их списком.

         :returns: Список строк из базы данных words.db
         :rtype: list
         :raises ValueError: Если возникает ошибка при открытии базы данных
         '''
        
        try:
                db = sqlite3.connect('words.db')
        except Exception as e:
                return f'Ошибка при открытии файла: {e}'
        c = db.cursor()
        c.execute("SELECT * FROM words")
        all_words = c.fetchall()
        for i in range(len(all_words)):
                all_words[i] = tuple(j.strip() for j in all_words[i])
        db.commit()
        db.close()
        return all_words
all_words = dict_db()
'''Список всех слов из базы данных'''


def ask_count():
        '''
        Задаёт количество вопросов в одном тесте.

         :returns: Количество вопросов в одном тесте
         :rtype: int
         '''
        
        questions = 10
        return questions


def menu():
        '''
        Выдает список основных функций:
        > Вернуться в главное меню (menu) <
        > Настройки языка (settings) <
        > Начать тестирование (start) <
        > Остановить тестирование - только во время теста (stop) <
        > Выбрать сложность и тематику слов (complexity_and_topic) <
        > Повторить слова и их перевод (dictionary) <
        > Помощь (help_pls) <
        > Выйти из программы (exit) <
        '''

        funcs = (menu, settings, start, complexity_and_topic)
        func = Mock()
        func()


def settings():
        '''
        Возвращает одну из настроек перевода, выбранную пользователем:
        > Английский - Русский <
        > Русский - Английский <
        > Случайно <

         :returns: Выбранная настройка
         :rtype: str
        '''
        
        var1, var2, var3 = 'Английский - Русский', 'Русский - Английский', 'Случайно'
        # yield var1, var2, var3
        answer = Mock()
        if answer == var1:
                return 'Английский - Русский'
        elif answer == var2:
                return 'Русский - Английский'
        else:
                return random.choice(('Английский - Русский', 'Русский - Английский'))
setts = settings()
'''Выбранная настройка перевод'''


def complexity_and_topic(c='A1', t='природа'):
        '''
        Возвращает одну тему и одну сложность, которые выберет пользователь, а также списки:
        words; new; processing; on_fix; repeat
        для последующих тестов.
        Сложность:        Тема:
        > A1 <                > природа <
        > A2 <                > учёба <
        > B1 <                > наука <
        > B2 <                > спорт <
        > C1 <                > технологии <
        > C2 <                > черты характера <
                        > животные <
                        > политика и экономика <
                        > домашний быт <
                        > бизнес <
        
        :returns: Кортеж, состоящий из сложности, темы и списков words, new, processing, on_fix, repeat
        :rtype: tuple
        '''
        global complexity, theme, words, new, processing, on_fix, repeat
        # c = 'A2'        # Выбранная сложность
        # t = 'природа'        # Выбранная тема
        words = [(item[0], item[1]) for item in all_words if (item[2] == c) and (item[3] == t)]
        processing = []
        on_fix = []
        repeat = []
        new = [item[1] if setts == 'Русский - Английский' else item[0] for item in words]
        # return complexity, theme, words, new, processing, on_fix, repeat
# complexity, topic, words, new, processing, on_fix, repeat = complexity_and_topic()


def start(setts='Английский - Русский'):
        '''
        Запускает тестирование, применяет настройки, распределяет шансы выпадения слов, задает сами вопросы.
        
        :param setts: Выбранные ранее настройки перевода
        :type setts: str
        :returns: -
        :rtype: None
        '''
        
        #Применение настроек к тестировующей системе
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

        '''Работа самой тестирующей системы.'''
        dict_translations = list(dct.values())
        score = 0
        for _ in range(ask_count()):
                word = random.choices(dict_keys, weights = chances, k = 1)[0]
                s = dict_translations.copy()
                variants = [0] * 4
                right_answer_index = random.randint(0, 3)
                variants[right_answer_index] = dct[word]
                s.remove(dct[word])
                for i in range(4):
                        if variants[i] == 0:
                                variants[i] = s.pop(random.randint(0, len(s) - 1))
                var1, var2, var3, var4 = variants           # Варианты ответов, var{right_answer + 1} - правильный
                yield word, var1, var2, var3, var4, right_answer_index

                # print(f'Переведи слово: {word}. 1) {var1}; 2) {var2}; 3) {var3}; 4) {var4}.')
                # answer = int(input())
                answer = Mock()
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
        menu()

if __name__ == "__main__":
        menu()
