import tushare as ts
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://sdi:sdi@123@192.168.11.122:3306/sdi2?charset=utf8')
ts.set_token('6a6b8bf5108aa2cc83d3ba23005fdb06323f208383992dd5e77a3d76')
pro = ts.pro_api()
df2 = pro.daily(trade_date='20190812')
df2.to_sql('s_tomorrow',engine,if_exists='append')
#df2=pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
#df2.to_sql('s_basics',engine,if_exists='append')