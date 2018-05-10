import pandas
import datetime


def datelist(start, end):
    start_date = datetime.date(*start)
    end_date = datetime.date(*end)

    result = []
    curr_date = start_date
    while curr_date != end_date:
        result.append("%04d%02d%02d" % (curr_date.year, curr_date.month, curr_date.day))
        curr_date += datetime.timedelta(1)
    result.append("%04d%02d%02d" % (curr_date.year, curr_date.month, curr_date.day))
    return result


movie_data = pandas.read_excel(r'../data/attendance.xlsx')
movie_data_date = pandas.read_excel(r'../data/attendance.xlsx').date.values
data_hy_date = pandas.read_excel(r'../data/hy3000027.xlsx').date.values  #
data_hy = pandas.read_excel(r'../data/hy3000027.xlsx')
sz_date = sorted(pandas.read_excel(r'../data/stock_date.xlsx').date.values.tolist())


# 挑出该交易日前一天的票房
def get_labels1(a_dates):
    all_data = []
    for i in range(2, len(data_hy_date) - 1):  # 这是个递减的日期
        date = data_hy_date[i]
        m = a_dates.index(date)  # 这是取票房的时间index
        n = sz_date.index(date)  # 这是大盘对应的时间index
        if data_hy_date[i - 1] == sz_date[n + 1] and data_hy_date[i + 1] == sz_date[n - 1]:  # 如果第二天没停牌
            spreads = data_hy[data_hy['date'].isin([data_hy_date[i - 1]])].open.tolist()[0] - \
                      data_hy[data_hy['date'].isin([date])].open.tolist()[0]  # 如果第二天没停牌
            gains = data_hy[data_hy['date'].isin([date])].open.tolist()[0] - \
                    data_hy[data_hy['date'].isin([data_hy_date[i + 1]])].close.tolist()[0]
            if a_dates[m - 1] in movie_data_date:
                element = movie_data[movie_data['date'].isin([a_dates[m - 1]])].to_dict('records')[0]  # 前一天的票房情况

                if spreads >= 0.3:
                    price_change = 1
                # elif 0 <= price_change < 0.2:
                #     price_change=1
                else:
                    price_change = 0

                if gains > 0:
                    gains = 1
                else:
                    gains = 0

                element['gains'] = gains
                element['result1'] = price_change
                element['attendance'] = float(str(element['attendance']).split('%')[0])
                print(element)
                all_data.append(element)
    df = pandas.DataFrame(all_data)
    df.to_excel('../hyxd3/hyxd_movie_3data1.xlsx')


# 两天
def get_labels2(a_dates):
    all_data = []
    for i in range(1, len(data_hy_date) - 1):  # 这是个递减的日期
        # for date in data_hy_date:#将华谊兄弟日期列表
        date = data_hy_date[i]
        m = a_dates.index(date)  #
        n = sz_date.index(date)  # 大盘
        try:
            if data_hy_date[i - 1] == sz_date[n + 1] and data_hy_date[i - 2] == sz_date[n + 2] and data_hy_date[
                        i + 1] == sz_date[n - 1]:  # 如果第二天没停牌
                gains = data_hy[data_hy['date'].isin([date])].open.tolist()[0] - \
                        data_hy[data_hy['date'].isin([data_hy_date[i + 1]])].close.tolist()[0]
                spreads1 = data_hy[data_hy['date'].isin([date])].open.tolist()[0]  # 今天
                spreads2 = data_hy[data_hy['date'].isin([data_hy_date[i - 2]])].open.tolist()[0]  # 后天开盘价
                price_change = spreads2 - spreads1  # 华谊兄弟价格变动只和
                if a_dates[m - 1] in movie_data_date:
                    element = movie_data[movie_data['date'].isin([a_dates[m - 1]])].to_dict('records')[0]  # 前一天的票房情况
                    if price_change >= 0.3:
                        price_change = 1
                    else:
                        price_change = 0
                    if gains > 0:
                        gains = 1
                    else:
                        gains = 0

                    element['gains'] = gains
                    element['result1'] = price_change
                    element['attendance'] = float(str(element['attendance']).split('%')[0])
                    print(element)
                    all_data.append(element)
        except:
            pass
    df = pandas.DataFrame(all_data)
    df.to_excel('../hyxd3/hyxd_movie_3data2.xlsx')


