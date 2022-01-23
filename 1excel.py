import pymysql
import pandas as pd
from pymysql.connections import Connection




mydb = pymysql.connect(host='localhost', user='smvigeugene',
                       password='23A<aL7LqlzV:>', database='dbnew', charset='utf8')
print ("\nConnection to DataBase established..\n")

# Assign spreadsheet filename to `file`
file = '/home/smv/severovo_sv.xlsx'
# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print('Получить из файла', file)
print('Вывести лист Excel', xl.sheet_names)  #печать названия страницы


# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('db_sv')
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  #вместо None можно указать число строк или столбцов
    print(df1)

df1.to_sql(name='sev', con=mydb, if_exists='replace', index=False)


print('\nКоличесво строк и столбцов', df1.shape, '\n')  #функция показывает количество строк и количество столбцов в таблице
print('....................\nОбщая сводка о таблице\n')
print( df1.info())  #получаем общую сводку о таблице, в т.ч. какие столбцы, их названия,
                   # тип данных в столбцах, количество не пустых элементов


