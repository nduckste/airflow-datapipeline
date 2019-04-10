from Movie.data_retrieval import get_data, merge_data

df_movie, df_rating, df_tag = get_data()
#print(df_movie[:5], df_rating[:5], df_tag[:5])
df_movie_rating, df_movie_tag, df_movie_tag_rating = merge_data(df_movie, df_rating, df_tag)
print(df_movie_tag_rating[:5].drop_duplicates())


