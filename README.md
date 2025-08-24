🎬 Movie Recommendation System

A simple Movie Recommendation System built with Streamlit that suggests movies based on their genres.
This project uses the movies-csv Kaggle dataset (harshshinde8/movies-csv) and applies content-based filtering with cosine similarity.

🚀 Features

Interactive Streamlit Web App

Select a movie and get recommendations

Content-based filtering (using genres)

Uses cosine similarity for recommendations

Ready to extend with ratings-based collaborative filtering

📂 Dataset

Dataset: Movies CSV (Kaggle)

It contains:

movies.csv → Movie IDs, Titles, Genres

ratings.csv → User Ratings (optional for collaborative filtering)

🛠️ Installation

Clone the repo / create a new folder and add app.py

Install dependencies:

pip install streamlit pandas scikit-learn kagglehub


Run the Streamlit app:

streamlit run app.py

📜 Code Overview

Data Loading: Downloads dataset using kagglehub

Preprocessing: Fills missing genres

Vectorization: Converts genres into a feature matrix using CountVectorizer

Similarity: Computes cosine similarity between movies

UI: Streamlit app with a dropdown menu and recommendation button

🎮 How to Use

Launch the app with streamlit run app.py

Select a movie from the dropdown

Click Recommend

Get a list of similar movies

🔮 Future Improvements

Add ratings-based collaborative filtering (Matrix Factorization, SVD, etc.)

Hybrid approach: combine genres + ratings

Add search bar for movies

Deploy on Streamlit Cloud / HuggingFace Spaces

📸 Demo (example flow)

User selects Toy Story (1995)

Recommendations:

A Bug’s Life (1998)

Monsters, Inc. (2001)

Finding Nemo (2003)

Shrek (2001)

Ice Age (2002)

👨‍💻 Author

Built by Shaz Bin Asaf ✨
(Feel free to fork & extend this project!)
