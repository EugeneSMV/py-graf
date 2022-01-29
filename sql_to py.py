import pandas as pd
from sqlalchemy import create_engine
import datetime


day_time = datetime.datetime.now()
print(day_time)

pd.options.display.width = 0  #pandas автоматически определяет размер окна терминала, без этого парамента
                               # последние столбцы столбцы переносились при печати

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