import pandas
import numpy


def get_all_movies():
    datas = pandas.read_excel('cleandata_unit.xlsx').to_dict('records')
    movies = pandas.read_excel('all_movie_box.xlsx').to_dict('records')

    all_movies = []
    for movie in datas:  # update失败不知为何
        if movie['name'] not in all_movies:
            all_movies.append(movie['name'])
            print(movie['name'])
    df = pandas.DataFrame(all_movies)
    df.to_excel('all_movie_list.xlsx')
    print('读写完成')


def parse_movies():
    movies = pandas.read_excel(r'../data/all_movie_list.xlsx')
    datas = pandas.read_excel(r'../data/cleandata_unit1.xlsx')
    for movie in movies.values[:1]:
        movie = movie[0]
        element = datas[datas['name'].isin([movie])]
        dates = sorted(element.date.values, reverse=True)  # sort()失败，sorted（）成功
        for n in range(0, len(dates) + 1):
            if n < len(datas):
                today_day = element[datas['date'].isin([dates[n]])].box.values
                yestoday_day = element[datas['date'].isin([dates[n + 1]])].box.values
                print(today_day, yestoday_day)
                today_day_box = today_day[0] - yestoday_day[0]
            else:
                today_day_box = element[datas['date'].isin([dates[n]])].box.values
            print(today_day_box)


def parse_sum():
    df = pandas.read_excel(r'../data/cleandata_unit1.xlsx')
    df = df.groupby(by=['date'])['box'].sum()
    df = df.to_frame()
    df['date'] = df.index
    df = df.reset_index(drop=True)
    df.to_excel('../data/sum_box.xlsx')
    print('读写完成')


def parse_comsum():
    data = pandas.read_excel(r'../data/sum_box.xlsx')
    df = data['box'].cumsum()

    df = df.to_frame()
    df['date'] = data['date']
    df.to_excel('../data/cumsum_box2.xlsx')
    print('读写完成')


def growth():  # growth=1000*(ny-t)/(t*(nd-td))不科学
    data = pandas.read_excel(r'../data/cumsum_box2.xlsx')
    df = data.to_dict('records')
    n = len(df)
    all_growth = []
    for i in range(0, n - 1):
        nd = df[i + 1]['date']
        td = df[i]['date']
        ny = int(df[i + 1]['box'])
        t = int(df[i]['box'])
        growth = 1000 * (ny - t) / (t * (nd - td))
        all_growth.append({'growth': growth, 'date': td})
    df = pandas.DataFrame(all_growth)
    df.to_excel('growth2.xlsx')
    print('读写完成')


def growth2():
    data = pandas.read_excel(r'../data/cumsum_box2.xlsx')
    df = data.to_dict('records')
    n = len(df)
    all_growth = []
    for i in range(0, n):
        if i == 0:
            g_d = {'growth': 0, 'date': df[i]['date']}
        if i == 1:
            yd = df[i - 1]['date']
            td = df[i]['date']
            n = int(df[i - 1]['box'])
            t = int(df[i]['box'])
            growth = (t - n) / (t * (td - yd))
            g_d = {'growth': growth, 'date': td}
        else:
            yd = df[i - 1]['date']
            td = df[i]['date']
            q = int(df[i - 2]['box'])
            n = int(df[i - 1]['box'])
            t = int(df[i]['box'])
            growth = (t - n) / ((n - q) * (td - yd))
            g_d = {'growth': growth, 'date': td}
        print(g_d)
        all_growth.append(g_d)
    df = pandas.DataFrame(all_growth)
    df.to_excel('../data/growth_divsion.xlsx')
    print('读写完成')


def add_labels():
    data = pandas.read_excel(r'../data/growth_divsion.xlsx')
    dates = data.date.values
    hy = pandas.read_excel(r'../data/hy3000027.xlsx')
    sum_data = []
    for date in dates:
        result = []
        result1 = []
        result2 = []
        result3 = []
        result4 = []
        result5 = []
        result6 = []
        result7 = []
        result8 = []

        for i in range(1, 25):

            element = hy[hy['date'].isin([date + i])].price_change.values
            element = element.tolist()  # 将array转化为list
            if len(element):  # 判断[]
                result.append(element[0])
        result1 = sum(result[:1])
        result2 = sum(result[:2])
        result3 = sum(result[:3])
        result4 = sum(result[:4])
        result5 = sum(result[:5])
        result6 = sum(result[:6])
        result7 = sum(result[:7])
        result8 = sum(result[:8])
        print(result8)
        sum_data.append(result8)

    dr = pandas.read_excel(r'../data/result7.xlsx')
    dr['result8'] = numpy.array(sum_data)
    dr.to_excel(r'../data/result8.xlsx')
    print('读写完成')
    df = pandas.read_excel(r'../data/result8.xlsx')
    print(df)


def standard_data():
    data = pandas.read_excel(r'../data/result8.xlsx')
    data['result1'] = int(data.result1.values * 100)
    data['result2'] = int(data.result2.values * 100)
    data['result3'] = int(data.result3.values * 100)
    data['result4'] = int(data.result4.values * 100)
    data['result5'] = int(data.result5.values * 100)
    data['result6'] = int(data.result6.values * 100)
    data['result7'] = int(data.result7.values * 100)
    data['result8'] = int(data.result8.values * 100)
    print(data)
    data.to_excel(r'../data/result9.xlsx')
