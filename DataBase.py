import sqlite3

class Database:
    def __init__(self, path_db: str, name_table='main') -> None:
        self.main_table = name_table
        self.db = sqlite3.connect(path_db)
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.main_table}(
                `id` INTEGER,
                `doc_id` INTEGER,
                `court_code` INTEGER,
                `judgment_code` INTEGER,
                `justice_kind` INTEGER,
                `category_code` INTEGER,
                `cause_num` TEXT,
                `adjudication_date` TEXT,
                `receipt_date` TEXT,
                `judje` TEXT,
                `doc_url` TEXT,
                `status` INTEGER,
                `date_publ` TEXT,
                `save_locale` BOOL,
                `advocate` TEXT,
                `court` TEXT)""")
        except self.db.Error as err:
            print(err)
        self.db.commit()
    
    def insert(self, values: list):
        with self.db:
            return self.cursor.execute(f'INSERT INTO {self.main_table} VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', values)
    
    def get_not_parce_advocate(self):
        with self.db:
            return self.cursor.execute(f'SELECT * FROM {self.main_table} WHERE `advocate`=? AND `doc_url`!=?', ('', '')).fetchall()
    
    def update_advocate(self, advocate: str, id: str):
        with self.db:
            return self.cursor.execute(f'UPDATE {self.main_table} SET `advocate`=? WHERE `id`=?', (advocate, id))