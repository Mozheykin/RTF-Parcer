import DataBase
import DB_postgresql
import os
from alive_progress import alive_bar


def main(path_some, path_db='resources/result.db', path_csv='resources/documents.csv'):
    db = DataBase.Database(path_db=os.path.join(os.getcwd(), path_db))
    all_lines = db.get_all()
    db_postgres = DB_postgresql.DB_postgress()
    with alive_bar(len(all_lines), title='ParceDBcourt:') as bar:
        for line in all_lines:
            db_postgres.save_data(line)
            bar()