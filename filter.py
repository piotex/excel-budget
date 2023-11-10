from typing import List
from models.CsvData import CsvData


def get_list_of_unique_csv_data(list_of_csv_data: List[CsvData]):
    list_of_unique_csv_data: List[CsvData] = []
    dict_for_filter = {}
    for elem in list_of_csv_data:
        if elem.Numer_referencyjny not in dict_for_filter:
            list_of_unique_csv_data.append(elem)
            dict_for_filter[elem.Numer_referencyjny] = 1
    return list_of_unique_csv_data


def ban_operations_between_own_bank_numbers(list_of_csv_data: List[CsvData]):
    res = []
    file_path = "priv-data/my_own_bank_addresses.txt"
    with open(file_path, 'r', encoding='utf-8') as file:
        content_list = file.readlines()
    ban_bank_address_list = [line.strip() for line in content_list]

    for elem in list_of_csv_data:
        if not (elem.Rachunek_docelowy in ban_bank_address_list and elem.Rachunek_źródłowy in ban_bank_address_list):
            res.append(elem)
    return res
