#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

file = "/Users/gitak/Documents/capstone/복지/police.csv"
subway = pd.read_csv(file,usecols=['지역구','행정동'], encoding='cp949')
subway

#구별, 행정동 별 해당  count 집계후 csv
gr_by_gu = subway.groupby(by=['지역구'], as_index=False).count()
gr_by_gu.to_csv('/Users/gitak/Documents/capstone/복지/police_gu_agg.csv', encoding='cp949')
gr_by_dong = subway.groupby(by=['행정동'], as_index=False).count()
gr_by_dong.to_csv('/Users/gitak/Documents/capstone/복지/police_dong_agg.csv',encoding='cp949')

# gr_by_dong = subway.groupby(['행정동'])
# gu_subway.to_csv('/Users/gitak/Documents/capstone/교통/gu_aggregation.csv',encoding='CP949')

