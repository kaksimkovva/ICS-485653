from pandas import *
def openExcel(path):
    """Функція відкриття ексель файлов
    Args:
        path (string): Path to excel file
    Returns:
        string: json output
    """
    xls = ExcelFile(path)
    df = xls.parse(xls.sheet_names[0])
    dict = df.to_dict()
    return dict
print (openExcel('/Users/anastasiyakaksimkova/Desktop/ICS-485653/Lab4/data/db.xlsx'))