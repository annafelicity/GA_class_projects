# Project 4 -- Classifying Housing Prices and Web Scraping

In this project, we'll put your modeling skills to the test again to classify homes into a high or low price scheme. Depending on your comfort level, you will either scrape data directly from zillow.com _or_ use a dataset provided here to create a model. 

### Deliverable

- A pull request from a forked copy of this repository containing:
  - Your results (in whichever format, `.py` or Jupyter notebook, you choose)
  - An executive summary detailing how you operationalized your target variable, your choice of data to include, how you transformed your data, your findings, and your judgment on how strong your model is.

### Project Set-up

Your data source can come from one of two places:

1. There is a dataset provided in this repository on housing prices with several key features -- it is fairly barebones but sufficient to, with some exploratory data analysis, create a good model here.
2. You are encouraged, however, to put some of the web scraping tools (such as BeautifulSoup) to the test! There are times where we have to gather or manipulate data from outside sources and this is a good time to test those skills and develop them further. 

### Suggested Process

- Begin by exploring the provided data. Are there any trends that you see? What type of data munging might be required? 
- Generate some classification models, remembering to:
  - Guard against overfitting through regularization and through comparing to holdout samples (including train/split and cross-validation)
  - Use a variety of techniques to compare how effective models are across different iterations
- Depending on your familiarity with the material and available time, use BeautifulSoup to scrape new or additional data from zillow.com
  - Within each page, find the information that you want to collect (remember to use Chrome's Inspect features!)
  - Save one of the pages locally and develop the necessary functions to collect that data
  - Once you're confident that you can successfully scrape one page, figure out how to loop over multiple pages and collect that data however you like (across different zipcodes, within the same zipcode, etc.)
  - Across pages, collect the data you want
  - Convert your saved data into a Pandas dataframe and begin modeling!

### Things you should try out!

Your ultimate goal is to create a model that you believe works the best, given the data that you have. How you develop that model is up to you (though we will talk at length about good ways to approach the modeling process). We should see some, if not all, of the following techniques in your modeling process:

- Use of regularization when warranted
- Cross-validation and train/test split to avoid overfitting
- Use of different hyperparameters (_k_ in _k_-nearest neighbors, alpha in regularization cases)
- Use of different features and different data transformations
- GridSearch to iterate over different sets of hyperparameters efficiently

Remember that modeling is not a linear process -- we have a large toolbox of different tools that make sense at different times. Use them judiciously and appropriately! 
