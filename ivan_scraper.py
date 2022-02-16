import json
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from googlesearch import search

start_time = datetime.now()

BASE_URL = 'https://www.mangaworld.in/archive?page='

fileName = 'JsonFile.json'

archive_links = []
for cont in range(1, 11):
    link = f'{BASE_URL}{cont}'
    archive_links.append(link)


def get_manga(archive_link):
    archive_page_content = BeautifulSoup(requests.get(archive_link).content, 'html.parser')
    
    for archive_item in archive_page_content('div', class_='entry'):
        item_data = {}

        item_data['name'] = archive_item.find('a')['title']
        item_data['link'] = archive_item.find('a')['href']
        item_data['poster'] = archive_item.find('img')['src']
        
        item_data = get_more_info(item_data, item_data['link'])

        print(item_data['name'])

        animes_data.append(item_data)


def get_more_info(item_data, link):
    page_content = BeautifulSoup(requests.get(link).content, 'html.parser')
    
    principal_info = page_content.find('div', class_='meta-data')
    manga_part = page_content.find('div', class_='chapters-wrapper')
    
    info_archive = []
    for infos in principal_info('div', class_='col-12'):
        infos.span.decompose()
        info_archive.append(infos.text.strip())
        
    category_all = principal_info.find_all('a', class_='badge-primary')
    genres = [category.text for category in category_all]

    author = type = artist = status = year = 'Stranger'
    for link in principal_info.findAll('a'):
        if re.search('author', str(link)):
            author = link.text
        if re.search('type', str(link)):
            type = link.text
        if re.search('artist', str(link)):
            artist = link.text
        if re.search('status', str(link)):
            status = link.text
        if re.search('year', str(link)):
            year = link.text

    
    try:
        manga_list = []
        for manga in manga_part('div', class_='chapter'):
            manga_url = manga.find('a')['href']
            manga_list.append(manga_url)
    except:
        manga_list = 'No chapters found'
        pass

    trama = page_content.find('div', id='noidungm').text
    
    return{
        **item_data,
        'nome_alternativo': info_archive[0],
        'generi': genres,
        'autore': author,
        'artista': artist,
        'tipo': type,
        'stato': status,
        'anno_di_uscita': year,
        'trama': trama,
        'voto': get_score(item_data['name'], author),
        'chapter': manga_list,
    }


def get_score(title, author):
    results = search(f'{title} {author} myanimelist manga')
    soup = BeautifulSoup(requests.get(results[0]).content, 'html.parser')

    score = soup.find("div", class_='score-label')
    if score is None:
        score = "N/A"
    else:
        score = score.text

    return score


animes_data = []
for link in archive_links:
    print(f'___________________________________________😅😂❤️ Page: {archive_links.index(link)} / {len(archive_links)} ❤️😂😅___________________________________________')
    get_manga(link)


with open(fileName, 'w', encoding='utf-8') as f:
    json.dump(animes_data, f, ensure_ascii=False, indent=2)

end_time = datetime.now()
print(f'Duration: {end_time - start_time}')