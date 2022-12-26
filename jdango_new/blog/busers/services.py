import random
import string

import pandas as pd
from sqlalchemy import create_engine

from basic import lambdas


class UserService(object):
    def __init__(self):
        pass
    def df_to_sql(self):
        df = self.dataframe_create()
        engine = create_engine(
            "mysql+pymysql://root:root@localhost:3306/mydb",
            encoding='utf-8')
        df.to_sql(name='blog_busers',
                  if_exists='append',
                  con = engine,
                  index=False)

    def dataframe_create(self):


        password = 1

        data =[{'email':lambdas.lambda_string(3) + '@naver.com','nickname':lambdas.lambda_k(2),'password':str(password)}
               for i in range(100)]
        print(data)
        df = pd.DataFrame(data)
        print(df)
        return df

    def get_users(self):
        pass

if __name__ == '__main__':
    s =UserService()
    s.df_to_sql() # 만듬 이미 돌리지마
