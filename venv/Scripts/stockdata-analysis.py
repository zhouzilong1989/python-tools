#coding:utf-8
import tushare as ts
import matplotlib.pyplot as plt
import datetime
import pandas as pd

pd.set_option('display.width',None)
#df = ts.realtime_boxoffice()
df = ts.get_deposit_rate()
print(df)

#
# ticker = '600028'
# finance=ts.get_hist_data(ticker, '2018-09-01', '2018-10-30')
# print finance
# opens = [q for q in finance["open"]]
# print opens
# indexs = [q.encode('utf-8') for q in finance.index]
# print indexs
# dates = [datetime.datetime.strptime(q.encode('utf-8') ,"%Y-%m-%d") for q in finance.index]
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot_date(dates, opens, '-')
# #ax.plot_date(["2018-10-01", "2018-10-02", "2018-10-03", "2018-10-04", "2018-10-05"], [5,2,3,2,5], '-')
# fig.autofmt_xdate()
# plt.show()
#
