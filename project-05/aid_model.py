#this is for a linear regression model

#1) import relevant libraries and stuff
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import FunctionTransformer, LabelBinarizer
from sklearn.pipeline import make_pipeline, make_union

#2) import train and test data
aid_train = pd.read_csv('university_train.csv')
aid_test = pd.read_csv('university_test.csv')

#3) operationalize y (y =
target_train = aid_train["percent_on_student_loan"]

#4) write all my definitions

#column returns
def female_col(df):
    return df["FEMALE"].values.reshape(-1, 1)

def faminc_col(df):
    return df["MD_FAMINC"].values.reshape(-1, 1)

def control_col(df):
    return df["CONTROL"].values.reshape(-1, 1)

def locale_col(df):
    return df["LOCALE"].values.reshape(-1, 1)

def state_col(df):
    return df["STABBR"].values.reshape(-1, 1)

def ccugprof_col(df):
    return df["CCUGPROF"].values.reshape(-1, 1)

def preddeg_col(df):
    return df["PREDDEG"].values.reshape(-1, 1)

def highdeg_col(df):
    return df["HIGHDEG"].values.reshape(-1, 1)

def drop_col(dummies_df):
	return dummies_df[:,:-1]

#5) make pipelines to clean/transform data column by column for x 
female_pipe = make_pipeline(FunctionTransformer(female_col, validate=False))
faminc_pipe = make_pipeline(FunctionTransformer(faminc_col, validate=False))
control_pipe = make_pipeline(FunctionTransformer(control_col, validate=False), 
	LabelBinarizer(), FunctionTransformer(drop_col, validate=False))
locale_pipe = make_pipeline(FunctionTransformer(locale_col, validate=False),
	LabelBinarizer(), FunctionTransformer(drop_col, validate=False))
state_pipe = make_pipeline(FunctionTransformer(state_col, validate=False),
	LabelBinarizer(), FunctionTransformer(drop_col, validate=False))
ccugprof_pipe = make_pipeline(FunctionTransformer(ccugprof_col, validate=False),
	LabelBinarizer(), FunctionTransformer(drop_col, validate=False))
preddeg_pipe = make_pipeline(FunctionTransformer(preddeg_col, validate=False),
	LabelBinarizer(), FunctionTransformer(drop_col, validate=False))
highdeg_pipe = make_pipeline(FunctionTransformer(highdeg_col, validate=False),
	LabelBinarizer(), FunctionTransformer(drop_col, validate=False))

#6) create X with make_union
union = make_union(female_pipe, faminc_pipe, control_pipe, locale_pipe, state_pipe, 
                   ccugprof_pipe, preddeg_pipe, highdeg_pipe)

#7) fit train to a model 
lr = LinearRegression()
lr.fit(union.fit_transform(aid_train), target_train)

#8) predict the model with the test dataset
predictions = lr.predict(union.transform(aid_test))

#9) export results
def evaluation_transformation(dataset, predictions):
    dataset = dataset.join(pd.DataFrame(predictions, columns=['Prediction']))
    dataset[['id_number', 'Prediction']].to_csv('submission_aid_final.csv', index=False)

evaluation_transformation(aid_test, predictions)


