from dataclasses import dataclass


@dataclass
class CsvData:
    Data_księgowania: str = ""
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


    def __add_my_category_by_Tytulem(self):
        if "Przelew środków własnych DM bossa" == self.Tytułem:
            self.my_category = "savings"
            self.my_sub_category = "akcje-etf"
        if "Przelew środków własnych obligacje" == self.Tytułem:
            self.my_category = "savings"
            self.my_sub_category = "obligacje"
        if "Wynagrodzenie" in self.Tytułem:
            self.my_category = "income"
            self.my_sub_category = "wyplata"
        if "ODSETKI OD OBLIGACJI" in self.Tytułem:
            self.my_category = "income"
            self.my_sub_category = "obligacje"
        if "Zwrot za czynsz" in self.Tytułem:
            self.my_category = "expense"
            self.my_sub_category = "czynsz"

    def __add_my_category_by_Typ_operacji(self):
        if "PŁATNOŚĆ BLIK" in self.Typ_operacji:
            self.my_category = "expense"
            self.my_sub_category = self.Typ_operacji.split(" ")[0].split(".")[0]
        if "PRZELEW BLIK WYCHODZĄCY" in self.Typ_operacji:
            self.my_category = "expense"
            self.my_sub_category = self.Typ_operacji
        if "PRZELEW BLIK WYCHODZĄCY" in self.Typ_operacji:
            self.my_category = "expense"
            self.my_sub_category = self.Typ_operacji
        if "TRANSAKCJA KARTĄ PŁATNICZĄ" == self.Typ_operacji:
            self.my_category = "expense"
            list_of_splitted_words = self.Nadawca_Odbiorca.split()
            if len(list_of_splitted_words) > 2 and list_of_splitted_words[-2].isdigit():
                result = ' '.join(list_of_splitted_words[:-2])
                self.my_sub_category = result.strip()
            else:
                result = ' '.join(list_of_splitted_words)
                self.my_sub_category = result.strip()



    def __add_my_category_other_income(self):
        if "" == self.my_sub_category and self.my_category == "income":
            self.my_sub_category = "other"

    def __add_my_category_other_savings(self):
        if "" == self.my_sub_category and self.my_category == "savings":
            self.my_sub_category = "other"

    def __add_my_category_other_expense(self):
        if "" == self.my_sub_category and self.my_category == "expense":
            self.my_sub_category = "other"


    def add_my_category(self):
        self.__add_my_category_by_Kwota_operacji()
        self.__add_my_category_by_Typ_operacji()
        self.__add_my_category_by_Tytulem()

        self.__add_my_category_other_income()
        self.__add_my_category_other_savings()
        self.__add_my_category_other_expense()
