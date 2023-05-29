from utils import get_data_operations, get_executed_operations, get_last_five_operations, get_format_sorted_data


def main():
    data = get_data_operations()
    operations = get_executed_operations(data)
    sorted_data = get_last_five_operations(operations)
    format_date = get_format_sorted_data(sorted_data)
    print(f"INFO: Вывод транзакций...\n\n{format_date}")


if __name__ == "__main__":
    main()
