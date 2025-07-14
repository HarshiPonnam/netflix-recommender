import streamlit as st
import pickle
import pandas as pd

# Load the model files
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


# Recommender logic
def recommend(movie):
    movie = movie.lower()
    if movie not in movies['title'].str.lower().values:
        return ["Movie not found."]

    index = movies[movies['title'].str.lower() == movie].index[0]
    distances = list(enumerate(similarity[index]))
    movie_list = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]
    return [movies.iloc[i[0]].title for i in movie_list]


# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="centered")
st.title("🎬 Movie Recommender System")
st.markdown("Find movies similar to your favorites!")

# Dropdown for movie selection
selected_movie = st.selectbox("Choose a movie", movies['title'].values)

# Button to trigger recommendations
if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.markdown("### 🍿 You might also like:")
    for movie in recommendations:
        st.write("➤", movie)
