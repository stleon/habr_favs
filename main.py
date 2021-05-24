import csv
from collections import defaultdict

from wordcloud import WordCloud

tags = defaultdict(int)

with open('tags.csv', 'r') as f:
    for row in csv.reader(f):
        tag = ''.join(row).lower()
        tags[tag] += 1


wordcloud = WordCloud(
    width=4096,
    height=3072,
    scale=1,
    font_path='/Library/Fonts/Verdana.ttf',
    max_words=len(tags.keys()))\
    .generate_from_frequencies(tags)

wordcloud.to_file('test.png')
