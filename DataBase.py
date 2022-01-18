import sqlite3

class Database:
    """[summary]
            Класс для работы с базой данных sqlite3
    """
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
        """[summary]
            функция для записи данных в БД из CSV файла
        Args:
            values (list): [description]
                Все параметры передаются листом (строка CSV файла) с добавленными полями.
                Добавляются поля: id, save_locale, advocate, court. Все добавленные поля по умолчанию заполняются 
                пустыми значениями, так как парсинг данных не производился
        Returns:
            [type]: [description]
                Возвращается True при успехе
        """
        with self.db:
            return self.cursor.execute(f'INSERT INTO {self.main_table} VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', values)
    
    def get_not_parce_advocate(self):
        """[summary]
                Функция для получения пустых полей адвокатов
        Returns:
            [type]: [description]
                Возвращает данные списком
        """
        with self.db:
            return self.cursor.execute(f'SELECT * FROM {self.main_table} WHERE `advocate`=? AND `doc_url`!=?', ('', '')).fetchall()
    
    def update_advocate(self, advocate: str, id: str):
        """[summary]
                Функция изменения значения поля адвокат, вписывает полученные значения,
                если значение не найдено то пишется -
        Args:
            advocate (str): [description]
            id (str): [description]
                Передаются на вход спарсенное значение и id номер куда будет вписываться значение
        Returns:
            [type]: [description]
                Возвращает True при успехе
        """
        with self.db:
            return self.cursor.execute(f'UPDATE {self.main_table} SET `advocate`=? WHERE `id`=?', (advocate, id))

    def get_not_parce_court(self):
        """[summary]
                Получаем список не спарсенных уголовных дел
        Returns:
            [type]: [description]
                Возвращает данные списком
        """
        with self.db:
            return self.cursor.execute(f'SELECT * FROM {self.main_table} WHERE `court`=? AND `doc_url`!=? AND `justice_kind`=?', ('', '', '2')).fetchall()
    
    def update_court(self, court: str, id: str):
        """[summary]
                Вписываем полученное значение
        Args:
            court (str): [description]
            id (str): [description]
                На вход подается спарсенное значение и id
        Returns:
            [type]: [description]
                Возвращает True при успехе
        """
        with self.db:
            return self.cursor.execute(f'UPDATE {self.main_table} SET `court`=? WHERE `id`=?', (court, id))
    
    def get_not_save(self):
        """[summary]
                Получаем список не сохраненных полей
        Returns:
            [type]: [description]
                Возвращаем все данные
        """
        with self.db:
            return self.cursor.execute(f'SELECT * FROM {self.main_table} WHERE `save_locale`=? AND `doc_url`!=?', ('0', '')).fetchall()
    
    def update_save(self, id: str):
        """[summary]
                Вписываем True при сохранении файла
        Args:
            id (str): [description]
                Получаем на вход id куда необходимо вписать 1
        Returns:
            [type]: [description]
                Возвращает True при успехе
        """
        with self.db:
            return self.cursor.execute(f'UPDATE {self.main_table} SET `save_locale`=? WHERE `id`=?', ('1', id))
    
    def end_id(self):
<<<<<<< HEAD
        return self.db.execute(f'SELECT id FROM {self.main_table} ORDER BY id DESC LIMIT 1').fetchone()
=======
        return self.db.execute(f'SELECT id FROM {self.main_table} ORDER BY id DESC LIMIT 1').fetchone()
>>>>>>> develop
