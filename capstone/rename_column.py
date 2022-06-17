#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

file = '/Users/gitak/Documents/capstone/교통/서울시 버스정류소 위치정보.csv'
df = pd.read_csv(file,encoding='cp949')

#df.rename(columns={"line":"호선","name":"역명","code":"지하철 코드","lat":"지하철 역 위치 경도","lng":"지하철 역 위치 위도"}, inplace = True)
df.rename(columns={"X좌표":"버스 위치 경도", "Y좌표":"버스 위치 위도"},inplace = True)
df.to_csv('/Users/gitak/Documents/capstone/교통/busStation.csv', encoding='cp949')

