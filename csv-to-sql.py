import pandas as pd
from sqlalchemy import create_engine
import csv

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

    # Read addresses from mCSV file.
text = list(csv.reader(open('/home/smv/sevsv.csv'), skipinitialspace=True))
for idx, row in enumerate(text):
    text[idx] = [i.strip().replace(',', '') for i in row]

    # Store data into a DataFrame.
df = pd.DataFrame(data=text, columns=['device', 'svid', 'mac_sv', 'appid', 'cabinet', 'level_kV', 'bay', 'winding',
                                      'module'])
df = df.drop(index=[0])  #удалить первую строку


    # Write DataFrame to MySQL using the engine (connection) created above. (if_exists {'fail', 'replace', 'append')
df.to_sql(name='sevsv', con=engine, if_exists='replace', index=False)
engine.execute('ALTER TABLE sevsv MODIFY device varchar(15);')  #изменяет тип данных столбца device таблицы sevsv
engine.execute('ALTER TABLE sevsv ADD PRIMARY KEY (device);')  #устанавливает для столбца device первичный ключ

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  #вместо None можно указать число строк или столбцов
    print(df)
