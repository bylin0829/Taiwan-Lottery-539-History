# -*- coding: UTF-8 -*-

from ntpath import join
import requests
from bs4 import BeautifulSoup
import pathlib

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

url_end = 153
url_tag = 'td'
url_class = 'auto-style5'
url_chapter = 'https://www.lotto-8.com/listlto539bbk.asp?indexpage='

for idx in range(url_end):
    url_goal = url_chapter + str(idx+1)
    response = requests.get(url_goal, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find_all(name=url_tag, class_=url_class)

    date = []
    number = []
    for i in result:
        if i.text.find('/') > -1 or i.text.find(',') > -1:
            data = i.text.replace(' ', '')
            if data.find('/') > -1:
                data = data[:4] + '/' + data[4:]
                date.append(data)
            else:
                data = data.replace(' ', '')
                number.append(data)

    if len(date) != len(number):
        raise ValueError()

    output_file = 'output.csv'
    folder = pathlib.Path(__file__).parent.resolve()
    file = join(folder, output_file)

    with open(file, 'a', encoding='UTF-8') as external_file:
        # print('Page {idx}'.format(idx=idx+1), file=external_file)
        for i in range(len(number)):
            add_text = 'date,{date},number,{number}'.format(
                date=date[i], number=number[i])
            print(add_text, file=external_file)
        external_file.close()
    print(idx)
