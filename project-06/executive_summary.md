#### Problem Statement:
Make recommendations to Netflix about what movie factors are the most direct predictors of rating using data from IMDB

#### Data:
Given time constraints, my model used the top 250 IMDB movies of all time (a dataset easily scraped from the IMDB website). A target variable was created using the "Ratings" data in which two categories were created to determine which factors made a movie truly amazing versus merely good. The median value of the top 250 movies was used as the splitter value.

#### Feature Selection:
The final feature selection for the model included the following categories of data:

•Runtime

•Director

•Rating

•Actors

•Genre

•Year

Time constraints also limited the feature selection, as certain data columns required a significant amount of data cleaning to make them useable for our purposes. With more time, I would see if incorporting these columns improved the model. Columns not considered at this time included:

•the "Awards" column which contained complicated strings that mixed number of awards with award types

•the "Writer" column which had a mix of all sorts of data in each row that needed to be extracted into separate columns

Other features, upon evaluation, would have had little effect on the modeling. The following were not included:

•"Country" because the vast majority of values were the US or the US in combination with another or other countries 

•"Language", ditto 

•"Metascore" was left out of the modeling as it contained a high number of empty values and also is based on another website's data, which raised questions as to use in an IMDB analysis

#### Modeling:
I tried a model with a versatile random-forest tree classifier model. Then I used the  feature importances tool to determine which of the features had the most impact on movie rating. The model performed fairly well when fit to the entire data set with a score of 0.884. When scored using a train/test split to mimic unseen data, the model revealed itself to be somewhat overfit, although not terribly so (the scores then ranged from .67 to .595). Looking at confusion matrices and classification scores such as precision and recall, the model did the best job at predicting the amazing movies and a less quality job at predicting the merely good movies. But given that Netflix would want to show viewers the most amazing movies to watch, this is acceptable.

Looking at the top 50 important features, the following proved the most significant predictors of having an "amazing" rating:

•Runtime had the most significant impact on the model and was the only feature to rank above 2 percent

•Certain actors, directors and years hovered in the 1 to 2 percent range of impact; interestingly these were not necessarily what one might expect (for example: director Asghar Farhadi as well as other foreign directors) 

•R and "Not Rated" were the only rating categories to make the top 20 important features

•After the top 20, the feature importance dropped to under .8 percent

#### Summary and Future Exploration:
According to this model, Netflix should consider collecting individual movie data with respect to all of the factors included in the model. No one particular feature category, aside from Runtime, jumped out as having particular impact. But particular directors, actors, ratings, genres, and years did have noticeably larger impact. 

This data then can be used to predict which movies would rate highly to a wide range of people. 

Future exploration that might improve this model and/or determine other types of data to collect would include adding the number and type of awards into the model, looking at the writer, and separating the actor column into individual actor names, rather than relying on CountVectorizer to group them. 

The biggest limitation of this model lies in the small dataset that only focuses on relatively high-rated movies. Ideally, with more time, the entire IMDB data set would be used, and the target would be broken down into several categories (e.g. amazing, good, mediocre, poor) to achieve better understanding about what makes a high-rated movie with respect to what makes a mediocre or low-rated movie.