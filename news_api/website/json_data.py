import requests
import json
from .convert_language import translateText

API_KEY = "7134f2e62d7a49babd40b617d29783a2"  # News api key form newsapi.org


def fetchNewsData(json_data):
    """Fetching news in json format"""
    json_data_lst = []
    for i in range(10):
        lang_fr = translateText([json_data['articles'][i]['title'].split("-")[0], json_data['articles'][i]['description']])
        title_en = json_data['articles'][i]['title'].split("-")[0]  # Using split function to avoid channel name
        desc_en = json_data['articles'][i]['description']
        title_fr = lang_fr[0].text
        desc_fr = lang_fr[1].text
        timestamp = json_data['articles'][i]['publishedAt']
        image_url = json_data['articles'][i]['urlToImage']

        # adding title, description, image_url, timestamp to data
        json_data_lst.append({"title_en": title_en, "desc_en": desc_en, "title_fr": title_fr, "desc_fr": desc_fr, "timestamp": timestamp, "image_url": image_url})
    return json_data_lst

def getData():
    url = 'https://newsapi.org/v2/top-headlines'
    data = {
        'apiKey': API_KEY,
        'category': "business",
        'language': "en",
        'country': "in"
    }

    json_res = json.loads(requests.get(url, data).text)
    return fetchNewsData(json_res)
