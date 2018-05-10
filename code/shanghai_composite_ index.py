'''
采集上证指数
'''
import requests
import json
import pandas

re = requests.get(
    'http://q.stock.sohu.com/hisHq?code=zs_000001&start=20111113&end=20180320&stat=1'
    '&order=D&period=d&callback=historySearchHandler&rt=jsonp&r=0.8391495715053367'
    '&0.9677250558488026')
results = re.text.lstrip('historySearchHandler').lstrip('([')[:-3]  # rstrip失败
re_dict = json.loads(results)
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
    all_date.append(stock_data)

df = pandas.DataFrame(all_date)
df.to_excel('stock_date.xlsx')
