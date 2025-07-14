🎬 Netflix-Style Movie Recommender System

A content-based movie recommendation system built with **Python**, **pandas**, **scikit-learn**, and **Streamlit**. This app suggests 5 similar movies based on a user-selected movie by analyzing movie metadata like overview, genres, cast, crew, and keywords.
Deployed using **Streamlit Cloud**, this project demonstrates my ability to clean and transform data, apply NLP techniques, and build a fully interactive web app.

🧠 Features
- Recommend 5 similar movies based on your selected movie
- Processes data from the TMDB 5000 Movie Dataset
- Combines key metadata: overview, genres, cast, crew, and keywords
- Applies **NLP** with `CountVectorizer` and **cosine similarity**
- Lightweight and fast — `.pkl` files used for instant loading
- Clean and user-friendly interface built with Streamlit


🛠️ Tech Stack

- **Frontend/UI:** Streamlit  
- **Backend/Data:** Python, pandas, numpy  
- **Machine Learning:** scikit-learn (cosine similarity, vectorization)  
- **Dataset:** [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)  
- **Other Tools:** Jupyter Notebook, GitHub


🗂️ Project Structure

app.py # Main Streamlit app

movies.pkl # Processed movie metadata

similarity.pkl # Cosine similarity matrix

tmdb_5000_movies.csv # Original movie data

tmdb_5000_credits.csv # Original credits data

requirements.txt # Python dependencies

  
Install dependencies:
pip install -r requirements.txt

Run the app:
streamlit run app.py

📝 Dataset Info
The project uses the TMDB 5000 Movie Dataset from Kaggle, which includes metadata like:
Overview
Genres
Keywords
Cast and crew

Nested fields (like genres and crew) were cleaned using ast.literal_eval() and parsed into usable Python objects.

🎓 What I Learned
How to clean and transform real-world datasets
Creating tag-based features for recommendation engines
Applying NLP + cosine similarity to build recommender logic
Packaging models using .pkl files for efficient deployment
Building and deploying a full-stack project on Streamlit Cloud

🙋‍♀️ About Me
I'm a Computer Science student passionate about building real-world ML applications. Feel free to connect on LinkedIn or explore more of my projects!
