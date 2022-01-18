import unittest
import Get_Re_else_func

class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_get_advocate(self):
        url_zah = 'http://od.reyestr.court.gov.ua/files/43/fcc00803897e6c8e322bf612f1cd4909.rtf'
        url_adv = 'http://od.reyestr.court.gov.ua/files/43/41e1a48a092180a3f64c2f98a74f97ae.rtf'
        result_zah = 'Защитник(Ратич Т.М.)'
        result_adv = 'Адвокат(Ороновська О.М.)'
        text = Get_Re_else_func.get_text_for_url(url_zah)
        self.assertEqual(Get_Re_else_func.get_advokat_re(text), result_zah)
        text = Get_Re_else_func.get_text_for_url(url_adv)
        self.assertEqual(Get_Re_else_func.get_advokat_re(text), result_adv)
        self.assertEqual(Get_Re_else_func.get_advokat_re(Get_Re_else_func.get_text_for_url('http://od.reyestr.court.gov.ua/files/43/a34e8e5c9c88f019fc43fe9bc4ab6cf3.rtf')), 'exception Zas')
        self.assertEqual(Get_Re_else_func.get_advokat_re(Get_Re_else_func.get_text_for_url('http://od.reyestr.court.gov.ua/files/43/ff2f4ce6a75295dc0c3356668b2b97db.rtf')), 'exception ADV')
        self.assertEqual(Get_Re_else_func.get_advokat_re(Get_Re_else_func.get_text_for_url('http://od.reyestr.court.gov.ua/files/43/4d1c6394daab3325363f2019024ff0df.rtf')), '-')
        self.assertEqual(Get_Re_else_func.get_advokat_re(Get_Re_else_func.get_text_for_url('http://od.reyestr.court.gov.ua/files/43/34ff2015677852f6698ede5cfb9150a6.rtf')), 'Адвокат(Брагіна Тетяна Віталіївна )')
    
    def test_get_court(self):
        self.assertEqual(Get_Re_else_func.get_criminal_court(Get_Re_else_func.get_text_for_url('http://od.reyestr.court.gov.ua/files/43/60c6cf1918b136838326e8344067f208.rtf')), "Особисте зобов'язання/Особиста порука")
        self.assertEqual(Get_Re_else_func.get_criminal_court(Get_Re_else_func.get_text_for_url('http://od.reyestr.court.gov.ua/files/43/aac40e931b9185758769f1cffa3d8d98.rtf')), 'Домашній арешт')
        self.assertEqual(Get_Re_else_func.get_criminal_court(Get_Re_else_func.get_text_for_url('http://od.reyestr.court.gov.ua/files/43/b434205208d5ec663674d1bae8bb2c28.rtf')), 'Виправна колонія')
        self.assertEqual(Get_Re_else_func.get_criminal_court(Get_Re_else_func.get_text_for_url('http://od.reyestr.court.gov.ua/files/43/e546171ed8e5e8a537342dfbe13494a6.rtf')), '-')

if __name__ == '__main__':
    unittest.main()