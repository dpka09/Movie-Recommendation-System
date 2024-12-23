import streamlit as st
import numpy as np
import pandas as pd
import pickle
import requests


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    
    movies_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]

    for x in movies_list:
        movie_id = movies.iloc[x[0]].id
        recommended_movies.append(movies.iloc[x[0]].title)
    return recommended_movies


movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Please select a title',
    movies['title'].values
)

if st.button('Recommend'):
    names=  recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with st.container():
        col1.write(names[0])

    with st.container():
        col2.write(names[1])

    with st.container():
        col3.write(names[2])
    
    with st.container():
        col4.write(names[3])

    with st.container():
        col5.write(names[4])
    

    

    