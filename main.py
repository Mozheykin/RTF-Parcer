import argparse
import SaveCSVinDB, DataBase
from termcolor import colored


functions_inicialization_dict = {
    'Save_CSV_in_DataBase': SaveCSVinDB,
    'DataBase': DataBase,
}

def parce_args() -> argparse.Namespace:
    parce_arg = argparse.ArgumentParser(description='function')
    parce_arg.add_argument('-f', dest='functions', required=True)
    parce_arg.add_argument('-s', dest='save_directory', default='')
    parce_arg.add_argument('-db', dest='data_base', default='/resources/result.db')
    parce_arg.add_argument('-csv', dest='csv', default='/resources/documents.csv')
    return parce_arg.parse_args()



def main():
    args = parce_args()
    if str(args.functions) in functions_inicialization_dict:
        functions_inicialization_dict[args.functions].main()
    else:
        print(colored(f'Not search inicialization function name, may be you want write this function:\n\t>>> {", ".join(key for key in functions_inicialization_dict)}', 'red'))


if __name__ == '__main__':
    main()