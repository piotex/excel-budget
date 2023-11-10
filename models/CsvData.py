from dataclasses import dataclass


@dataclass
class CsvData:
    Data_księgowania:str = ""
    Data_waluty: str = ""
    Nadawca_Odbiorca: str = ""
    Adres_nadawcy_odbiorcy: str = ""
    Rachunek_źródłowy: str = ""
    Rachunek_docelowy: str = ""
    Tytułem: str = ""
    Kwota_operacji: float = 0
    Waluta: str = ""
    Numer_referencyjny: str = ""
    Typ_operacji: str = ""
    my_category: str = ""
    my_sub_category: str = ""

    def __add_my_category_by_Kwota_operacji(self):
        if self.Kwota_operacji > 0:
            self.my_category = "income"
        if self.Kwota_operacji < 0:
            self.my_category = "expense"

    def __add_my_category_by_Typ_operacji(self):
        if self.Typ_operacji == "TRANSAKCJA KARTĄ PŁATNICZĄ":
            self.my_category = "expense"

    def __add_my_category_by_Tytułem(self):
        if self.Tytułem == "Przelew środków własnych DM bossa":
            self.my_category = "savings"
            self.my_sub_category = "akcje-etf"
        if self.Tytułem == "Przelew środków własnych obligacje":
            self.my_category = "savings"
            self.my_sub_category = "obligacje"





    def add_my_category(self):
        self.__add_my_category_by_Kwota_operacji()
        self.__add_my_category_by_Typ_operacji()
        self.__add_my_category_by_Tytułem()


