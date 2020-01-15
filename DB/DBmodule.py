import pandas as pd
import csv

df_movies = pd.read_csv('movies.csv', usecols=['movieId', 'title', 'genres'],
                        dtype={'movieId': 'int32', 'title': 'str', 'genres': 'str'})

df_ratings = pd.read_csv('ratings.csv', usecols=['userId', 'movieId', 'rating'],
                         dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})

df_tags = pd.read_csv('../ml-latest/tags.csv', usecols=['userId', 'movieId', 'tag'],
                      dtype={'userId': 'int32', 'movieId': 'int32', 'tag': 'str'})

Inner_Join = pd.merge(df_movies, df_tags, how='inner', on=['movieId', 'movieId'])

with open('movies_with_tags.csv', "wt", newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    last_id = -1
    illegal_words = ["movies", "not", "r", "does", "in", "this", "é˜®ä¸€é¸£", "tã©a", "movie", "movies.", "movie."]
    last_title = ''
    tags = []
    tagline = ''
    first = 0
    for index, row in Inner_Join.iterrows():
        # print(row['movieId'], row['title'], row['tag'], row['genres'])
        if first == 0:
            last_id = row['movieId']
            last_title = row['title']
            tags = row['genres'].split('|')
            for cursor, value in enumerate(tags):
                tags[cursor] = value.lower()
            first = 1
            for i in str(row['tag']).split():
                if str(i).lower() not in tags:
                    if str(i).lower() not in illegal_words:
                        tags.append(str(i).lower())
            continue

        if row['movieId'] == last_id:
            for i in str(row['tag']).split():
                if str(i).lower() not in tags:
                    if str(i).lower() not in illegal_words:
                        tags.append(str(i).lower())
        else:
            for i in tags:
                tagline += i + ' '
            writer.writerow([last_id, last_title, tagline])
            last_id = row['movieId']
            last_title = row['title']
            tags = []
            tags = row['genres'].split('|')
            for cursor, value in enumerate(tags):
                tags[cursor] = value.lower()
            for i in str(row['tag']).split():
                if str(i).lower() not in tags:
                    if str(i).lower() not in illegal_words:
                        tags.append(str(i).lower())
            tagline = ''
