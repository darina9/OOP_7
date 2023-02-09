from Phonebook import *


pb = []
pb.append(Phonebook("Черный Игорь Иванович", "956894922", "Тбилиси"))
pb.append(Phonebook("Красный Илья Петрович", "9563839495", "Батуми"))
pb.append(Phonebook("Белый Константин Ильич",
          "9563839294", "Кутаиси"))


def show_addressbook():
    for i in pb:
        print(i.get_name(), i.get_phone(), i.get_city())
