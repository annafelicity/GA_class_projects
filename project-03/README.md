# Project 3 -- Estimating Flight Ticket Price Using Linear Regression

In this project, we're going to put your new modeling and data transformation skills to the test! We will be using data provided by the Bureau of Transportation Statistics to predict the price of airline tickets for flights leaving O'Hare and Midway.

## The Data

The data we'll be using is a modified form of data provided [here](https://www.transtats.bts.gov/Fields.asp?Table_ID=272). The data has been cleaned up somewhat (though not completely!) and subset to flights leaving from MDW and ORD. The available fields are:

- InitID: Unique Identifier for Ticket
- FarePerMile: The amount paid per mile of flight
- Coupons: How many tickets were purchased in the order
- Origin: The departure airport of the flight
- RoundTrip: Was the ticket a round trip ticket or not?
- OnLine: Was the departing flight on the same operating carrier that it was booked on or not?
- RPCarrier: Reporting carrier of the flight (crosswalk table can be found [here](https://www.transtats.bts.gov/Oneway.asp?Field_Desc=Reporting%20Carrier&Field_Type=Char&Sel_Cat=REPORTING_CARRIER&Lookup_Table=L_CARRIERS&Sel_Var=PASSENGERS&Sel_Stat=Sum&Data_Type=CAT&Percent_Flag=0&Display_Flag=0))
- Passengers: Number of passengers on the flight
- ItinFare: Itinerary fare per passenger
- BulkFare: Was the ticket part of a bulk order of tickets?
- Distance: How many miles was the flight?
- DistanceGroup: Pre-binned version of Distance (crosswalk table can be found [here](https://www.transtats.bts.gov/Oneway.asp?Field_Desc=Distance%20Group%2C%20in%20500%20Mile%20Intervals&Field_Type=Num&Sel_Cat=DISTANCE_GROUP&Lookup_Table=L_DISTANCE_GROUP_500&Sel_Var=PASSENGERS&Sel_Stat=Sum&Data_Type=CAT&Percent_Flag=0&Display_Flag=0))

The data can be found at [here](./airline.csv) and, if you need it, a 10% subsample can be found [here](./airline_10.csv).

## Your Task

Unlike Projects 1 and 2, Project 3 (and the projects to follow) are much more freeform. Instead of giving you steps to follow, we leave the development up to you, within a few guidelines.

For this project, you will clean and prepare the data given to you above. Once you've prepared the data, please use it to create a linear regression that predicts the fare of a ticket (`ItinFare`) on some or all of the features in the data set. 

You are free to return this project in any format you prefer (`.py` file, Jupyter Notebook, etc.) but please add and commit your results to a forked copy of this repository and issue a Pull Request when you're complete.

Please include the following in your submission:

- Your exploratory data analysis of the given data 
- Any plots of the data that might be useful for exploration
- Train, Test and Split your data, leaving a hold-out set for a final test
- Transform your data into whatever features you determine are correct. Defend your justifications and assumptions
- Model your data, using linear regression. Discuss your findings.
- Use Lasso and/or Ridge regression. Are they an improvement on the basic linear regression model? Discuss what Lasso and Ridge regressions are doing.
- For each of your models, generate plots comparing your actual values to the values predicted by your models. How do you interpret these findings?
- Test each of your models with your hold-out set of data. How do they compare to your results when using the data you modeled with?
- Discuss your models. Which would you choose? Why?
- Discuss the coefficients on your final model. How would you interpret them?

Happy modeling!

### A note

This is based off of real data which, you will come to learn, is not easy to model. Additionally, linear regression is a modeling technique that is easy to interpret but is difficult to use to create a highly accurate model. Don't worry if your models are not super accurate -- we'll discuss more and more ways over the next few weeks to create more predictive models. 
