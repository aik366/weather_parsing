import requests
from bs4 import BeautifulSoup as BS


def main():
    url = 'https://rp5.ru/Погода_в_Краснодаре,_Краснодарский_край'
    class_ = 'ArchiveTemp'

    r = requests.get(url)
    html = BS(r.text, 'html.parser')
    t = html.find(class_=class_).find(class_='t_0').text
    find_text = html.find('div', {'id': "forecastShort-content"}).find(class_='t_0').get_text()

    print(find_text[:-3])


if __name__ == '__main__':
    main()
