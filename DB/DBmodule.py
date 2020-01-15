import pandas as pd
import csv

df_movies = pd.read_csv('movies.csv', usecols=['movieId', 'title', 'genres'],
                        dtype={'movieId': 'int32', 'title': 'str', 'genres': 'str'})

# df_ratings = pd.read_csv('ratings.csv', usecols=['userId', 'movieId', 'rating'],
#                          dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})

# df_tags = pd.read_csv('tags.csv', usecols=['userId', 'movieId', 'tag'],
#                       dtype={'userId': 'int32', 'movieId': 'int32', 'tag': 'str'})

df_genome_tags = pd.read_csv('genome-tags.csv', usecols=['tagId', 'tag'],
                             dtype={'tagId': 'int32', 'tag': 'str'})

df_genome_scores = pd.read_csv('genome-scores.csv', usecols=['movieId', 'tagId', 'relevance'],
                             dtype={'tagId': 'int32', 'movieId': 'int32', 'relevance': 'float32'})

# print(df_movies.loc[df_movies['title'] == 'Toy Story (1995)'])
# print(df_tags.loc[df_tags['movieId'] == '1'])
Inner_Join_tag_genomes = pd.merge(df_genome_tags, df_genome_scores, how='inner', on=['tagId', 'tagId'])
Inner_Join = pd.merge(Inner_Join_tag_genomes, df_movies, how='inner', on=['movieId', 'movieId'])
# print(Inner_Join.loc[Inner_Join['title'] == 'Toy Story (1995)'])
# Inner_Join = pd.merge(df_movies, df_tags, how='inner', on=['movieId', 'movieId'])

with open('movies_with_tags.csv', "wt", newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    last_id = -1
    # illegal_words = ["movies", "not", "r", "does", "in", "this", "é˜®ä¸€é¸£", "tã©a", "movie", "movies.", "movie."]
    relevance_filter = 0.9
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
            # for i in str(row['tag']).split():
            #     if str(i).lower() not in tags:
            #         if str(i).lower() not in illegal_words:
            #             tags.append(str(i).lower())
            if str(row['tag']).lower() not in tags:
                if row['relevance'] >= relevance_filter:
                    tags.append(str(row['tag']).lower())
            continue

        if row['movieId'] == last_id:
            # for i in str(row['tag']).split():
            #     if str(i).lower() not in tags:
            #         if str(i).lower() not in illegal_words:
            #             tags.append(str(i).lower())
            if str(row['tag']).lower() not in tags:
                if row['relevance'] >= relevance_filter:
                    tags.append(str(row['tag']).lower())
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
            # for i in str(row['tag']).split():
            #     if str(i).lower() not in tags:
            #         if str(i).lower() not in illegal_words:
            #             tags.append(str(i).lower())
            if str(row['tag']).lower() not in tags:
                if row['relevance'] >= relevance_filter:
                    tags.append(str(row['tag']).lower())
            tagline = ''