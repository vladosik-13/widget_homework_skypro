from src.utils import get_transactions
from src.csv_excel_importer import csv_import, excel_import
from src.processing import filter_by_state, sort_list_by_date
from src.generators import filter_by_currency, get_search
from src.widget import mask_account_card, get_date


def main():
    """Функция взаимодействия с пользователем и выстраивания основной логики проекта"""
    transactions = []
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

    clear_transactions = []
    for transaction in transactions:
        if len(transaction) != 0:
            clear_transactions.append(transaction)
    transactions = clear_transactions

    # Выбор статуса
    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию."
                       "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").strip()
        if status.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Операции отфильтрованы по статусу \"{status.upper()}\".")
            transactions = filter_by_state(transactions, {status.upper()})
            break
        else:
            print(f"Статус операции \"{status}\" недоступен. Пожалуйста, введите корректный статус.")

        # Уточняем у пользователя дополнительные параметры сортировки
    user_input = ""
    while user_input.lower() != "нет":
        user_input = input("Отсортировать операции по дате? (Да/Нет)\n")
        if user_input.lower() == "да":
            user_input = input("Отсортировать по возрастанию/по убыванию?")
            if user_input.lower() == "по убыванию":
                transactions = sort_list_by_date(transactions)
                break
            elif user_input.lower() == "по возрастанию":
                transactions = sort_list_by_date(transactions, reverse=False)
                break

    while True:
        user_input = input("Выводить только рублевые тразакции? Да/Нет\n")
        if user_input.lower() == "да":
            transactions_generator = filter_by_currency(transactions, "RUB")
            break
        elif user_input.lower() == "нет":
            transactions_generator = transactions
            break

    while True:
        user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
        if user_input.lower() == "да":
            user_input = input("Введите слово для фильтрации\n")
            transactions = get_search(transactions_generator, user_input)
            break
        elif user_input.lower() == "нет":
            transactions = []
            for transaction in transactions_generator:
                transactions.append(transaction)
            break

    # Вывод списка транзакций
    print("Распечатываю итоговый список транзакций...")
    if len(transactions) != 0:
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for transaction in transactions:
            date = get_date(transaction.get("date"))
            description = transaction.get("description")
            card_to = mask_account_card(transaction.get("to"))
            try:
                amount = round(float(transaction.get("operationAmount").get("amount")))
                name = transaction.get("operationAmount").get("currency").get("name")
            except AttributeError:
                amount = round(float(transaction.get("amount")))
                name = transaction.get("currency_name")
            if transaction.get("from") is not None and str(transaction.get("from")) != "nan":
                card_from = mask_account_card(str(transaction.get("from")))
                print(f"{date} {description}\n{card_from} -> {card_to}\nСумма: {amount} {name}\n\n")
            else:
                print(f"{date} {description}\n{card_to}\nСумма: {amount} {name}\n\n")

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
