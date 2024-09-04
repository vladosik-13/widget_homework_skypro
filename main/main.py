from src.utils import get_transactions
from src.csv_excel_importer import csv_import, excel_import


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Введите необходимый пункт меню: ")
    if choice == "1":
        transactions = get_transactions('C:/Users/user/PycharmProjects/home_work_widget/data/operations.json')
        file_type = "JSON"
    elif choice == "2":
        transactions = csv_import('C:/Users/user/PycharmProjects/home_work_widget/data/transactions.csv')
        file_type = "CSV"
    elif choice == "3":
        transactions = excel_import('C:/Users/user/PycharmProjects/home_work_widget/data/transactions_excel.xlsx')
        file_type = "XLSX"
    else:
        print("Неверный ввод. Выберите необходимый пункт меню:")
        return

    print(f"Для обработки выбран {file_type}-файл.")

if __name__ == "__main__":
    main()