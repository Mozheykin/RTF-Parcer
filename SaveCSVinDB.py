import os
from alive_progress import alive_bar
import DataBase

def main(path_some, path_db='resources/result.db', path_csv='resources/documents.csv', args=''):
    """[summary]
            Получение построчно данных из CSV файла и запись в Базу Данных
    Args:
        path_some ([type]): [description]
        path_db (str, optional): [description]. Defaults to 'resources/result.db'.
        path_csv (str, optional): [description]. Defaults to 'resources/documents.csv'.
    """
    db = DataBase.Database(path_db=os.path.join(os.getcwd(), path_db))
    length = 0
    with open(file=os.path.join(os.getcwd(), path_csv), newline='') as file:
        length = len(file.readlines())

    with alive_bar(length, title='SaveCSVinDB:') as bar:
        with open(file=os.path.join(os.getcwd(), path_csv), newline='') as file:
            next(file)
            end_id = db.end_id()
            if end_id:
                for i in range(int(end_id[0])):
                    next(file) 
                    bar()
                num = int(end_id[0])
            else:
                num = 0
            for line in file:
                num += 1
                values = list(line.strip().split('\t'))
                values.insert(0, num)
                values.extend([False, '', ''])
                db.insert(values=values)
                # if num % 1000 == 0:
                #     print(num)
                bar()
