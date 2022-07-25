from bs4 import BeautifulSoup
import urllib.request

counter_pages = 0
results = []
while True:
    # counter_pages += 1
    try:
        if counter_pages == 1:
            myURL = f'https://gidonline.io/genre/boevik/'
        else:
            myURL = f'https://gidonline.io/genre/boevik/page/{counter_pages}/'
        # https://gidonline.io/genre/boevik/page/2/
        req = urllib.request.urlopen(myURL)
        html_doc = req.read()
    except urllib.error.HTTPError:
        print(f'No more pages. Last page is: {counter_pages}')
        break

    soup = BeautifulSoup(html_doc, 'html.parser')

    films = soup.find_all('a', class_='mainlink')
    ratings = soup.find_all('div', class_='f-rate')
    links = soup.find('div', id='posts').find_all('a')


    for i in range(len(films)):
        results.append({'title': films[i].find('span').string,
                        'rating_film': ratings[i].img.get('alt'),
                        'year': films[i].find('div', class_="mqn").string,
                        'link': links[i].get("href"),
                        })
        # results.append({'link': films[i].a.get('href').string, })
    # <a class="mainlink" href="https://gidonline.io/film/tron-nasledie/"><img src="/img/8d6760408_200x300.jpg" alt=""><span>Трон: Наследие</span><div class="f-rate"><img src="https://gidonline.io/wp-content/plugins/wp-postratings/images/stars_crystal/rating_on.png" alt="2,213 votes, average: 9.00 out of 10" class="post-ratings-image"><img src="https://gidonline.io/wp-content/plugins/wp-postratings/images/stars_crystal/rating_on.png" alt="2,213 votes, average: 9.00 out of 10" class="post-ratings-image"><img src="https://gidonline.io/wp-content/plugins/wp-postratings/images/stars_crystal/rating_on.png" alt="2,213 votes, average: 9.00 out of 10" class="post-ratings-image"><img src="https://gidonline.io/wp-content/plugins/wp-postratings/images/stars_crystal/rating_on.png" alt="2,213 votes, average: 9.00 out of 10" class="post-ratings-image"><img src="https://gidonline.io/wp-content/plugins/wp-postratings/images/stars_crystal/rating_on.png" alt="2,213 votes, average: 9.00 out of 10" class="post-ratings-image"><img src="https://gidonline.io/wp-content/plugins/wp-postratings/images/stars_crystal/rating_on.png" alt="2,213 votes, average: 9.00 out of 10" class="post-ratings-image"><img src="https://gidonline.io/wp-content/plugins/wp-postratings/images/stars_crystal/rating_on.png" alt="2,213 votes, average: 9.00 out of 10" class="post-ratings-image"><img src="https://gidonline.io/wp-content/plugins/wp-postratings/images/stars_crystal/rating_on.png" alt="2,213 votes, average: 9.00 out of 10" class="post-ratings-image"><img src="https://gidonline.io/wp-content/plugins/wp-postratings/images/stars_crystal/rating_on.png" alt="2,213 votes, average: 9.00 out of 10" class="post-ratings-image"><img src="https://gidonline.io/wp-content/plugins/wp-postratings/images/stars_crystal/rating_off.png" alt="2,213 votes, average: 9.00 out of 10" class="post-ratings-image"></div><div class="mqn">2010</div></a>
    print(results)
    # print(myURL)
    break

film = 1

print(results)
with open('newfile.txt', 'w', encoding='utf-8') as file:
    for result in results:
        file.write(f"Фильм №:{film} \n\n Название: {result['title']} \n Рейтинг: {result['rating_film']} \n Год: {result['year']} \n Ссылка: {result['link']} \n ***********\n")
        film +=1

#
# {result["rating_film"]}
#
# {result["year"]}