def get_labels3(a_dates):
    all_data = []
    for i in range(1, len(data_hy_date) - 1):  # 这是个递减的日期
        # for date in data_hy_date:#将华谊兄弟日期列表
        date = data_hy_date[i]
        m = a_dates.index(date)  #
        n = sz_date.index(date)  # 大盘
        try:
            if data_hy_date[i - 1] == sz_date[n + 1] and data_hy_date[i - 2] == sz_date[n + 2] and data_hy_date[
                        i - 3] == sz_date[n + 3] and data_hy_date[i + 1] == sz_date[n - 1]:  # 如果第二天没停牌
                gains = data_hy[data_hy['date'].isin([date])].open.tolist()[0] - \
                        data_hy[data_hy['date'].isin([data_hy_date[i + 1]])].close.tolist()[0]
                price_change1 = data_hy[data_hy['date'].isin([date])].open.tolist()[0]  # 今天
                price_change3 = data_hy[data_hy['date'].isin([data_hy_date[i - 3]])].open.tolist()[0]  # 大后天开盘易日
                price_change = price_change3 - price_change1  # 华谊兄弟价格变动只和
                if a_dates[m - 1] in movie_data_date:
                    element = movie_data[movie_data['date'].isin([a_dates[m - 1]])].to_dict('records')[0]  # 前一天的票房情况
                    if price_change >= 0.3:
                        price_change = 1
                    else:
                        price_change = 0

                    if gains > 0:
                        gains = 1
                    else:
                        gains = 0
                    element['gains'] = gains
                    element['result1'] = price_change
                    element['attendance'] = float(str(element['attendance']).split('%')[0])
                    print(element)
                    all_data.append(element)
        except:
            pass
    df = pandas.DataFrame(all_data)
    df.to_excel('../hyxd3/hyxd_movie_3data3.xlsx')


def get_labels4(a_dates):
    all_data = []
    for i in range(1, len(data_hy_date) - 1):  # 这是个递减的日期
        # for date in data_hy_date:#将华谊兄弟日期列表
        date = data_hy_date[i]
        m = a_dates.index(date)  #
        n = sz_date.index(date)  # 大盘
        try:
            if data_hy_date[i - 1] == sz_date[n + 1] and data_hy_date[i - 2] == sz_date[n + 2] \
                    and data_hy_date[i - 3] == sz_date[n + 3] and data_hy_date[i - 4] == sz_date[n + 4] and \
                            data_hy_date[i + 1] == sz_date[n - 1]:  # 如果第二天没停牌
                gains = data_hy[data_hy['date'].isin([date])].open.tolist()[0] - \
                        data_hy[data_hy['date'].isin([data_hy_date[i + 1]])].close.tolist()[0]
                price_change1 = data_hy[data_hy['date'].isin([date])].open.tolist()[0]  # 今天
                price_change4 = data_hy[data_hy['date'].isin([data_hy_date[i - 4]])].open.tolist()[0]
                price_change = price_change4 - price_change1  # 华谊兄弟价格变动只和
                if a_dates[m - 1] in movie_data_date:
                    element = movie_data[movie_data['date'].isin([a_dates[m - 1]])].to_dict('records')[0]  # 前一天的票房情况
                    if price_change >= 0.3:
                        price_change = 1
                    else:
                        price_change = 0
                    if gains > 0:
                        gains = 1
                    else:
                        gains = 0

                    element['gains'] = gains
                    element['result1'] = price_change
                    element['attendance'] = float(str(element['attendance']).split('%')[0])
                    print(element)
                    all_data.append(element)
        except:
            pass
    df = pandas.DataFrame(all_data)
    df.to_excel('../hyxd3/hyxd_movie_3data4.xlsx')


