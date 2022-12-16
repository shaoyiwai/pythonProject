import os
import pandas as pd

file_path = r'C:\Users\qchd\Desktop\牛排'
lst = []
for file in os.listdir(r'C:\Users\qchd\Desktop\牛排'):
    if file.endswith(".xlsx"):
        file_name = os.path.join(file_path, file)
        df = pd.read_excel(file_name)
        # sheet_name="流量来源")
        df['账号名'] = file.split('.')[0]
        lst.append(df)
writer = pd.ExcelWriter(r'C:\Users\qchd\Desktop\直播分析汇总.xlsx')
pd.concat(lst).to_excel(writer, 'Sheet1', index=False)
writer.save()
