import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path_full = "Iowa_Liquor_Sales_reduced.csv"

file_path_sample = "Iowa_Liquor_sales_sample_10pct.csv"

df = pd.read_csv(file_path_full)

print("\nProblem 1\n")
#What is the shape of the dataset? How many rows and columns?
print("This dataset has a shape of %s rows and %s columns." % (df.shape[0], df.shape[1])) 
#What types are each of the columns in the dataset?
print("\nThe column types are as follows:\n\n", df.dtypes)

print("\nProblem 2\n")
# How much missing data is there? 
print("We can see how much missing data there is by looking at the following accounting:\n\n",df.isnull().sum())
#What steps do you need to take to clean the data?
print("\nTo clean the data, there are several things that need to be done.\n\nA: Address missing data: You could take the following steps:\n1) re: missing county number and missing category number, replace with a float number that is identifiable as missing (like 999999.9) as the existing values are floats. 2) re: missing county and category name, replace with the word \"missing\" as the existing values are strings. This preserves any data in those rows that might be used.\nHowever, given that rows with missing data account for about half of one percent of the data, it is a big enough dataset that it would definitely be reasonable to drop these rows. This is what I did.\n\nB: Fix data in columns (State Bottle Cost, State Bottle Retail, Sale (Dollars)) that have $ symbols by removing the $ and then convert the remaining strings to floats.\n\nC: Add some additional columns with useful values such as the year pulled from the date column and the profit computed in its own column.")

#Here's all the data cleaning code (if I put it in earlier, then the chart above would just print out as zeros):

#drops NaN rows since such a tiny percentage of total data
df = df.dropna()

#cleans $ symbols from problem columns and turns into useable floats
df["State Bottle Cost"] = df["State Bottle Cost"].apply(lambda x: float(x.replace("$","")))
df["State Bottle Retail"] = df["State Bottle Retail"].apply(lambda x: float(x.replace("$","")))
df["Sale (Dollars)"] = df["Sale (Dollars)"].apply(lambda x: float(x.replace("$","")))

#adds "Year" column for questions 3 and 4
df["Year"] = df["Date"].str[6:10].astype(int)

print("\nProblem 3\n")
# Were all stores in the dataset open in 2015? If not, what steps do you think are appropriate to address that?
print("We know from the below accounting that a small number of stores were open in 2016 but not in 2015. Given that this number represents such a tiny percentage of total stores (there were %s stores in 2015 and %s in 2016), I think we can ignore this. We could also remove those rows." %(df.loc[(df["Year"] == 2015), "Store Number"].nunique(), df.loc[(df["Year"] == 2016), "Store Number"].nunique()))

#total number of unique stores in 2016 and 2015
df.loc[(df["Year"] == 2016), "Store Number"].nunique()
df.loc[(df["Year"] == 2015), "Store Number"].nunique()
#stores open in 2015 that were not open in 2016
only_2016 = set(df.loc[(df["Year"] == 2016), "Store Number"]) - set(df.loc[(df["Year"] == 2015), "Store Number"])
print(only_2016)
print("The above store numbers are the %s stores in 2016 that were not open in 2015." % len(only_2016))

print("\nProblem 4\n")
# What is the yearly liquor sales for each store in 2015? What is the profit for each store in 2015?
print("The yearly liquor sales for each store in 2015 can be calculated by totaling the number of bottles sold, the volume sold (gallons and liters), and the gross sales in dollars, depending on which particular type of total one is looking for. You can pull any individual store's total sales by using their store number. You can generate a pivot table for all of them such as (first 10 rows showing):\n")
print(pd.pivot_table(df,index=["Store Number"], values=["Sale (Dollars)", "Volume Sold (Liters)", "Volume Sold (Gallons)","Bottles Sold",], aggfunc=np.sum).head(10))

df["Profit"] = df["Sale (Dollars)"] - (df["Bottles Sold"] * df["State Bottle Cost"])
print("\nThe profit for each store can be calculated by subtracting the cost of the bottles sold from the total sales (I assigned this to a new column as it's a useful calculation). Then you can output a pivot table of all stores' profits per type of liquor totaled up like this (first 10 rows showing):\n")
print(pd.pivot_table(df,index=["Store Number"], values=["Profit"], aggfunc="sum").head(10))

print("\nProblem 5\n")
# Create a broader category for each liquor type (for example "100 Proof Vodka" and "Imported Vodka" both could fall under a "Vodka" category). How many different liquors went into each category? What categories had the highest number of bottles sold? What category has the highest profits?

