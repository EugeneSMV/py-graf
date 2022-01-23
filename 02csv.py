import csv
import pymysql

mydb = pymysql.connect(host='localhost', user='smvigeugene',
                       password='23A<aL7LqlzV:>', database='dbnew')
print ("\nConnection to DataBase established..\n")




with open('/home/smv/dbsv.csv', newline='') as f:  #
    reader = csv.reader(f)
    for row in reader:
        print(row)
