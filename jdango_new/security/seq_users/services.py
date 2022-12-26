import random

import pandas as pd
from sqlalchemy import create_engine

from basic import lambdas


class SUserService(object):
    def __init__(self):
        pass
    def df_to_sql(self):
        df = self.dataframe_create()
        engine = create_engine(
            "mysql+pymysql://root:root@localhost:3306/mydb",
            encoding='utf-8')
        df.to_sql(name='seq_users',
                  if_exists='append',
                  con = engine,
                  index=False)

    def dataframe_create(self):
        '''
        susers_id = models.AutoField(primary_key=True)
        user_email = models.CharField(max_length=20)
        password = models.CharField(max_length=20)
        user_name = models.CharField(max_length=20)
        phone = models.CharField(max_length=20)
        birth = models.CharField(max_length=20)
        address = models.CharField(max_length=20)
        job = models.CharField(max_length=20)
        user_interests = models.CharField(max_length=20)
        token = models.CharField(max_length=20)
            '''



        data =[{'user_email':lambdas.lambda_string(3) + '@naver.com','password':'1',
                'user_name':lambdas.lambda_k(2), 'phone':lambdas.lambda_phone(4),'birth':lambdas.lambda_birth(1985, 2011),
                'address':  random.choice(lambdas.address_list),'job':random.choice(lambdas.job_list),
                'user_interests':random.choice(lambdas.interests_list),'token':'JWT fefege..'}
               for i in range(100)]

        print(data)
        df = pd.DataFrame(data)
        print(df)
        return df

    def get_users(self):
        pass

if __name__ == '__main__':
    s =SUserService()
    s.df_to_sql() # 만듬 이미 돌리지마
