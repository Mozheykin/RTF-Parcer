import Get_Re_else_func
import DataBase
import os
from alive_progress import alive_bar


def main(path_csv, path_some='resources/', path_db='resources/result.db'):
    """[summary]
            Получение текста из локали или по url ссылке, парсинг данных и сохранение их
            в базе данных.
    Args:
        path_csv ([type]): [description]
        path_some (str, optional): [description]. Defaults to 'resources/'.
        path_db (str, optional): [description]. Defaults to 'resources/result.db'.
    """
    path_db = os.path.join(os.getcwd(), path_db)
    assert(os.path.isfile(path_db))
    db = DataBase.Database(path_db=path_db)
    len_court = db.get_len_court()[0]

    with alive_bar(len_court, title='ParceDBcourt:') as bar:
        while db.get_len_court()[0] > 1:
            court = db.get_not_parce_court()
            cour_d = {
                'id': court[0],
                'doc_id': court[1],
                'court_code': court[2],
                'judgment_code': court[3],
                'justice_kind': court[4],
                'category_code': court[5],
                'cause_num': court[6],
                'adjudication_date': court[7],
                'receipt_date': court[8],
                'judje': court[9],
                'doc_url': court[10],
                'status': court[11],
                'date_publ': court[12],
                'save_locale': court[13],
                'advocate': court[14],
                'court': court[15],
            }

            if cour_d['status'] != '0':
                path = (path_some, f"{cour_d['receipt_date'].split('-')[0][1:]}/", f"{cour_d['judgment_code']}/", 
                f"{cour_d['justice_kind']}/", f"{cour_d['court_code']}/", f"{cour_d['doc_id']}.txt")

                path_file = os.getcwd()

                for value in path:
                    path_file = os.path.join(path_file, value)
                
                if all([cour_d['save_locale'] == '1', os.path.isfile(path_file)]):
                    text = Get_Re_else_func.get_text_file(path_file=path_file)
                else:
                    text = Get_Re_else_func.get_text_for_url(url=cour_d['doc_url'])
                    if 'Timeout' in text:
                        get_adv = text
                        break
                    
                get_adv = Get_Re_else_func.get_criminal_court(text)

                db.update_court(court=get_adv, id=cour_d['id'])
                
            bar()