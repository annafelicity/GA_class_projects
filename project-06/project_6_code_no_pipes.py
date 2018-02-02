#1)import all the stuff
import numpy as np
import pandas as pd
from  sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier, ExtraTreesClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline, make_union
from sklearn.model_selection import StratifiedKFold

#2)import data scraped from web and saved to csv
movie_data = pd.read_csv("IMDBTop250.csv")

#3)operationalize y into two categories: "amazing"=1 and "good"=0
#this is the target variable
is_amazing = movie_data["imdbRating"].apply(lambda x: 0 if x <= np.median(movie_data["imdbRating"]) else 1)

#4)clean data and make X for modeling
#strip "min" from runtime (maybe retitle as runtime_minutes?)
movie_data["Runtime"] = movie_data["Runtime"].str.replace(" min","")
#turn runtime into number
movie_data["Runtime"] = movie_data["Runtime"].apply(int)

#make director dummies:
dir_dummies = pd.get_dummies(movie_data["Director"], prefix="Dir")

#fill nan in rated col
movie_data["Rated"].fillna("NOT RATED", inplace=True)

#make rated dummies:
rated_dummies = pd.get_dummies(movie_data["Rated"])

#apply CountVectorizer to genre:

genre_words = CountVectorizer.fit_transform(movie_data["Genre"])


#actors column:
#apply CountVectorizer as below (can I name column names like with get dummies?)
#CountVectorizer(ngram_range=(2, 3), min_df=2)


X = movie_data["Runtime"].copy() #add in any other columns that don't need changes
X = X.join(dir_dummies)
#join on all other dummy and CVect dfs
