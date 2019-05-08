from Movie.data_retrieval import get_data, merge_data
from Movie.connect import create_engine_pgsql, create_engine_mysql, insert_to_db
from Movie.aggregation import agg_rating_movie, agg_rating_tag

df_movie, df_rating, df_tag = get_data()
df_movie_rating, df_movie_tag, df_movie_tag_rating = merge_data(df_movie, df_rating, df_tag)
df_agg_rating = agg_rating_movie(df_movie_rating)
df_agg_rating_genre = agg_rating_tag(df_movie_tag_rating)

#print(df_movie[:5], df_rating[:5], df_tag[:5])
#print(df_movie_tag_rating[:5].drop_duplicates())
#print(df_agg_rating[:10])


#engine = create_engine_pgsql()
engine = create_engine_mysql()

insert_to_db(engine,df_agg_rating,'agg_movie_rating')
insert_to_db(engine,df_agg_rating_genre,'agg_rating_genre')



