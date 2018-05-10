'''
采集华谊兄弟市场详情
'''
import json
import pandas
import requests


re = requests.get('http://q.stock.sohu.com/hisHq?code=cn_300027&start=20111113&'
                  'end=20180320&stat=1&order=D&period=d&callback=historySearchHand'
                  'ler&rt=jsonp&r=0.8391495715053367&0.9677250558488026')
results = re.text.lstrip('historySearchHandler').lstrip('([')[:-3]  # rstrip失败
re_dict = json.loads(results)
print(re_dict)
data = re_dict["hq"]
all_date = []
for element in data:
    stock_data = {}
    stock_data['date'] = element[0].replace('-', '')
    stock_data['open'] = element[1]
    stock_data['close'] = element[2]
    stock_data['price_change'] = element[3]
    stock_data['p_change'] = element[4]
    stock_data['low'] = element[5]
    stock_data['high'] = element[6]
    stock_data['volume'] = element[7]
    stock_data['turn-volume'] = element[8]
    print(stock_data)
    all_date.append(stock_data)

df = pandas.DataFrame(all_date)
df.to_excel('hyxd300027.xlsx')