def get_labels5(a_dates):
    all_data = []
    for i in range(1, len(data_hy_date) - 1):  # 这是个递减的日期
        # for date in data_hy_date:#将华谊兄弟日期列表
        date = data_hy_date[i]
        m = a_dates.index(date)  #
        n = sz_date.index(date)  # 大盘

        try:
            if data_hy_date[i - 1] == sz_date[n + 1] and data_hy_date[i - 2] == sz_date[n + 2] \
                    and data_hy_date[i - 3] == sz_date[n + 3] \
                    and data_hy_date[i - 4] == sz_date[n + 4] \
                    and data_hy_date[i - 5] == sz_date[n + 5] and data_hy_date[i + 1] == sz_date[n - 1]:  # 如果第二天没停牌
                gains = data_hy[data_hy['date'].isin([date])].open.tolist()[0] - \
                        data_hy[data_hy['date'].isin([data_hy_date[i + 1]])].close.tolist()[0]
                price_change1 = data_hy[data_hy['date'].isin([date])].open.tolist()[0]  # 今天
                price_change5 = data_hy[data_hy['date'].isin([data_hy_date[i - 5]])].open.tolist()[0]
                price_change = price_change5 - price_change1  # 华谊兄弟价格变动只和
                if a_dates[m - 1] in movie_data_date:
                    element = movie_data[movie_data['date'].isin([a_dates[m - 1]])].to_dict('records')[0]  # 前一天的票房情况
                    if price_change >= 0.3:  # 0.2的数据是错的，但是不管了，反正用不着
                        price_change = 1
                    else:
                        price_change = 0
                    if gains > 0:
                        gains = 1
                    else:
                        gains = 0

                    element['gains'] = gains
                    element['result1'] = price_change
                    element['attendance'] = float(str(element['attendance']).split('%')[0])
                    print(element)
                    all_data.append(element)
        except:
            pass
    df = pandas.DataFrame(all_data)
    df.to_excel('../hyxd3/hyxd_movie_3data5.xlsx')


# 上次是手动加的，这次忘记加了
def standard_data():
    for i in range(1, 6):
        stardard_data = []
        data = pandas.read_excel(r'../hyxd3/hyxd_movie_3data' + str(i) + '.xlsx').to_dict('records')
        for element in data:
            if element['date'] < 20120000:
                element['lasty'] = 101.7
                stardard_data.append(element)
            elif 20120000 <= element['date'] < 20130000:
                element['lasty'] = 131.2
                stardard_data.append(element)
            elif 20130000 <= element['date'] < 20140000:
                element['lasty'] = 170.7
                stardard_data.append(element)
            elif 20140000 <= element['date'] < 20150000:
                element['lasty'] = 217.7
                stardard_data.append(element)
            elif 20150000 <= element['date'] < 20160000:
                element['lasty'] = 296.4
                stardard_data.append(element)
            elif 20160000 <= element['date'] < 20170000:
                element['lasty'] = 438.8
                stardard_data.append(element)
            elif 20170000 <= element['date'] < 20180000:
                element['lasty'] = 455.2
                stardard_data.append(element)
            elif 20180000 <= element['date'] < 20190000:
                element['lasty'] = 301
                stardard_data.append(element)
        df = pandas.DataFrame(stardard_data)
        df.to_excel('../hyxd3/hyxd_movie_3newdata' + str(i) + '.xlsx')
        print('读写完成')


dates = datelist((2011, 11, 12), (2018, 3, 20))
dates = [int(i) for i in dates]
get_labels1(dates)
get_labels2(dates)
get_labels3(dates)
get_labels4(dates)
get_labels5(dates)
standard_data()
