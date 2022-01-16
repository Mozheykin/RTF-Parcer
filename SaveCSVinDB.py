import os
from alive_progress import alive_bar
import DataBase

def main(path_some, path_db='resources/result.db', path_csv='resources/documents.csv'):
    db = DataBase.Database(path_db=os.path.join(os.getcwd(), path_db))
    with alive_bar(7158065, title='SaveCSVinDB:', length=60, spinner='dots_waves', bar='classic2') as bar:
        with open(file=os.path.join(os.getcwd(), path_csv), newline='') as file:
            next(file)
            for num, line in enumerate(file):
                values = list(line.strip().split('\t'))
                values.insert(0, num + 1)
                values.extend([False, '', ''])
                db.insert(values=values)
                # if num % 1000 == 0:
                #     print(num)
                bar()