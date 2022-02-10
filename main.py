import argparse
import SaveCSVinDB, DataBase, ParceDBadvocate, ParceDBcourt, SaveRTFinLocale, Convert_DB_Postgresql
from termcolor import colored


functions_inicialization_dict = {
    'Save_CSV_in_DataBase': SaveCSVinDB,
    'Parce_DB_advocate': ParceDBadvocate,
    'Parce_DB_court': ParceDBcourt,
    'Save_RTF_in_Locale': SaveRTFinLocale,
    'Convert_DB_Postgresql': Convert_DB_Postgresql,
}

def parce_args() -> argparse.Namespace:
    """[summary]
    В функции получаются основные флаги объявленные в командной строке
    Returns:
        argparse.Namespace: [description]
        Возвращает распарсенные аргументы объявленные флагами,
        использует argparce для их добычи.
        -f обязательный флаг, указывает на инициализированную функцию, 
            на данный момент их 4 штуки, а именно:
            Save_CSV_in_DataBase - Сохранение CSV файла в базу данных;
            Parce_DB_advocate - парсинг адвокатов;
            Parce_DB_court - парсинг меры пресечения;
            Save_RTF_in_Locale - сохранение RTF файлов в локальное хранилище;
    """
    parce_arg = argparse.ArgumentParser(description='function')
    parce_arg.add_argument('-f', dest='functions', required=True)
    parce_arg.add_argument('-s', dest='save_directory', default='resources/')
    parce_arg.add_argument('-db', dest='data_base', default='resources/result.db')
    parce_arg.add_argument('-csv', dest='csv', default='resources/documents.csv')
    return parce_arg.parse_args()



def main():
    """
    Основная функция отвечающая за запуск функций.
    Передает в каждую функцию 3 параметра, а именно:
    - дирректория для сохранения локальных данных RTF;
    - дирректория для сохранения базы данных и её имя;
    - дирректория где находится CSV файл и его название;
    """
    args = parce_args()
    if str(args.functions) in functions_inicialization_dict:
        functions_inicialization_dict[args.functions].main(path_db=args.data_base, path_csv=args.csv, path_some=args.save_directory)
    else:
        print(colored(f'Not search inicialization function name, may be you want write this function:\n\t>>> {", ".join(key for key in functions_inicialization_dict)}', 'red'))


if __name__ == '__main__':
    main()