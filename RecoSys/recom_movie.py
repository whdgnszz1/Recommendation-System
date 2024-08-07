import os
import pandas as pd

base_src = '../machine_learning_data'
u_data_src = os.path.join(base_src, 'u.data')
r_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv(u_data_src,
                      sep='\t',
                      names=r_cols,
                      encoding='latin-1')
ratings = ratings.set_index('user_id')

base_src = '../machine_learning_data'
u_item_src = os.path.join(base_src, 'u.item')
i_cols = ['movie_id', 'title', 'release date', 'video release date',
          'IMDB URL', 'unknown', 'Action', 'Adventure', 'Animation',
          'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
          'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
movies = pd.read_csv(u_item_src,
                     sep='|',
                     names=i_cols,
                     encoding='latin-1')
movies = movies.set_index('movie_id')


def recom_movie(n_items):
    movie_mean = ratings.groupby(['movie_id'])['rating'].mean()
    movie_sort = movie_mean.sort_values(ascending=False)[:n_items]
    recom_movies = movies.loc[movie_sort.index]
    recommendations = recom_movies['title']
    return recommendations

print(recom_movie(5))
