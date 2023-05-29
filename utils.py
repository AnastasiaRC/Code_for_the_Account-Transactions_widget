import json
from datetime import datetime


def get_data_operations():
    """Открывает файл operations.json конвертирует его содержимое и сохраняет в переменную data"""
    with open("/home/anastasia/PycharmProjects/course_work__3/operations.json") as f:
        data = json.load(f)
    return data


def get_executed_operations(data):
    """Обрабатывает данные на наличие ключа state и далее фильтрует значение ключа по Executed,
     сохраняет это все в список operations"""
    operations = []
    for operation in data:
        if "state" in operation:
            if operation["state"] == "EXECUTED":
                operations.append(operation)
    return operations


def get_last_five_operations(operations):
    """Сортирует список operations по последним 5 операциям по убыванию"""
    data = sorted(operations, key=lambda x: x["date"], reverse=True)
    sorted_data = data[:5]
    return sorted_data


def get_format_sorted_data(sorted_data):
    """Форматирует дату date_transfer, извлекает описание перевода transfer_description,объединяет сумму и валюту
    amount_currency, у получателя отфильтровывает карту или счет - where_transfer, проверяет наличие отправителя и
    также отфильтровывает карту или счет from_transfer (если отправителя нет, выводит '...'), собирает все в список
    format_data с нужной расстановкой и возвращает строку с необходимым форматом"""
    format_data = []
    for element in sorted_data:
        date_transfer = datetime.strptime(element["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        transfer_description = element["description"]
        amount_currency = f'{element["operationAmount"]["amount"]} {element["operationAmount"]["currency"]["name"]}'
        if "Счет" in element["to"]:
            where_transfer = f'{element["to"].split()[0]} **{element["to"].split()[1][-4:]}'
        else:
            where_transfer = f'{element["to"][:-12]} {element["to"][-12:-10]}** **** {element["to"][-4:]}'
        if "from" in element and "Счет" in element["from"]:
            from_transfer = f'{element["from"].split()[0]} **{element["from"].split()[1][-4:]}'
        elif "from" in element and len(element["from"].split()) >= 2:
            from_transfer = f'{element["from"][:-12]} {element["from"][-12:-10]}** **** {element["from"][-4:]}'
        else:
            from_transfer = "..."
        format_data.append(f'''{date_transfer} {transfer_description}\n{from_transfer} -> {where_transfer}\n{amount_currency}\n''')
    return '\n'.join(format_data)
