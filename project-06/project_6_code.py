#1)import all the stuff
import numpy as np
import pandas as pd
from  sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier, ExtraTreesClassifier
from sklearn.preprocessing import FunctionTransformer, LabelBinarizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline, make_union
from sklearn.model_selection import StratifiedKFold

#2)import data scraped from web and saved to csv
movie_data = pd.read_csv("IMDBTop250.csv")

#3)operationalize y into two categories: "amazing"=1 and "good"=0
#this is the target variable
is_amazing = movie_data["imdbRating"].apply(lambda x: 0 if x <= np.median(movie_data["imdbRating"]) else 1)

#4)make X (doing this as a pipeline in case I want to scrape more data later)

#4a)write all my definitions
#column extractors:
def actors_col(df):
    return df["Actors"].values.reshape(-1, 1)

def director_col(df):
    return df["Director"].values.reshape(-1, 1)

def genre_col(df):
    return df["Genre"].values.reshape(-1, 1)

def plot_col(df):
    return df["Plot"].values.reshape(-1, 1)

def rated_col(df):
    return df["Rated"].values.reshape(-1, 1)

def runtime_col(df):
    return df["Runtime"]

def title_col(df):
    return df["Title"].values.reshape(-1, 1)

def year_col(df):
    return df["Year"].values.reshape(-1, 1)

#clean runtime col
def runtime_fix(df):
	df = df.str.replace(" min","")
	df = df.apply(int)
	return df.values.reshape(-1, 1)

#fill nan in rated col
def not_rated(column):
	column.fillna("NOT RATED", inplace=True)
	return column

#todense for CountVectorizer pipes
def dense(sparse):
	return sparse.todense()

#4b) make pipelines:
actors_pipe = make_pipeline(FunctionTransformer(actors_col, validate=False),
                         CountVectorizer(ngram_range=(2, 3), min_df=2),
                         FunctionTransformer(dense, validate=False))

director_pipe = make_pipeline(FunctionTransformer(director_col, validate=False),
							LabelBinarizer())

genre_pipe = make_pipeline(FunctionTransformer(genre_col, validate=False), CountVectorizer())

rated_pipe = make_pipeline(FunctionTransformer(rated_col, validate=False), FunctionTransformer(not_rated, validate=False), LabelBinarizer())

runtime_pipe = make_pipeline(FunctionTransformer(runtime_col, validate=False),
							FunctionTransformer(runtime_fix, validate=False))

year_pipe = make_pipeline(FunctionTransformer(year_col, validate=False))

#4c) make feature union:
union = make_union(actors_pipe, director_pipe, genre_pipe, plot_pipe, rated_pipe, runtime_pipe, title_pipe, year_pipe)
X = union.fit_transform(movie_data)

#5) do train/test split and fit first model to try plus visualize the predictions



