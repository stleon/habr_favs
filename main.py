import csv

from wordcloud import WordCloud

with open('favs/tags.csv', 'r') as f:
    # WordCloud does not support generate from seq
    # TODO generate_from_frequencies
    text = ', '.join(row[0] for row in csv.reader(f))

    print(text)

    wordcloud = WordCloud(
        width=2880,
        height=1800,
        scale=1,
        font_path='/Library/Fonts/Verdana.ttf',
        max_words=10000).generate(text)
    wordcloud.to_file('test.png')
