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