#function that sorts into bigger parent categories
def categorizer(cat):
    if "VODKA" in cat:
        return "Vodka"
    elif "GINS" in cat:
        return "Gins"     
    elif "BRANDIES" in cat:
        return "Brandies"
    elif "RUM" in cat:
        return "Rum"
    elif "SCHNAPPS" in cat:
        return "Schnapps"
    elif ("BOURBON" in cat) or ("WHISK" in cat) or ("RYE" in cat) or ("SCOTCH" in cat):
        return "Whiskies Etc."
    elif "LIQUEUR" in cat:
        return "Liqueurs"
    elif "TEQUILA" in cat:
        return "Tequila"
    else:
        return "Misc."

#makes new column with category types
df["Category Type"] = df["Category Name"].astype(str).apply(categorizer)

print("We can see how many liquors (defined as individual items, not category names) went into each parent category by looking at the following pivot table.\n")
print(pd.pivot_table(df,index=["Category Type"],values=["Item Description"],aggfunc=lambda x: len(x.unique())))

print("\nTo find out the categories with the highest number of bottles sold, we can see from the following pivot table that Whiskies, Etc. had the highest number sold, followed closely by Vodka.\n")
print(pd.pivot_table(df,index=["Category Type"],values=["Bottles Sold"],aggfunc=np.sum))
print("\nThe highest profits (by far) were found in the Whiskies, Etc. category, which you can see in the following pivot table:\n")
print(np.round(pd.pivot_table(df,index=["Category Type"],values=["Profit"],aggfunc=np.sum)))

print("\nNote that this was just a rough categorization into parent categories and an alcohol lover might cringe at some of the things that ended up lumped together--for example, sloe gins are not gins! The categories are problematic however, as they are of wildly different sizes.")

print("\nProblem 6\n")
# Create a table that contains the following:
# Each broad category you created
# Each liquor that falls in that category
# The average, max, min, and total volume sold and the price per bottle sold

print("The following pivot table shows each parent category of liquor with each type of liquor in every category with the average, max, min, and total volume sold (liters) and the average price per bottle sold:\n")
print(pd.pivot_table(df,index=["Category Type", "Item Description"],values=["Volume Sold (Liters)", "State Bottle Retail"], aggfunc={"Volume Sold (Liters)":[np.mean, max, min, np.sum], 'State Bottle Retail':np.mean}))


print("\nProblem 7\n")
# Your employers are curious about county-by-county differences -- what is the most popular category of liquor in each category? Do all counties share the same tastes?

print("There are several ways to go about answering whether there are county-by-county differences in liquor consumption. In order to find the most popular category of liquor in each county, you can either make a pivot table or a groupby (see code below for both of these) that aggregates volume of liquor sold by category type and county (you could also make a case for doing this by total number of bottles sold). You can also use this piece of analysis to determine whether counties share the same tastes. I'm having a hard time figuring out how to sort just within those county-category type blocks, but if I could figure out how to do that, I could pull the top value (or top couple values) of each and make a separate dataframe to answer the question whether all counties share the same tastes. If you call sort_values in reverse order you can quickly see from the top results that liquor tastes do vary somewhat from county to county as a variety of types are represented. I could also figure out what the max value of each county-category type set was. But you can see the beginnings of this analysis here in the pivot table and groupby:\n")
print("Pivot table:", pd.pivot_table(df,index=["County", "Category Type"],values=["Volume Sold (Liters)"],aggfunc=np.sum))
print("\nGroupby:", df.groupby(["County", "Category Type"])["Volume Sold (Liters)"].sum())

print("\nProblem 8\n")
# Some counties have a very high population and some counties have a very low population. Assign county stores to being either large or small (I leave it up to you to determine what that cut-off is!) Do high population counties have a smaller or larger number of stores? Do high population counties purchase more bottles of liquor on average in a given order? Are there different tastes across high population and low population counties?
print("In the interest of time I'm going to have to just write what I'd do here. First, you need to consult a list that gives county population and decide where the cutoff is. Then you'd make a new column that added large and small as appropriate (using a function that did the assignments). There are 99 counties so perhaps there is some sort of merge that could make this easier. Then you could find the counts of unique stores in the group of high population counties, and then low population counties. Then you could compute the mean of bottle purchase for high vs low. Then you could repeat the task above re: category types by high vs low to see how they compare.")

print("\nProblem 9\n")
# Pick one of the questions asked above. How would you show your results visually?
print ("See the saved figure, liquor_profits.png, that this code generates for a visualization of a bar chart of the profits by parent liqueur category.")
profits = pd.DataFrame(pd.pivot_table(df,index=["Category Type"],values=["Profit"],aggfunc=np.sum))

ax = profits.plot(kind='bar', title ="Liquor Profits by Parent Category",figsize=(15,10),legend=True, fontsize=12)
ax.set_xlabel("Liquor",fontsize=12)
ax.set_ylabel("Profit",fontsize=12)

plt.savefig("liquor_profits.png")