import pandas as pd
import csv

s = pd.read_csv('/home/smv/sevsv.csv')
print(s)
print(s['device'])
print(s.shape)
print(s.columns)