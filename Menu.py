from Addressbook import *
from Filemanager import Filemanager
from Phonebook import *


class Menu:
    run = Filemanager()

    def main_menu():
        inp = int(input(
            "1 - Отобразить справочник \n2 - Выгрузить данные \n3 - Загрузить данные \n...........\nВыберите действие: "))

        if inp == 1:
            show_addressbook()

        elif inp == 2:
            Filemanager.fileExport(pb)
            print("Export finish")

        elif inp == 3:
            Filemanager.fileImport(pb)
            print("Import finish")
