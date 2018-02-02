# Project 5: Deployment and Reproducible Data Science through Kaggle Competitions 

Welcome to Week 5! This week is focused primarily on the concept of the Data Science Pipeline -- modeling (as we will discuss) is only one part of the broader discipline. 

As data scientists, one question we frequently have to tackle is how our model will be used once we have found a successful fit. We want to make sure that our incoming data is always transformed in the way that our model expects. We also want the data that our model generates (predictions, etc.) to be available in some sort of useful fashion. 

This week's project should challenge you to think of your model as one part of a number of steps. We will be relying on custom challenges within a website known as [Kaggle](https://www.kaggle.com/). This website runs challenges for data scientists that benefit from reproducible work and thoughtful tweaking.

## Requirements

You should have received an invitation to the following Kaggle In-Class challenges:

- [Project 5 Classification Challenge](https://inclass.kaggle.com/c/project-5-classification)
- [Project 5 Regression Challenge](https://inclass.kaggle.com/c/project-5-regression-challenge)

Information on each challenge, plus the data itself, is available on the Kaggle website. 

Your deliverables are:

1. At least one successful submission of your predictions to each challenge
2. At least two `.py` scripts (one for each challenge, more than two is fine) containing code that does the following:
  - Applies the same data transformation code to both the training and test data (this code should be kept in a function or functions _and/or_ make use of sklearn's Pipelines library)
  - Generates predictions and outputs the results in the required format for Kaggle. This will include transforming the predictions and ID numbers for each row into the proper format and exporting to csv (this code should be kept in a function or functions)
  - _Optionally_ use one or more of the following techniques:
    - Storing your model object to disk using `joblib` and loading it into memory for scoring
    - Use of the [argparse](https://docs.python.org/2/library/argparse.html) library to run your script with command line arguments. (You'll notice that we will not cover this in class at all -- it's worth a gander and learning how to use libraries on one's own is a valuable skill!)

## Suggested Workflow

This sort of work is probably best approached in stages. Remember that your ultimate goal is a high score on the challenge, so as you iterate on your model you should also be generating predictions using the test csvs for both challenges and uploading semi-frequently.

1. Perform exploratory data analysis and cleaning (as per usual)
2. Generate some test models and create predictions
3. Identify necessary steps to transform your predictions into Kaggle's expected state. Upload your first results to Kaggle and confirm that your transformations work.
4. Generate reproducible steps for:
  - Data transformation (what steps did you apply to the training data? How can you make them occur reproducibly and _in the same manner_ to your test data?)
  - Generating predictions (ensure that your fit model is not refit to your test data!)
  - Exporting predictions (can you reproducibly get the output done?)
5. Once the basic framework for your data pipeline is complete, iterate on your model, using your pipeline to efficiently generate results.

