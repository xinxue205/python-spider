# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:35:27 2019

@author: Administrator
"""

import tushare as ts
ts.set_token('6a6b8bf5108aa2cc83d3ba23005fdb06323f208383992dd5e77a3d76')
#df = ts.get_stock_basics()
pro = ts.pro_api()

df = pro.fina_indicator(ts_code='600000.SH')
#另一种方式ts.get_stock_basics()
df.to_csv('c:/day/000875.csv')
#选择保存  df.to_csv('c:/day/000875.csv',columns=['open','high','low','close'])
