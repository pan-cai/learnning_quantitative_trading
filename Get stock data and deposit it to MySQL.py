# _*_ coding: utf-8 _*_

import tushare as ts #引入Tushare库

from sqlalchemy import create_engine

engine = create_engine('mysql://root:passwd@127.0.0.1/tushare?charset=utf8')

Stock = ["600372"]

st = ts.get_hist_data(Stock)

try:

    st.to_sql('Stock',engine,if_exists='append')

except Exception,e:

     print Exception,":",e

print "Stocks have saved to MySQL!"
