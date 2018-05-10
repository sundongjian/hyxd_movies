'''
采集华谊兄弟电影名单
'''
import requests
import pandas

from bs4 import BeautifulSoup


def get_response(url):
    re = requests.get(url)
    re.encoding = 'utf-8'
    return re


def parse_resposne(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    dates = soup.select('dd ')
    content = []
    for date in dates:
        time = date.select('i')[0].text
        names = date.select('div a[target="_blank"]')
        for name in names:
            result = dict(name.attrs).get('title', '')
            if result != '':
                content.append({'name': result, 'date': time})
    return content


def main():
    # urls = ['http://movie.mtime.com/company/11131/productioncompanies.html',
    #         'http://movie.mtime.com/company/11131/productioncompanies-2.html',
    #         'http://movie.mtime.com/company/11131/productioncompanies-3.html',
    #         'http://movie.mtime.com/company/11131/productioncompanies-4.html',
    #         'http://movie.mtime.com/company/11131/productioncompanies-5.html']

    urls = ['http://movie.mtime.com/company/11131/distributors.html',
            'http://movie.mtime.com/company/11131/distributors-2.html',
            'http://movie.mtime.com/company/11131/distributors-3.html', ]
    contents = []
    for url in urls:
        response = get_response(url)
        content = parse_resposne(response)
        contents.extend(content)
    df = pandas.DataFrame(contents)
    df.to_excel('hyfx.xlsx')
    # df.to_excel('hyzz.xlsx')


if __name__ == '__main__':
    main()
