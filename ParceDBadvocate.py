import Get_Re_else_func
import DataBase
import os
from alive_progress import alive_bar


def main(path_csv, path_some='resources/', path_db='resources/result.db'):
    path_db = os.path.join(os.getcwd(), path_db)
    assert(os.path.isfile(path_db))
    db = DataBase.Database(path_db=path_db)
    list_not_parce_advocate = db.get_not_parce_advocate()

    

    with alive_bar(len(list_not_parce_advocate), title='ParceDBadvocate:') as bar:
        for advocate in list_not_parce_advocate:
            adv_d = {
                'id': advocate[0],
                'doc_id': advocate[1],
                'court_code': advocate[2],
                'judgment_code': advocate[3],
                'justice_kind': advocate[4],
                'category_code': advocate[5],
                'cause_num': advocate[6],
                'adjudication_date': advocate[7],
                'receipt_date': advocate[8],
                'judje': advocate[9],
                'doc_url': advocate[10],
                'status': advocate[11],
                'date_publ': advocate[12],
                'save_locale': advocate[13],
                'advocate': advocate[14],
                'court': advocate[15],
            }

            if adv_d['status'] != '0':
                path = (path_some, f"{adv_d['receipt_date'].split('-')[0][1:]}/", f"{adv_d['judgment_code']}/", 
                f"{adv_d['justice_kind']}/", f"{adv_d['court_code']}/", f"{adv_d['doc_id']}.txt")

                path_file = os.getcwd()

                for value in path:
                    path_file = os.path.join(path_file, value)
                
                if adv_d['save_locale'] == '1':
                    text = Get_Re_else_func.get_text_file(path_file=path_file)
                else:
                    text = Get_Re_else_func.get_text_for_url(url=adv_d['doc_url'])
                    if 'Timeout' in text:
                        get_adv = text
                        break
                    
                get_adv = Get_Re_else_func.get_advokat_re(text)

                db.update_advocate(advocate=get_adv, id=adv_d['id'])
                
            bar()