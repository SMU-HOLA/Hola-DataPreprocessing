#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

pol = pd.read_csv('/Users/gitak/Documents/capstone/복지/경찰청_경찰관서 위치, 주소 현황_20210924.csv', encoding='cp949')
not_seoul= pol[pol['지방청'] != '서울청'].index
seoul_police = pol.drop(not_seoul)

seoul_police.to_csv('/Users/gitak/Documents/capstone/복지/seoul_police.csv', encoding='cp949')

