import os
from alive_progress import alive_bar
import DataBase

def main(path_db='/resources/result.db', path_csv='/resources/documents.csv'):
    print('SaveCSVinDB')
    db = DataBase.Database(path_db)
    with open(file=os.path.join(os.getcwd(), path_csv), newline='') as file:
        next(file)
        for num, line in enumerate(file):
            values = list(line.split('\t'))
            values.insert(1, num)
            db.insert(values=values)