import random
import string

import pandas as pd
from sqlalchemy import create_engine

class UserService(object):
    def __init__(self):
        pass
    def df_to_sql(self):
        df = self.frame_create()
        engine = create_engine(
            "mysql+pymysql://root:root@localhost:3306/mydb",
            encoding='utf-8')
        df.to_sql(name='blog_busers',
                  if_exists='append',
                  con = engine,
                  index=False)

    def Dataframe_create(self):
        n = 5
        email = ''
        golbang = '@google.com'
        password = 1
        nickname = 'NICK'
        data = []
        #email_list = list()
        a = 1
        for i in range(100):
            for i in range(n):
                email +=str(random.choice(string.ascii_letters))
            email += golbang
            # DF 만들때 [[],[],[]] 2차원 리스트 가능 / dic도 가능
            data.append({'num':a,'email':email,'nickname':nickname,'password':password})
            email = ''
            a =a+1
        df = pd.DataFrame(data)
        print(df)

        #중복체크
        #df2 = pd.DataFrame([[1],[2],[1]] ,columns=['email'])
        #print(df2)

        return data
    def get_users(self):
        pass

if __name__ == '__main__':
    s =UserService()
    s.Dataframe_create() # 만듬 이미 돌리지마
