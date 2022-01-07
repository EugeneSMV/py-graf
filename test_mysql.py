
import pymysql

con = pymysql.connect(host='localhost', user='smvigeugene',
                      password='23A<aL7LqlzV:>', database='dbnew')  # связь с базой данных dbnew
dev = "PAS003"
# current version MySQL
with con:
    cur = con.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()
    print("Database version: {}".format(version[0]))

  # Метод fetchAll() позволяет извлечь все строки результата запроса,
    print("Table severovo:")
    cur.execute("SELECT * FROM severovo")
    rows = cur.fetchall()
    for row in rows:
        print("{0} {1} {2} {3} {4}".format(row[0], row[1], row[2], row[3], row[4]))

  # вывести названия столбцов с информацией из таблицы базы данных.
    print("Table severovo:")
    cur.execute("SELECT * FROM severovo")
    rows = cur.fetchall()
    desc = cur.description
    print("{0:>3} {1:>8} {2:>14} {3:>10} {4:>8}".format(desc[0][0], desc[1][0], desc[2][0], desc[3][0], desc[4][0]))
    for row in rows:
        print("{0} {1} {2} {3} {4}".format(row[0], row[1], row[2], row[3], row[4]))


  # получить строку с определенным значением  device

    print("Параметры для device =", dev)
    cur.execute("SELECT * FROM severovo WHERE device=%s", dev)

    device, svid, mac_sv, appid, csbinet = cur.fetchone()
    print(device, svid, mac_sv, appid, csbinet)





