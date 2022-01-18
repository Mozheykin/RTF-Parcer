import re
from striprtf.striprtf import rtf_to_text
import requests


def get_advokat_re(text: str) -> str:
    """[summary]

    Args:
        text (str): [description]

    Returns:
        str: [description]
    """

    if 'адвок' in text:
        advocate = re.search(r'(?:[Аа]двокат(а́|а|ів|ом|і́в|о́м|а́ми|ами|у́|у|а́х|ах|и|и́)*(\s+|( \s)+)(-\s)*)(([А-ЯЁЇІЄҐ][а-яёїієґ]+\s[А-ЯЁЇІЄҐ][а-яёїієґ]+\s[А-ЯЁЇІЄҐ][а-яёїієґ]+\s)|([А-ЯЁЇІЄҐ][а-яёїієґ]+\s[А-ЯЁЇІЄҐ]\.\s*[А-ЯЁЇІЄҐ]\.))', text)
        if not advocate  is None: 
            return f'Адвокат({advocate[5]})'
        else:
            return 'exception ADV'
    elif 'захисн' in text:
        zahs = re.search(r'(?:[Зз]ахисник(а́|а|ів|ом|і́в|о́м|а́ми|ами|у́|у|а́х|ах|и|и́)*(\s+|( \s)+)(-\s)*)(([А-ЯЁЇІЄҐ][а-яёїієґ]+\s[А-ЯЁЇІЄҐ][а-яёїієґ]+\s[А-ЯЁЇІЄҐ][а-яёїієґ]+\s)|([А-ЯЁЇІЄҐ][а-яёїієґ]+\s[А-ЯЁЇІЄҐ]\.\s*[А-ЯЁЇІЄҐ]\.))', text)
        if not zahs  is None: 
            return f'Защитник({zahs[5]})'
        else:
            return 'exception Zas'
    elif 'юрист' in text:
        jur = re.search(r'(?:[Юю]рист(а́|а|ів|ом|і́в|о́м|а́ми|ами|у́|у|а́х|ах|и|и́)*(\s+|( \s)+)\d(\s+|( \s)+)(класу|класа)\s(-\s)*)(([А-ЯЁЇІЄҐ][а-яёїієґ]+\s[А-ЯЁЇІЄҐ][а-яёїієґ]+\s[А-ЯЁЇІЄҐ][а-яёїієґ]+\s)|([А-ЯЁЇІЄҐ][а-яёїієґ]+\s[А-ЯЁЇІЄҐ]\.\s*[А-ЯЁЇІЄҐ]\.))', text)
        if not jur  is None: 
            return f'Юрист({jur[3]})'
        else:
            return 'exception Jur'
    else:
        return ''


def get_criminal_court(text: str) -> str:
    """[summary] Функция поиска меры пресечения в файле

    Args:
        text (str): [description] Получается текст файла для поиска в нём данных

    Returns:
        str: [description] Возвращаются найденные значения из перечня
        перебувати, знаходитись, утримується
        [Пп]еребува(ти|ють|в)\s
        [Зз]находи(ти|тись|ться|вся)\s
        [Уу]триму(ється|вався|ватись|)\s

        ([Пп]еребува(ти|ють|в|є)|[Зз]находи(ти|тись|ться|вся)|[Уу]триму(ється|вався|ватись))\s((в\s)|(у\s))*(ДУ\s)*([А-ЯЁЇІЄҐ][а-яёїієґ]+\s)*((ОСОБА\_\d)|([Оо]соба\_\d)|(СІЗО)|([Сс]лідчий ізолятор))

        У Х В А Л И В:
    """
    
    court_sizo = {
                '1': re.findall(r'[Оо]брати\sобвинуваченому.*в\sДУ.*СІЗО', text),
                '2': re.findall(r'[Зз]астосувати.*в\sмежах\sдосудового\sрозслідування', text),
                '3': re.findall(r'[Пп]родовжити.*в.*СІЗО', text),
                '4': re.findall(r'[Зз]алишити.*(змін)*.*(СІЗО|продовжити)', text),
            }

    for regular in court_sizo.values():
        if regular:
            return 'СІЗО'

    court_colonija = {
        '1': re.findall(r'тимчасово\sзалишити\sв\sДержавній\sустанові.*слідчий\sізолятор', text),
        '2': re.findall(r'[Пп]родовжити.*(в|у)\s(Держа(в)*ній|ДУ).*((виправн(а|ій)\sколоні(я|ї))|(слідчий\sізолятор))', text),
    }

    for regular in court_colonija.values():
        if regular:
            return 'Виправна колонія'

    
    court_electronic_braslet = {
        '1': re.findall(r'[Зз]астосувати.*із\sзастосуванням\sзасобу\sелектронного\sконтролю', text),
        '2': re.findall(r'[Оо]брати.*з\sносінням\sелектронного\sбраслету', text),
        '3': re.findall(r'з\sзобовязанням\sносіння\sелектроного\sпристрою\sу\sвигляді\sбраслету', text),
        '4': re.findall(r'продовжити.*із\sзастосуванням\sелектронних\sзасобів\sконтролю', text),
    }

    for regular in court_electronic_braslet.values():
        if regular:
            return 'Електронний браслет'
    

    court_home_arrest = {
        '1': re.findall(r'[Оо]брати.*у\sвигляді\sдомашнього\sарешту', text),
        '2': re.findall(r'[Пп]родовжити.*у\s(вигляді|виді)\sдомашнього\sарешту', text),
        '3': re.findall(r'[Зз]астосувати.*домашнього\sарешту', text),
        '4': re.findall(r'[Зз]мінити.*домашн(ій|ього)\sарешт(у)*', text),
    }

    for regular in court_home_arrest.values():
        if regular:
            return 'Домашній арешт'
    

    court_subscribe = {
        '1': re.findall(r'змін(ити|ено).*на\sпідписку\sпро\sневиїзд', text),
        '2': re.findall(r'залишити.*про\sневиїзд', text),
    }

    for regular in court_subscribe.values():
        if regular:
            return 'Підписка про невиїзд'
    

    court_personal_commitment = {
        '1': re.findall(r'[Зз]мінити.*на\sособисте\sзобов`язання', text),
        '2': re.findall(r'[Пп]родовжити.*у\sвигляді\sособистої\sпоруки', text),
        '3': re.findall(r'[Оо]брати.*у\sвигляді\sособистого\sзобов`язання', text),
        '4': re.findall(r'[Зз]астосувати.*у\sвигляді\sособистої\sпоруки', text),
        '5': re.findall(r'[Зз]астосувати.*запобіжний\sзахід', text),
        '6': re.findall(r'[Зз]астосувати\sвідносно\sпідозрюваного', text),
    }

    for regular in court_personal_commitment.values():
        if regular:
            return "Особисте зобов'язання/Особиста порука"
    
    return ''


def get_text_file(path_file: str):
    with open(path_file, 'r') as file:
        text = file.read
    return text

def get_text_for_url(url: str) -> str:
    """[summary]

    Args:
        url (str): [description]

    Returns:
        str: [description]
    """
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'}
    try:
        response = requests.get(url=url, headers=headers, timeout=5)
    except requests.exceptions.Timeout:
        return 'Timeout'
    result = rtf_to_text(response.text)
    return result