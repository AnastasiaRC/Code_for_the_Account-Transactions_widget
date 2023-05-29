import pytest
from utils import get_data_operations, get_executed_operations, get_last_five_operations, get_format_sorted_data


def test_get_data_operations():
    data = get_data_operations()
    assert isinstance(data, list)


def test_get_executed_operations(test_data):
    assert get_executed_operations(test_data[:2]) == [{
        "date": "2019-07-03T18:35:29.512364",
        "description": "Перевод организации",
        "id": 41428829,
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "code": "USD",
                "name": "USD"
            }
        },
        "state": "EXECUTED",
        "to": "Счет 35383033474447895560"
    }]
    # assert len(get_executed_operations(test_data)) == 0


def test_get_last_five_operations(test_data):
    data = get_last_five_operations(test_data)
    list_date = []
    for element in data:
        list_date.append(element["date"])
    assert list_date == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364', '2018-09-12T21:27:25.241689']


def test_get_format_sorted_data(test_data):
    data = get_format_sorted_data(test_data[:3])
    assert data == ('26.08.2019 Перевод с карты на карту\nMaestro 1596 83** **** 5199 -> Visa Classic 6831 98** **** 7658\n31957.58 руб.\n\n03.07.2019 Перевод организации\n... -> Счет **5560\n8221.37 USD\n\n12.09.2018 Перевод со счета на счет\nСчет **3400 -> Счет **3493\n31957.58 руб.\n')