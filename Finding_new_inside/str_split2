import pandas as pd

df = pd.read_csv('data/museum_2.csv')

#지역번호라는 칼럼을 만들어, 운영기간 전화번호에서 지역번호만 가져온다.
number = df['운영기관전화번호'].str.split('-', n=1, expand = True)
df['지역번호'] = number[0]
df
