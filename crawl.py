import json
import pandas as pd
import requests
r = requests.get('https://www.dcard.tw/service/api/v2/forums')
json_obj = r.json()
df = pd.DataFrame(json_obj)
#印出資料前三行，確認資料載入如同預期
df.tail(3)
# 列出所有columns
df.columns
# 依序且篩選出「name，isSchool，description，subscriptionCount，createdAt」欄位，並且將欄位命名成中文。
# 用兩層中括號篩選
df1 = df[['name', 'alias', 'isSchool', 'description', 'subscriptionCount', 'createdAt', 'updatedAt']]

# 可以用.columns選取欄位並重新命名
df1.columns = ['看板名稱', '看板別名', '學校', '描述', '訂閱人數', '建立時間', '更新時間']
df1.head(3)
#最新有更動的看板前三名
df2 = df1.sort_values('更新時間', ascending = False)
df2.head(3)
# 最多訂閱人數前三名
df3 = df1.sort_values('訂閱人數', ascending = False)
df3.head(3)
# 只挑出是學校的看板，並且對訂閱人數做排序
mask1 = df1['學校'] == True
df4 = df1[mask1].sort_values('訂閱人數', ascending = False)
df4.head()
import io
import json
import requests
import logging
import random
import time
import datetime
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm

%matplotlib inline
class Dcard:

    API_ROOT = 'https://www.dcard.tw/service/api/v2'
    FORUMS = 'forums'
    POSTS = 'posts'
    
    def get(self, url, verbose=False, **kwargs):
        response = requests.get(url, **kwargs)
        if verbose:
            logging.info(response.url)
        return response.json()

    def filter_general(self, forums):
        for forum in forums:
            if not forum['isSchool']:
                yield forum

    #@staticmethod
    def get_forums(self, **kwargs):
        url = '{api_root}/{api_forums}'.format(api_root=Dcard.API_ROOT, api_forums=Dcard.FORUMS)
        forums = get(url)
        if kwargs.get('no_school'):
            return [forum for forum in filter_general(forums)]
        return forums

    #@staticmethod
    def get_post_metas(self, forum, params):
        url = '{api_root}/{api_forums}/{forum}/{api_posts}'.format(
            api_root=Dcard.API_ROOT,
            api_forums=Dcard.FORUMS,
            api_posts=Dcard.POSTS,
            forum=forum
        )
        #print(url)
        article_metas = self.get(url, params=params)
        return article_metas

    #@staticmethod
    def get_post_ids(self, forum, pages=3):
        ''' 
            為了一次取的更多頁的文章 (可以把一次 request 取得 30 筆，視作取得一頁)
            使用此 method 將 `get_post_metas` 做包裝，提供一次抓取多頁文章資訊，
            且通常是為了之後用途而抓取 {文章編號}。
        '''
        params = {'popular': 'false'}
        ids = []
        post_list = []
        for _ in range(pages):
            metas = self.get_post_metas(forum, params)
            ids += [e['id'] for e in metas]
            params['before'] = ids[-1]
            #time.sleep(round(random.uniform(2,3), 2))
        return ids

    #@staticmethod
    def get_post_content(self, post_meta):
        post_url = '{api_root}/{api_posts}/{post_id}'.format(
            api_root=Dcard.API_ROOT,
            api_posts=Dcard.POSTS,
            post_id=post_meta
        )
        links_url = '{post_url}/links'.format(post_url=post_url)
        comments_url = '{post_url}/comments'.format(post_url=post_url)
        params = {}
        content = self.get(post_url)
        links = self.get(links_url)
        comments = []
        while True:
            _comments = self.get(comments_url, params=params, verbose=True)
            if len(_comments) == 0:
                break
            comments += _comments
            params['after'] = comments[-1]['floor']
            #time.sleep(round(random.uniform(2,3), 2))
        return {
            'content': content,
            'links': links,
            'comments': comments
        }
board = 'korea_star'
pageNum = 14

dcardObj = Dcard()
post_id_list = dcardObj.get_post_ids(board, pageNum)
post_list = []
for post_id in tqdm(post_id_list):
    result = dcardObj.get_post_content(post_id)
    post_dict = {}
    post_dict = result['content']
    post_dict['links'] = result['links']
    post_dict['postUrl'] = 'https://www.dcard.tw/f/{}/p/{}'.format(result["content"]["forumAlias"], result["content"]["id"])
    post_dict['comments'] = result['comments']
    post_list.append(post_dict)
    #time.sleep(round(random.uniform(2,3), 2))
df = pd.DataFrame(post_list)
if 'excerpt' in df.columns:
    del df['excerpt']
df.sample()
# 資料回傳的欄位名稱
df.columns
## 處理時間欄位 createdAt，並且轉換為 +8 台灣時區，並以空字串代替 nan 的值
df["createdAt"] = df["createdAt"].apply(lambda x:str(x).split('.')[0])
df["time"] = df["createdAt"].apply(lambda x: datetime.datetime.strptime(str(x),"%Y-%m-%dT%H:%M:%S")+datetime.timedelta(hours=+8))
df.fillna('', inplace=True)
df["year"] = df["time"].apply(lambda x: x.year)
df["month"] = df["time"].apply(lambda x: x.month)
df["day"] = df["time"].apply(lambda x: x.day)
df["hour"] = df["time"].apply(lambda x: x.hour)
df["minute"] = df["time"].apply(lambda x: x.minute)
df["second"] = df["time"].apply(lambda x: x.second)
df["weekday"] = df["time"].apply(lambda x: x.isoweekday())
df.sample()