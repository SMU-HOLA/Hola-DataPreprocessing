#!/usr/bin/env python
# coding: utf-8

# In[20]:


import json
import requests
import pandas as pd
APP_KEY = 'c113241066618b00d323967d63f5df37' 

def addr_to_lat_lon(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query={address}'.format(address=addr)
    headers = {"Authorization": "KakaoAK " + APP_KEY}
    result = json.loads(str(requests.get(url, headers=headers).text))
    
    # result['documents'][0]['address']가 인덱스 범위를 벗어나는 경우 예외처리
    try:
        match_first = result['documents'][0]['address']
    except:
        return float(0), float(0)
    
    return float(match_first['x']), float(match_first['y'])


# In[23]:


file = '/Users/gitak/Documents/capstone/복지/seoul_police.csv'


df = pd.read_csv(file,usecols=['경찰서','관서명','구분','주소'], encoding='cp949') 


for i in range(len(df)):
    lat, lon = addr_to_lat_lon(df.loc[i,"주소"])
    
    df.loc[i,'경찰서 위도'] = lat
    df.loc[i,'경찰서 경도'] = lon

    
print('Success')    
df.to_csv('/Users/gitak/Documents/capstone/복지/seoul_police_pos.csv', encoding = 'cp949')
    

