## From news API


import requests


def getnewsfromsource(source):
    url = 'http://newsapi.org/v2/top-headlines?sources='+source+'Your API Key'
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    l = response['articles']
    sources = []
    desc =[]
    news =[]
    img =[]
    for i in range(len(l)):
        f = l[i]
        sources.append(f['source'])
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    print(news)
    print(desc)

def get_top_headlines():
    url = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=Your API Key'
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    l = response['articles']

    flag = 0;
    desc =[]
    news =[]
    img =[]
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        flag += 1
        if(flag==3):
            break

    print(news)
    print(desc)


if __name__ == "__main__":
    get_top_headlines()
