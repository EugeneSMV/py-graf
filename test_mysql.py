
import pymysql


with open('/home/smv/enter/mysql_user.txt', 'r', encoding='utf-8-sig') as fp:  #читать имя из файла
    mysql_usr = fp.read().rstrip()
with open('/home/smv/enter/mysql_password.txt', 'r', encoding='utf-8-sig') as fp:  #читать пароль из файла
    mysql_pass = fp.read().rstrip()
with open('/home/smv/enter/mysql_host.txt', 'r', encoding='utf-8-sig') as fp:  #читать хост из файла
    mysql_host = fp.read().rstrip()


con = pymysql.connect(host=mysql_host, user=mysql_usr,
                      password=mysql_pass, database='dbnew')  # связь с базой данных dbnew
dev = "PAS003"
# current version MySQL
with con:
    cur = con.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()
    print("Database version: {}".format(version[0]))

  # Метод fetchAll() позволяет извлечь все строки результата запроса,
    print("Table sevsv:")
    cur.execute("SELECT * FROM sevsv")
    rows = cur.fetchall()
    for row in rows:
        print("{0} {1} {2} {3} {4}".format(row[0], row[1], row[2], row[3], row[4]))



  # получить строку с определенным значением  device

    print("Параметры для device =", dev)
    cur.execute("SELECT * FROM severovo WHERE device=%s", dev)

    device, svid, mac_sv, appid, cabinet = cur.fetchone()
    print(device, svid, mac_sv, appid, cabinet)





