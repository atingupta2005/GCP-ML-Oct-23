import streamlit as st
import pandas as pd
import clip
import torch
from sklearn.metrics.pairwise import cosine_similarity
import pickle
from thefuzz import fuzz

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load('ViT-B/32', device)

# load embeddings from file
with open('embeddings.pkl','rb') as f:
    image_embeddings = pickle.load(f)

dfImages = pd.read_csv("images_to_txt.csv")

st.header('Image Search App')
search_term = 'a picture of ' + st.text_input('Search: ')
my_search_term = search_term.replace('a picture of ', '')
search_embedding = model.encode_text(clip.tokenize(search_term).to(device)).cpu().detach().numpy()

st.sidebar.header('App Settings')
top_number = st.sidebar.slider('Number of Search Results', min_value=1, max_value=30)
picture_width = st.sidebar.slider('Picture Width', min_value=100, max_value=500)

df_rank = pd.DataFrame(columns=['image_path','sim_score'])

for path,embedding in image_embeddings.items():
    sim = cosine_similarity(embedding,
                            search_embedding).flatten().item()
    df_rank = pd.concat([df_rank,pd.DataFrame(data=[[path,sim]],columns=['image_path','sim_score'])])
df_rank.reset_index(inplace=True,drop=True)

df_rank.sort_values(by='sim_score',
                    ascending=False,
                    inplace=True,
                    ignore_index=True)

# display code: 3 column view
col1, col2, col3 = st.columns(3)

for row in dfImages.iterrows():
    score = fuzz.token_set_ratio(row[1][2], my_search_term)
    
    #print("search_term: ", my_search_term, score)
    if score > 60:
        print("score: ", score)
        print(f"Searched {my_search_term} in image: ", row[1][1])
        print(row[1][2])
        st.image(f"images/{row[1][1]}",width=picture_width)

df_result = df_rank.head(top_number)
for i in range(top_number):
    if i % 3 == 0:
        with col1:
            st.image(df_result.loc[i,'image_path'],width=picture_width)
    elif i % 3 == 1:
        with col2:
            st.image(df_result.loc[i,'image_path'],width=picture_width)
    elif i % 3 == 2:
        with col3:
            st.image(df_result.loc[i,'image_path'],width=picture_width)