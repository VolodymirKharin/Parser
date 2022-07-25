from bs4 import BeautifulSoup
import urllib.request


class Parser:

    raw_html = ''
    html = ''
    results = []
    counter_pages = 180

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        while True:
            self.counter_pages += 1
            try:
                if self.counter_pages == 1:
                    myURL = f'{self.url}'
                else:
                    myURL = f'{self.url}page/{self.counter_pages}/'
                # https://gidonline.io/genre/boevik/page/2/
                req = urllib.request.urlopen(myURL)
                self.raw_html = req.read()
                print(f'Парсинг страницы:{myURL} с номером: {self.counter_pages}')
            except urllib.error.HTTPError:
                print(f'No more pages. Last page is: {self.counter_pages}')
                break
            self.get_soup()
            self.parsing()

    def get_soup(self):
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        films = self.html.find_all('a', class_='mainlink')
        ratings = self.html.find_all('div', class_='f-rate')
        links = self.html.find('div', id='posts').find_all('a')

        for i in range(len(films)):
            self.results.append({'title': films[i].find('span').string,
                            'rating_film': ratings[i].img.get('alt'),
                            'year': films[i].find('div', class_="mqn").string,
                            'link': links[i].get("href"),
                            })

    def save(self):
        with open(self.path, 'w', encoding='utf-8') as file:
            film = 0
            for result in self.results:
                file.write(f"Фильм №:{film} \n\n Название: {result['title']} \n Рейтинг: {result['rating_film']} \n Год: {result['year']} \n Ссылка: {result['link']} \n ***********\n")
                film += 1

    def run(self):
        self.get_html()
        self.save()

