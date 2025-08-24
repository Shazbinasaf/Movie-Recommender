import streamlit as st
import pandas as pd
import kagglehub
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download dataset
path = kagglehub.dataset_download("harshshinde8/movies-csv")

# Load movies
movies = pd.read_csv(f"{path}/movies.csv")

# Preprocess
movies['genres'] = movies['genres'].fillna('')

# Vectorize genres
cv = CountVectorizer(tokenizer=lambda x: x.split('|'))
genre_matrix = cv.fit_transform(movies['genres'])

# Cosine similarity
cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

# Index mapping
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# Streamlit UI
st.title("🎬 Movie Recommendation System")
selected_movie = st.selectbox("Pick a movie:", movies['title'].sample(50))

def recommend(title, num_recommendations=5):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    return movies.iloc[[i[0] for i in sim_scores]]['title']

if st.button("Recommend"):
    st.subheader("You may also like:")
    for rec in recommend(selected_movie):
        st.write(f"👉 {rec}")
