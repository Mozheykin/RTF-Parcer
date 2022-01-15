import sqlite3

class Database:
    def __init__(self, path_db: str, name_table='main') -> None:
        self.main_table = name_table
        self.db = sqlite3.connect(path_db)
        self.cursor = self.db.cursor()
        self.db.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.main_table}(
            id INTEGER,
            doc_id INTEGER,
            court_code INTEGER,
            judgment_code INTEGER,
            justice_kind INTEGER,
            category_code INTEGER,
            cause_num TEXT,
            adjudication_date TEXT,
            receipt_date TEXT,
            judje TEXT,
            doc_url,
            status INTEGER,
            date_publ TEXT)''' )
        self.db.commit()
    
    def insert(self, values: list, name_table='main'):
        with self.db:
            return self.cursor.execute(f'INSERT INTO {name_table} VALUES({values})')