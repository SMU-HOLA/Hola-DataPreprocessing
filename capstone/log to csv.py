#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd


#log파일 txt파일로 변환후 다시 csv파일로 변환
file = "/Users/gitak/Documents/capstone/교통/subway_new.txt"

df = pd.read_table(file, sep=',')
df.to_csv("/Users/gitak/Documents/capstone/교통/subway.csv", encoding='cp949')

