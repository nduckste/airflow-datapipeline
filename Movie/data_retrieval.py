import pandas as pd

FILEPATH_MOVIE =r"../Files/movies.csv"
FILEPATH_RATING =r"../Files/ratings.csv"
FILEPATH_TAG =r"../Files/tags.csv"

def get_data():
    df_movie = pd.read_csv(FILEPATH_MOVIE, nrows=10000)
    df_rating = pd.read_csv(FILEPATH_RATING, nrows=10000)
    df_tag = pd.read_csv(FILEPATH_TAG, nrows=10000)
    return df_movie, df_rating, df_tag

def merge_data(df_movie, df_rating, df_tag):
    df_movie_rating = df_movie.merge(df_rating, how="inner", on="movieId")
    print(df_movie_rating.columns)

    df_movie_tag = df_movie.merge(df_tag, how="inner", on="movieId")
    print(df_movie_tag.columns)

    df_movie_tag_rating = df_movie_rating.merge(df_movie_tag, how="inner", on="userId")
    print(df_movie_tag_rating.columns)

    return df_movie_rating, df_movie_tag, df_movie_tag_rating
