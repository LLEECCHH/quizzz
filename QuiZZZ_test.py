import os
import random
import sqlite3
from unittest.mock import Mock, patch
import pytest

from QuiZZZ import (
        dict_db,
        ask_count,
        menu,
        settings,
        complexity_and_topic,
        start,
)

def test_dict_db_success():
        # Mock the sqlite3.connect and cursor behavior for a successful scenario
        mock_db = Mock()
        mock_cursor = Mock()
        mock_db.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [
                (" word1 ", " перевод1 "),
                (" word2 ", " перевод2 "),
        ]

        with patch("sqlite3.connect", return_value=mock_db):
                result = dict_db()

        assert result == [("word1", "перевод1"), ("word2", "перевод2")]
        mock_db.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT * FROM words")
        mock_cursor.fetchall.assert_called_once()
        mock_db.commit.assert_called_once()
        mock_db.close.assert_called_once()

def test_dict_db_failure():
        # Mock sqlite3.connect to raise an exception
        with patch("sqlite3.connect", side_effect=Exception("Test Exception")):
                result = dict_db()

        assert result == "Ошибка при открытии файла: Test Exception"

def test_ask_count():
        assert ask_count() == 10

def test_menu():
        # Mock the function calls within menu()
        mock_func = Mock()
        with patch("QuiZZZ.Mock", return_value=mock_func):
                menu()

        mock_func.assert_called_once()

def test_settings_english_to_russian():
    with patch('QuiZZZ.Mock', return_value='Английский - Русский'):
        result = settings()
        assert result == 'Английский - Русский'

def test_settings_russian_to_english():
    with patch('QuiZZZ.Mock', return_value='Русский - Английский'):
        result = settings()
        assert result == 'Русский - Английский'

def test_settings_random():
    with patch('QuiZZZ.Mock', return_value='Случайно'):
        with patch('random.choice', return_value='Английский - Русский'):
            result = settings()
            assert result == 'Английский - Русский'
        with patch('random.choice', return_value='Русский - Английский'):
            result = settings()
            assert result == 'Русский - Английский'
