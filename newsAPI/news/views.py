from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
  url = f'https://newsapi.org/v2/top-headlines?country=kr&apiKey=<API_KEY>'
  news_dummy = requests.get(url).json()
  articles = news_dummy['articles']

  articlesSorted = []
  for article in articles:
    articlesSorted.append({
      'source_name': article['source']['name'], 
      'author': article['author'], 
      'title': article['title'], 
      'url': article['url'], 
      'urlToImage': article['urlToImage']})

  return render(request, 'home.html', {'articlesSorted': articlesSorted})