import unittest
from unittest.mock import MagicMock, mock_open, patch

from src.csv_excel_importer import csv_import, excel_import


class TestExcelImport(unittest.TestCase):
    @patch('pandas.read_excel')
    def test_excel_import(self, mock_read_excel):
        # Создаем имитируемый объект DataFrame
        mock_df = MagicMock()
        mock_df.to_dict.return_value = [
            {'date': '2023-01-01', 'amount': 100, 'category': 'groceries'},
            {'date': '2023-01-02', 'amount': 200, 'category': 'entertainment'}
        ]

        # Настраиваем mock, чтобы pd.read_excel возвращал наш имитируемый DataFrame
        mock_read_excel.return_value = mock_df

        # Вызов тестируемой функции
        transactions = excel_import('dummy_path.xlsx')

        # Ожидаемый результат
        expected_output = [
            {'date': '2023-01-01', 'amount': 100, 'category': 'groceries'},
            {'date': '2023-01-02', 'amount': 200, 'category': 'entertainment'}
        ]

        # Проверка на соответствие
        self.assertEqual(transactions, expected_output)
        mock_read_excel.assert_called_once_with('dummy_path.xlsx')

    @patch('pandas.read_excel')
    def test_excel_import_with_exception(self, mock_read_excel):
        # Настраиваем mock, чтобы вызывать исключение
        mock_read_excel.side_effect = Exception("File not found")

        # Вызов тестируемой функции
        transactions = excel_import('dummy_path.xlsx')

        # Ожидаем, что функция вернет пустой список при ошибке
        self.assertEqual(transactions, [])


class TestCsvImport(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='date,amount,category\n2023-01-01,100,groceries\n'
                                                              '2023-01-02,200,entertainment')
    def test_csv_import(self, mock_file):
        # Имитация вызова функции
        transactions = csv_import('dummy_path.csv')

        # Ожидаемый результат (так как мы пропустили первую строку)
        expected_output = [
            ['2023-01-01', '100', 'groceries'],
            ['2023-01-02', '200', 'entertainment']
        ]

        # Проверка на соответствие:
        self.assertEqual(transactions, expected_output)
        mock_file.assert_called_once_with('dummy_path.csv', 'r', encoding='utf-8')

    @patch('builtins.open', new_callable=mock_open)
    def test_csv_import_with_exception(self, mock_file):
        # Настраиваем mock для выбрасывания исключения
        mock_file.side_effect = IOError("File not found")

        # Вызов функции
        transactions = csv_import('dummy_path.csv')

        # Проверяем, что функция возвращает пустой список в случае ошибки
        self.assertEqual(transactions, [])
