import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def make_recommendations(user_input, nr_recommendations):

    df = pd.read_csv("ml-latest/movies_with_tags.csv")
    df2 = pd.concat([df["tags"], pd.DataFrame([user_input])])
    vectorizer = CountVectorizer(stop_words='english')

    X = vectorizer.fit_transform(df2[0])
    cosine_sim = cosine_similarity(X[:-1], X[-1])

    similar_movies = list(enumerate(cosine_sim))
    similar_movies.sort(key=lambda x: x[1], reverse=True)

    recommendations = list()

    for movie in similar_movies[:nr_recommendations]:
        recommendations.append((df.iloc[movie[0]], movie[1]))

    return recommendations



if __name__ == "__main__":
    print(make_recommendations("I am looking for an animated comedy movie made by Studio Ghibli", 10))