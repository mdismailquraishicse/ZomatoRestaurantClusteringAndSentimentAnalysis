from flask import Flask, render_template, request
import pickle
import pandas as pd
import restaurant_recommender as rr

df = pd.read_csv('./data/Zomato Restaurant names and Metadata.csv')
df = df[['Name','Links','Cuisines']]
restaurant_similarity_score = pickle.load(open('./pickle/res_sim_scor.pkl','rb'))
similarity_score_for_people = pickle.load(open('./pickle/sim_scor_for_ppl.pkl','rb'))
user_based_pvt = pickle.load(open('./pickle/userbasedpvt.pkl','rb'))
vector_df = pickle.load(open('./pickle/vector.pkl','rb'))
restaurant_names= list(vector_df.index)
app = Flask("__name__")
@app.route('/')
def index():
    return render_template("index.html",
                           restaurant_names = restaurant_names
                           )
@app.route('/recommend', methods=["GET","POST"])
def recommend():
    name = request.form.get('userinput')
    rec = rr.recommend_restaurants(name,10)
    return render_template("recommendations.html",
                           restaurants= rec,
                           restaurant_names= restaurant_names
    )

if __name__=="__main__":
    Flask.run(debug=True)