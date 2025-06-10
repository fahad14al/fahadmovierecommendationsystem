import pandas as pd
import streamlit as st
import pickle


# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# Load data
movies_dict = pickle.load(open('movie_dic.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.title('Movie Recommender System')

select_movie_name = st.selectbox(
    "Select a movie:",
    movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(select_movie_name)
    st.write("Recommended Movies:")
    for i in recommendations:
        st.write(i)
