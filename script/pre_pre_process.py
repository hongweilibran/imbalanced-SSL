import os
import numpy as np
import csv
import pandas as pd


data_path = '/media/bran/data/iclr_22_imbalance/skin_lesion/HAM10000_metadata.csv'
col_list = ["image_id", "dx"]
df = pd.read_csv(data_path, usecols=col_list)
# print(df["image_id"])
# print(df["dx"])

image_id = df["image_id"]
dx = df["dx"]




print(np.sum(dx == 'akiec'))
print(np.sum(dx == 'bcc'))
print(np.sum(dx == 'bkl'))
print(np.sum(dx == 'df'))
print(np.sum(dx == 'mel'))
print(np.sum(dx == 'nv'))
print(np.sum(dx == 'vasc'))


print(np.unique(dx))
print(np.shape(image_id))
print(np.shape(dx))









# types = ['bkl', 'df', 'mel', 'vasc', 'bcc', 'nv', ]
#
# rows = []
# with open(data_path, 'r') as file:
#     csvreader = csv.reader(file)
#     header = next(csvreader)
#     for row in csvreader:
#         rows.append(row)
# print(header)
# print(rows)
#








