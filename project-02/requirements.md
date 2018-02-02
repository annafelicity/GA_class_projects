# Project 2 -- Data Analysis Using Iowa Liquor Store Data

Under Iowa state law, those licensed to sell liquor in the state of Iowa must submit the amount of alcohol purchased to the state (i.e., Joe's Bar in Des Moines purchases 300 bottles of Grey Goose vodka). The state of Iowa provides this information free-of-charge to the public.

As an enterprising junior Data Scientist, you've been asked to provide an analysis of this data. You'll be using Python, Pandas, and some of the other tools that we've learned acquired this week. Most importantly though, have fun digging deeply into a fascinating dataset!

## The Data

The data comes in two forms -- one full-sized set of data and, if you need a smaller set of data, a 10% random sample is also available (and can be useful to get your code running first before you dive into the larger set of data).

- [Full Version](https://www.dropbox.com/sh/pf5n5sgfgiri3i8/AACkaMeL_i_WgZ00rpxOOcysa?dl=0)
- [10% Subsample](https://drive.google.com/file/d/0Bx2SHQGVqWaseDB4QU9ZSVFDY2M/view)

## Deliverable

Your deliverable will be in two parts: 1) an executive summary of your findings (`executive_summary.md`) based partly on the questions posed here as well as from your own independent data analysis and 2) the script used to derive your results (`results.py`).

`results.py` will have two sections:
- Answers to the provided 9 questions below
- Your own individual data analysis to flesh out your executive summary.

Please submit your deliverable via pull request to the `DSI-CHI-2/project-02` repository.

## Getting Started

1. Fork the `DSI-CHI-2/project-02` repository to your own GA github account.
2. Clone it to your local machine.
3. Before answering the questions, take some time to explore the data (you can find the dataset you should use [here](https://www.dropbox.com/sh/pf5n5sgfgiri3i8/AACkaMeL_i_WgZ00rpxOOcysa?dl=0) or if you need a smaller subsection, a 10% sample [here](https://drive.google.com/file/d/0Bx2SHQGVqWaseDB4QU9ZSVFDY2M/view?usp=sharing). You should also familiarize yourself with the codebook by looking [here](https://data.iowa.gov/Economy/Iowa-Liquor-Sales/m3tr-qhgy). Try and answer these questions first:
  1. What is the level of observation?
  2. How many rows and columns are there?
  3. Is data missing? If so, from which columns? What are some potential reasons that they are missing?
  4. What questions might you want to investigate with this data? Do you have any hypotheses about what you might find?

## Questions 1-9

1. What is the shape of the dataset? How many rows and columns? What types are each of the columns in the dataset? 
2. How much missing data is there? What steps do you need to take to clean the data? 
3. Were all stores in the dataset open in 2015? If not, what steps do you think are appropriate to address that? 
4. What is the yearly liquor sales for each store in 2015? What is the profit for each store in 2015?
5. Create a broader category for each liquor type (for example "100 Proof Vodka" and "Imported Vodka" both could fall under a "Vodka" category). How many different liquors went into each category? What categories had the highest number of bottles sold? What category has the highest profits?
6. Create a table that contains the following:
  - Each broad category you created
  - Each liquor that falls in that category
  - The average, max, min, and total volume sold and the price per bottle sold
7. Your employers are curious about county-by-county differences -- what is the most popular category of liquor in each category? Do all counties share the same tastes?
8. Some counties have a very high population and some counties have a very low population. Assign county stores to being either large or small (I leave it up to you to determine what that cut-off is!) Do high population counties have a smaller or larger number of stores? Do high population counties purchase more bottles of liquor on average in a given order? Are there different tastes across high population and low population counties?
9. Pick one of the questions asked above. How would you show your results visually? 

## Open Exploration

Now that you are well acquainted with this dataset, you will be doing some open data exploration. Have you found any interesting facts that you want to dig into? Any hypotheses about alcohol consumption in Iowa that seem plausible (or that you may want to disprove)? This is your chance!

Set out your question in your Executive Summary and get to work. It's not necessary to definitively prove or disprove your hypothesis (and in many cases, we often cannot due to time or data limitations). The most important part is clarity in what you're trying to answer, a reasoned explanation of what you have found (including portions of your defense that may be weak or require further research), and (if warranted) prescriptions for next steps. Have fun with this part -- data exploration can be one of the most challenging and rewarding parts of being a data scientist!
