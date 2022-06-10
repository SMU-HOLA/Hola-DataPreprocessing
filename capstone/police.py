#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests 
import sys
import json
import datetime 


def json_request(url='', encoding='utf-8', success=None, error=lambda e: print('%s : %s' % (e, datetime.now()), file=sys.stderr)):
    headers = {'Authorization': 'KakaoAK {}'.format(APP_KEY)}
    resp = requests.get(url, headers=headers)
    # print('%s : success for request [%s]' % (datetime.now(), url))
    return resp.text


def reverse_geocode(longitude, latitude):
    # 파라미터 최적화하여 url 생성
    url = '%s?x=%s&y=%s' %(URL, longitude, latitude)
    # json request
    try:
          # print('try')
        json_req = json_request(url=url)
        json_data = json.loads(json_req)
        json_doc = json_data.get('documents')[0]
    except:
        json_doc='null'
    return json_doc

 
def get_gu_name(json_doc):
    
    if(json_doc == 'null'):
        return 'null'
        
    json_gu_name = json_doc.get('region_2depth_name')
    return json_gu_name # 전처리 함수에서 주소 리스트 받아서 데이터프레임에 추가


def get_dong_name(json_doc):  
   
    if(json_doc == 'null'):
        return 'null'
        
    json_dong_name = json_doc.get('region_3depth_name')
    return json_dong_name # 전처리 함수에서 주소 리스트 받아서 데이터프레임에 추가



# In[3]:


#카카오 API 사용
APP_KEY = 'c113241066618b00d323967d63f5df37' 
URL = 'https://dapi.kakao.com/v2/local/geo/coord2regioncode.json'

file = '/Users/gitak/Documents/capstone/복지/seoul_police_pos.csv'


df = pd.read_csv(file,usecols=['경찰서','구분','주소','경찰서 위도','경찰서 경도'], encoding='cp949') 

print("전처리 시작")

for i in range(len(df)):
    x_crd = float(df.loc[i, ['경찰서 위도']])
    y_crd = float(df.loc[i, ['경찰서 경도']])
    
    json_doc = reverse_geocode(x_crd,y_crd)
    
    if(get_gu_name(json_doc) == "null" or get_dong_name(json_doc) == "null"):
        continue
    
    gu_name = get_gu_name(json_doc)
    dong_name = get_dong_name(json_doc)
    
    #print(gu_name,dong_name)
    df.loc[i, ['지역구']] = gu_name
    df.loc[i, ['행정동']] = dong_name
    
    # 새로운 칼럼인 카테고리에 교통 추가 
    df.loc[i,['카테고리']] = '복지'

    if(i % 100 == 0):
        print(str(i)+'번째 전처리완료')
        
df.to_csv("/Users/gitak/Documents/capstone/복지/police.csv",encoding='cp949')

