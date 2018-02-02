# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 6: APIs + Random Forests

## Overview

This week, we learned about ensemble methods, APIs, and natural language processing. Now we're going to put these skills to the test. You've been hired by Netflix to examine what factors lead to certain ratings for movies. Given that Netflix does not currently store this type of data, your boss has suggested that you collect ratings and reviews data from IMDB. Netflix is no stranger to machine learning, however:

- Netflix uses random forests and decision trees to predict what types of movies an individual user may like.
- Using unsupervised learning techniques, they are able to continually update suggestions, listings, and other features of it's user interface.
- Netflix, however, hasn't focused on collecting data on the top movies of all time, and would like to add some of them to their offerings based on popularity and other factors.

**Point:** Your boss isn't sure where to start on this project, so your task is to collect the data and construct a random forest to understand what factors contribute to ratings.

## Project Summary
Acquire data from IMDB, and use whatever metrics you can collect to predict whether it is a good movie.

When you've finished your analysis, Netflix would like a report detailing your findings, with recommendations as to next steps.

Here are some questions to keep in mind:

- What factors are the most direct predictors of rating?
- You can use rating as your target variable. But it's up to you whether to treat it as continuous, binary, or multiclass.

**Goal**: Completed Jupyter notebook or `.py` file that includes modeling using a random forest and an blog post explaining your findings.

## Requirements
This is deliberately open ended. There is no starter code. It's up to you how to acquire the data, store the data, and what features you want to use. 

We expect you to use a **tree-based model**, but the rest of the decisions are up to you. 

We will be looking for the following things:
 - A clear problem statement & description of the goals of your study to be included in the final report
 - Data from IMDB
 - Cleaned and refined data
 - Visualization. Plots that describe your data and evaluate your model.
 - Tree-based models (use any combination of ensemble techniques: random forests, bagging, boosting). 
 - An executive summmary presenting the results of your findings as a report to Netflix, including:
  - a problem statement,
  - summary statistics of the various factors (e.g. year, number of ratings, etc.),
  - your model,
  - at least 2 graphics,
  - and your recommendations for next steps!

## Necessary Deliverables / Submission

- Jupyter notebook or `.py` file that contains your models and cleaning code
- A markdown file containing your executive summary.

## Rubric / What We're Looking For

*100% of this project review will come from the strength of your executive summary.*

We require your code as well (it should work and be as clean and well-written as possible) but we will pay particular focus to how you craft and discuss your findings within your executive summary. A template executive summary (written for the Titanic project) is included for your perusal, but you should feel free to work within whatever structure makes the most sense to you. 

We will look for the following in your executive summary:

1. Do you introduce your problem statement and how your model approaches it?
2. Do you discuss your data cleaning and exploration? Do you warn the reader of any potential weaknesses?
3. Do you discuss your modeling technique? Why did you choose one model and not the other? Is your model overfit (and why / why not)? 
4. Are you confident in the findings of your model? Why or why not?
5. What are extra steps that would make sense? Additional data that you would want? 

---

## Suggested Ways to Get Started

- You can get data on the top 250 movies on IMDB using the [IMBDpie API](https://github.com/richardasaurus/imdb-pie) 
- If you need additional data, you can either research additional APIs, or scrape it yourself using BeautifulSoup
- Read the docs for whatever technologies you use. Most of the time, there is a tutorial that you can follow, but not always, and learning to read documentation is crucial to your success!
