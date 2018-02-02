#this is for a classification method using K Nearest Neighbors

#1) import relevant libraries and stuff
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, Imputer, FunctionTransformer, LabelBinarizer
from sklearn.pipeline import make_pipeline, make_union

#2) import train and test data
school_train = pd.read_csv('school_data_training.csv')
school_test = pd.read_csv('school_data_test.csv')

#3) operationalize y (y = "probation")
target_train = school_train["probation"]

#4) write all my definitions
#[Note: I want to figure out how to make a generic column extractor]

def avg_student_col(df):
    return df["Average Student Attendance"]

def healthy_schools_col(df):
    return df["Healthy Schools Certified?"]

def misconduct_col(df):
    return df["Rate of Misconducts (per 100 students) "]

def avg_teacher_col(df):
    return df["Average Teacher Attendance"]

def iep_col(df):
    return df["Individualized Education Program Compliance Rate "]

def ward_col(df):
    return df["Ward"]

def police_d_col(df):
    return df["Police District"]

#strip percentage signs
def strip_percent(column):
    column = column.str.replace("%", "")
    column = column.apply(float)
    return column

def return_array(column):
    return column.values.reshape(-1, 1)

#5) make pipelines to clean/transform data column by column for x 

avg_stud_pipe = make_pipeline(FunctionTransformer(avg_student_col, validate=False),
                         FunctionTransformer(strip_percent, validate=False),
                         FunctionTransformer(return_array, validate=False))

avg_teach_pipe = make_pipeline(FunctionTransformer(avg_teacher_col, validate=False),
                         FunctionTransformer(strip_percent, validate=False),
                         FunctionTransformer(return_array, validate=False))

iep_pipe = make_pipeline(FunctionTransformer(iep_col, validate=False),
                         FunctionTransformer(strip_percent, validate=False),
                         FunctionTransformer(return_array, validate=False))

miscon_pipe = make_pipeline(FunctionTransformer(misconduct_col, validate=False),
                         FunctionTransformer(return_array, validate=False))

police_pipe = make_pipeline(FunctionTransformer(police_d_col, validate=False),
                         FunctionTransformer(return_array, validate=False),
                         LabelBinarizer())

ward_pipe = make_pipeline(FunctionTransformer(ward_col, validate=False),
                         FunctionTransformer(return_array, validate=False),
                         LabelBinarizer())

#6) create X with make_union
union = make_union(avg_stud_pipe, avg_teach_pipe, iep_pipe, miscon_pipe, police_pipe, ward_pipe)
union.fit_transform(school_train)

#then add standard scaler for knn
#note if I change this to logistic regression, drop this part 
#and add drop a column in the relevant dummy column pipes
final_pipe = make_pipeline(union, StandardScaler())
final_pipe.fit_transform(school_train)

#7) fit train to a model 
#(try KNN and LogReg--remember LogReg needs one dummy 
#dropped from each set of dummies)
knn = KNeighborsClassifier()
knn.fit(final_pipe.fit_transform(school_train), target_train)

#8) predict the model with the test dataset
predictions = knn.predict(final_pipe.transform(school_test))

#9) export results
def evaluation_transformation(dataset, predictions):
    dataset = dataset.join(pd.DataFrame(predictions, columns=['Prediction']))
    dataset[['Id', 'Prediction']].to_csv('submission_school_final.csv', index=False)

evaluation_transformation(school_test, predictions)
