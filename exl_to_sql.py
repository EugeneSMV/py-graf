import pandas as pd
from sqlalchemy import create_engine

with open('/home/smv/enter/mysql_user.txt', 'r', encoding='utf-8-sig') as fp:  #читать имя из файла
    mysql_usr = fp.read().rstrip()
with open('/home/smv/enter/mysql_password.txt', 'r', encoding='utf-8-sig') as fp:  #читать пароль из файла
    mysql_pass = fp.read().rstrip()
with open('/home/smv/enter/mysql_host.txt', 'r', encoding='utf-8-sig') as fp:  #читать хост из файла
    mysql_host = fp.read().rstrip()



# Set database credentials.
creds = {'usr': mysql_usr,
        'pwd': mysql_pass,
        'hst': mysql_host,
        'prt': 3306,
        'dbn': 'dbnew'}
    # MySQL conection string.
connstr = 'mysql+pymysql://{usr}:{pwd}@{hst}:{prt}/{dbn}'
    # Create sqlalchemy engine for MySQL connection.
engine = create_engine(connstr.format(**creds))


# Assign spreadsheet filename to `file`
file = '/home/smv/sevsv.xlsx'
# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print('Получить из файла', file)
print('Вывести лист Excel', xl.sheet_names)  #печать названия страницы


# Load a sheet into a DataFrame by name: df
df = xl.parse('db_sv')


    # Write DataFrame to MySQL using the engine (connection) created above. (if_exists {'fail', 'replace', 'append')
df.to_sql(name='sevsv', con=engine, if_exists='replace', index=False)
engine.execute('ALTER TABLE sevsv MODIFY device varchar(15);')  #изменяет тип данных столбца device таблицы sevsv
engine.execute('ALTER TABLE sevsv ADD PRIMARY KEY (device);')  #устанавливает для столбца device первичный ключ

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  #вместо None можно указать число строк или столбцов
    print(df)

print('\nКоличесво строк и столбцов', df.shape, '\n')  #функция показывает количество строк и количество столбцов в таблице
print('....................\nОбщая сводка о таблице\n')
print(df.info())  #получаем общую сводку о таблице, в т.ч. какие столбцы, их названия,
                   # тип данных в столбцах, количество не пустых элементов


