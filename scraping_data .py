# -*- coding: utf-8 -*-
"""Scraping_Data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s7rGPrfht1f4j4Q6wE2cCwUTIaKWkIDX

**Instalation du snscrape par ce qu'il récupère des éléments tels que les utilisateurs, les profils d'utilisateurs, les hashtags...sans utiliser l'API de Twitter.**
"""

pip install -q snscrape

import os
import pandas as pd
from datetime import date
from google.colab import files

today = date.today()
end_date = today
print(end_date)

"""j'ai creer 2 variables search_term représente le filtrage de notre base et form_date represente par exemple l'apparesion de ce hashtag """

search_term= '#harassment'
from_date = '2018-01-01'

"""dans cette partie j'ai afficher le nombre de tweets avec ce hashtag (2018-2022)"""

os.system(f"snscrape --since {from_date} twitter-search '{search_term} until:{end_date}' > result-tweets.txt")
if os.stat("result-tweets.txt").st_size == 0:
  counter = 0
else:
  df = pd.read_csv('result-tweets.txt', names=['link'])
  counter = df.size

print('Number Of Tweets : '+ str(counter))

"""j'ai choisie d'afficheer uniquement 2500 tweets  """

max_results = 2500

"""par la suite j'ai affiche tous publication ou commentaire qui on #harassment"""

extracted_tweets = "snscrape --format '{content!r}'"+ f" --max-results {max_results} --since {from_date} twitter-search '{search_term} until:{end_date}' > extracted-tweets.txt"
os.system(extracted_tweets)
if os.stat("extracted-tweets.txt").st_size == 0:
  print('No Tweets found')
else:
  df = pd.read_csv('extracted-tweets.txt', names=['content'])
  for row in df['content'].iteritems():
    print(row)

"""Et je termine par sauveguarder mes données dans un fichier csv"""

df.to_csv('twitter_dataset.csv')

files.download('twitter_dataset.csv')