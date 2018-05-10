import requests
from bs4 import BeautifulSoup
import datetime
import pandas
import time


def creaturl(result):
    urllist = []
    for date in result:
        url = 'http://58921.com/boxoffice/wangpiao/' + date
        urllist.append(url)
    return urllist


def parse_url(url):
    date = url[-8:]
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    result = soup.select('tr')
    end_result = []
    for element in result:
        content = []
        result1 = element.select('td')[:2]
        result_dic = {}
        for re in result1:
            single = re.select('a')[0].text
            content.append(single)
        if content != []:
            result_dic['name'] = content[0]
            result_dic['box'] = content[1]
            result_dic['date'] = date
            end_result.append(result_dic)
    print('采集完成' + date)
    time.sleep(0.3)
    return end_result


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


def main():
    '''
    这里为了防止中途出错，统一300条文档一个文件，最后不足300的另外取
    :return:
    '''
    dates = datelist((2018, 3, 20), (2018, 4, 6))
    urllist = creaturl(dates)
    # for n in range(0,(len(dates)//300)):
    #     all_result=[]
    #     for url in urllist[300*n:300*(n+1)]:
    #         result=parse_url(url)
    #         all_result.extend(result)
    #     df=pandas.DataFrame(all_result)
    #     df.to_excel('movie'+str(n)+'.xlsx')
    #     print('采集完成'+str(n+1)+'*300')
    #     time.sleep(2)

    all_result = []
    for url in urllist:
        result = parse_url(url)
        all_result.extend(result)
    df = pandas.DataFrame(all_result)
    df.to_excel('movie' + str(8) + '.xlsx')
    time.sleep(2)


if __name__ == "__main__":
    main()
