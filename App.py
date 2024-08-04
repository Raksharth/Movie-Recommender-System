import streamlit as st
import pickle
import pandas as pd

## Importing movies list from the pickle file
Movies_List = pickle.load(open('Movie.pkl', 'rb'))
Movie = pd.DataFrame(Movies_List)  # Assuming the pickled file is a DataFrame or dictionary
Movies_List = Movie['title'].values

## Importing Similarity Pickle File
Similarity = pickle.load(open('similarity.pkl', 'rb'))

## Creating recommend function
def Recommend(Movie_Name):
    Movie_Index = Movie[Movie['title'] == Movie_Name].index[0]
    Distances = Similarity[Movie_Index]
    Movies_List = sorted(list(enumerate(Distances)), reverse=True, key=lambda x: x[1])[1: 6]

    Recommended_Movies = []
    for i in Movies_List:
        Recommended_Movies.append(Movie.iloc[i[0]][1])
    return Recommended_Movies

## For page Title:
st.title('Movie Recommender System')

## For Select Box:
Select_Movie_Name = st.selectbox(
    "Select the Movie",
    Movies_List
)

## Placing the Recommend Button
if st.button("Recommend"):
    Recommendations = Recommend(Select_Movie_Name)
    for i in Recommendations:
        st.write(i)