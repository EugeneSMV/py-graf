import xlwings as xw  #может обрабатывать «проект Excel», содержащий несколько документов
import pandas as pd

wb=xw.Book('/home/smv/severovo_sv.xlsx')
data_excel = wb.sheets['db_sv']
data_pd = data_excel.range('A1:D7').options(pd.DataFrame, header = 1, index = False).value
print (data_pd)
