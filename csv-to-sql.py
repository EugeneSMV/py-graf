import pymysql
import pandas as pd
from pymysql.connections import Connection
from sqlalchemy import create_engine
import csv




# Set database credentials.
creds = {'usr': 'smvigeugene',
        'pwd': '23A<aL7LqlzV:>',
        'hst': 'localhost',
        'prt': 3306,
        'dbn': 'dbnew'}
    # MySQL conection string.
connstr = 'mysql+pymysql://{usr}:{pwd}@{hst}:{prt}/{dbn}'
    # Create sqlalchemy engine for MySQL connection.
engine = create_engine(connstr.format(**creds))

    # Read addresses from mCSV file.
text = list(csv.reader(open('/home/smv/severovo_sv.csv'), skipinitialspace=True))
for idx, row in enumerate(text):
    text[idx] = [i.strip().replace(',', '') for i in row]

    # Store data into a DataFrame.
df = pd.DataFrame(data=text, columns=['device', 'svid', 'mac_sv', 'appid', 'cabinet', 'level_kV', 'bay', 'winding',
                                      'module', 'mac_hardware', 'number_hardware', 'tape_hardware'])
df = df.drop(index=[0])  #удалить первую строку


    # Write DataFrame to MySQL using the engine (connection) created above. (if_exists {'fail', 'replace', 'append')
df.to_sql(name='sevsv', con=engine, if_exists='replace', index=False)
engine.execute('ALTER TABLE sevsv MODIFY device varchar(15);')  #изменяет тип данных столбца device таблицы sevsv
engine.execute('ALTER TABLE sevsv ADD PRIMARY KEY (device);')  #устанавливает для столбца device первичный ключ

print(df)