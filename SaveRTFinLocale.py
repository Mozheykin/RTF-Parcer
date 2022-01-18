import Get_Re_else_func
import DataBase
import os
from alive_progress import alive_bar


def main(path_csv, path_some='resources/', path_db='resources/result.db'):
    """[summary]
            Получение списка не сохраненных данных, получение текста по url и
            сохранение файла в локале.
    Args:
        path_csv ([type]): [description]
        path_some (str, optional): [description]. Defaults to 'resources/'.
        path_db (str, optional): [description]. Defaults to 'resources/result.db'.
    """
    path_db = os.path.join(os.getcwd(), path_db)
    assert(os.path.isfile(path_db))
    db = DataBase.Database(path_db=path_db)
    list_not_save = db.get_not_save()

    

    with alive_bar(len(list_not_save), title='SaveLocale:') as bar:
        for save in list_not_save:
            sav_d = {
                'id': save[0],
                'doc_id': save[1],
                'court_code': save[2],
                'judgment_code': save[3],
                'justice_kind': save[4],
                'category_code': save[5],
                'cause_num': save[6],
                'adjudication_date': save[7],
                'receipt_date': save[8],
                'judje': save[9],
                'doc_url': save[10],
                'status': save[11],
                'date_publ': save[12],
                'save_locale': save[13],
                'advocate': save[14],
                'court': save[15],
            }

            if sav_d['status'] != '0':
                path = (path_some, f"{sav_d['receipt_date'].split('-')[0][1:]}/", f"{sav_d['judgment_code']}/", 
                f"{sav_d['justice_kind']}/", f"{sav_d['court_code']}/",)

                path_file = os.getcwd()

                for value in path:
                    path_file = os.path.join(path_file, value)
                
                if not os.path.isdir(path_file):
                    os.makedirs(path_file)
                
                path_file = os.path.join(path_file, f"{sav_d['doc_id']}.txt")
                
                text = Get_Re_else_func.get_text_for_url(url=sav_d['doc_url'])

                with open(path_file, 'w') as file:
                    file.write(text)

                db.update_save(sav_d['id'])
                
            bar()