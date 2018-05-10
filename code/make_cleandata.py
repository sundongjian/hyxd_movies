import pandas
import json

hyfx_movies = pandas.read_excel('../data/hyfx.xlsx')
hyzz_movies = pandas.read_excel('../data/hyzz.xlsx')

hyfx_name = list(hyfx_movies['name'])
hyzz_name = list(hyzz_movies['name'])


def clean_data():
    clean_data = []
    for i in range(0, 8):
        print('正在读取第', i)
        file = '../data/movie' + str(i) + ('.xlsx')
        movies = pandas.read_excel(file).to_dict('records')  # 转字典
        for movie in movies:  # update失败不知为何
            if movie['name'] in hyfx_name and movie['name'] in hyzz_name:
                movie['hyzz'] = 1
                movie['hyfx'] = 1
                clean_data.append(movie)
                # hyfx_name.remove(movie['name'])
                # hyzz_name.remove(movie['name'])
            elif movie['name'] in hyfx_name:
                movie['hyzz'] = 0
                movie['hyfx'] = 1
                clean_data.append(movie)
                # hyfx_name.remove(movie['name'])
            elif movie['name'] in hyzz_name:
                movie['hyzz'] = 1
                movie['hyfx'] = 0
                clean_data.append(movie)
                # hyzz_name.remove(movie['name'])
    # print(hyfx_name)
    # print(hyzz_name)
    df = pandas.DataFrame(clean_data)
    df.to_excel('../data/cleandata.xlsx')
    print('读写完成')


def parse_data():
    file = '../data/cleandata.xlsx'
    clean_data1 = []
    file = pandas.read_excel(file).to_dict('records')
    for i in file:
        m = i['box']
        if isinstance(m, str) and m.endswith('亿'):
            m = float(m[:-1]) * 10000
        if isinstance(m, str) and m.endswith('万'):
            m = float(m[:-1])
        else:
            m = float(m) * 0.0001
        m_new = {'box': m}
        i.update(m_new)
        clean_data1.append(i)

    df = pandas.DataFrame(clean_data1)
    df.to_excel('../data/cleandata_unit1.xlsx')


# clean_data()
parse_data()
