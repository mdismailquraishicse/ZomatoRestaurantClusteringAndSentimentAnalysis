import pickle
import pandas as pd
import numpy as np

restaurant_similarity_score = pickle.load(open('./pickle/res_sim_scor.pkl','rb'))
similarity_score_for_people = pickle.load(open('./pickle/sim_scor_for_ppl.pkl','rb'))
user_based_pvt = pickle.load(open('./pickle/userbasedpvt.pkl','rb'))
vector_df = pickle.load(open('./pickle/vector.pkl','rb'))

def recommend_restaurants(restaurant_name,topn):
    index = vector_df.index.get_loc(restaurant_name)
    indices = restaurant_similarity_score[index].argsort()[-topn-1:-1][::-1]
    recomendations = []
    for i in indices:
        recomendations.append(vector_df.index[i])
    return recomendations