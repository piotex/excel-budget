from typing import List
from filter import get_list_of_unique_csv_data, ban_operations_between_own_bank_numbers
from models.CsvData import CsvData
from reader import read_csv_to_dataclass_list, get_list_of_priv_files, save_list_of_unique_csv_data

file_list = get_list_of_priv_files()
list_of_csv_data: List[CsvData] = []

for path in file_list:
    csv_data_objects = read_csv_to_dataclass_list(path)
    list_of_csv_data += csv_data_objects

list_of_csv_data = ban_operations_between_own_bank_numbers(list_of_csv_data)
list_of_unique_csv_data = get_list_of_unique_csv_data(list_of_csv_data)

save_list_of_unique_csv_data(list_of_unique_csv_data)
