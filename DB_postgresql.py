import psycopg2


class DB_postgress:
    def __init__(self, name='rtf-parcer', user='postgres', password='qwerty', host='localhost'):
        self.name = name
        self.user = user
        self.password = password
        self.host = host
        self.conn = psycopg2.connect(dbname=self.name, user=self.user, password=self.password, host=self.host)
        self.create_table_main()

    def create_table_main(self):
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute('''CREATE TABLE IF NOT EXISTS main (
                    id SERIAL PRIMARY KEY,
                    doc_id INTEGER,
                    court_code INTEGER,
                    judgment_code TEXT,
                    justice_kind INTEGER,
                    category_code TEXT,
                    cause_num TEXT,
                    adjudication_date TEXT,
                    receipt_date TEXT,
                    judje TEXT,
                    doc_url TEXT,
                    status INTEGER,
                    date_publ TEXT,
                    save_locale INTEGER,
                    advocate TEXT,
                    court TEXT);
                ''')

    def save_data(self, values:list):
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT id FROM main WHERE id=%s', (values[0],))
                id = cursor.fetchone()
                if not id:
                    cursor.execute('INSERT INTO main VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);', values)
    
    def get_len_advocate(self):
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT COUNT(*) as count FROM main WHERE advocate=%s AND doc_url!=%s', ('', ''))
                return cursor.fetchone()
    
    def get_not_parce_advocate(self):
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT * FROM main WHERE advocate=%s AND doc_url!=%s', ('', ''))
                return cursor.fetchone()
    
    def update_advocate(self, advocate:str, id:str):
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute('UPDATE main SET advocate=%s WHERE id=%s', (advocate, id))
    
    def get_len_court(self):
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT COUNT(*) as count FROM main WHERE court=%s AND doc_url!=%s AND justice_kind=%s', ('', '', '2'))
                return cursor.fetchone()
    
    def get_not_parce_court(self):
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT * FROM main WHERE court=%s AND doc_url!=%s AND justice_kind=%s', ('', '', '2'))
                return cursor.fetchone()
    
    def update_court(self, court:str, id:str):
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute('UPDATE main SET court=%s WHERE id=%s', (court, id))
    
    def get_not_save(self):
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT * FROM main WHERE save_locale=%s AND doc_url!=%s', ('0', ''))
                return cursor.fetchone()
    
    def get_len_not_save(self):
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT COUNT(*) AS count FROM main WHERE save_locale=%s AND doc_url!=%s', ('0', ''))
                return cursor.fetchone()
    
    def update_save(self, id:str):
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute('UPDATE main SET save_locale=%s WHERE id=%s', ('1', id))
    



if __name__ == '__main__':
    db = DB_postgress()

