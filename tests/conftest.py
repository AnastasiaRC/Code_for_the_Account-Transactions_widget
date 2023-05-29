import pytest


@pytest.fixture
def test_data():
    return [
        {"date": "2019-08-26T10:50:58.294041",
         "from": "Maestro 1596837868705199",
         "description": "Перевод с карты на карту",
         "id": 441945886,
         "operationAmount": {"amount": "31957.58", "currency": {"code": "RUB", "name": "руб."}},
         "to": "Visa Classic 6831982476737658"},
        {"date": "2019-07-03T18:35:29.512364",
         "description": "Перевод организации",
         "id": 41428829,
         "operationAmount": {"amount": "8221.37", "currency": {"code": "USD", "name": "USD"}},
         "state": "EXECUTED",
         "to": "Счет 35383033474447895560"},
        {"date": "2018-09-12T21:27:25.241689",
         "from": "Счет 84163357546688983400",
         "description": "Перевод со счета на счет",
         "id": 441945886,
         "operationAmount": {"amount": "31957.58", "currency": {"code": "RUB", "name": "руб."}},
         "state": "EXECYTED",
         "to": "Счет 84163357546688983493"}]
