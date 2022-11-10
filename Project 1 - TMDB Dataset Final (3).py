#!/usr/bin/env python
# coding: utf-8

# # Project: Investigate a Dataset - TMDb movie data Analysis
# 
# ## Introduction
# 
# ### Dataset Description
# 
# This data set contains information about 10,000 movies collected from The Movie Database (TMDb), including user ratings and revenue.
# 
# Certain columns, like ‘cast’ and ‘genres’, contain multiple values separated by pipe (|) characters.
# 
# There are some odd characters in the ‘cast’ column. Don’t worry about cleaning them. You can leave them as is.
# 
# The final two columns ending with “_adj” show the budget and revenue of the associated movie in terms of 2010 dollars, accounting for inflation over time.
# 
# All the columns in the data set and their respective significance: id - movies unique identifiers, imdb_id, popularity-how much the movie is known, budget-allocated cost of casting the movie, revenue - income received form movies, original_title - the title the movie was first released and known by , cast-team involved in the production, homepage-a link to where the movie is, director-the leader of the cast, tagline-a movies key phrase, keywords-what the movie is most likely going to be searched by, overview-a quick storyline of the movie, runtime-how long the movie shows, genres-the respective movie categories, production_companies-the company resposible for the movie, release_date-the date the movie was deployed to the public, vote_count-how many people have voted for a movie, vote_average-the average rating from the votes, release_year-the year the movie was released to the public, budget_adj-adjusted budget as at 2010 factoring in inflation, revenue_adj - adjusted revenue as at 20210 factoring in inflation
# 
# 
# ## Question(s) for Analysis
# 
# This analysis will particularly address the question(s).
# 
# - Which year has the highest average rating?
# - Which year had the highest average revenue?
# - Who are the directors of the top ten most popular movies??
# - Which year had the highest average popularity?
# - What kinds of properties are associated with movies that have high revenues?
#   - Do movies with higher popularity receive better ratings?
#   - Do movies with higher popularity bring in higher revenue?
#   - Do movies with a higher runtime bring in more revenue?
#   - Do movies with a higher budget bring in more revenue?
# - Which year was the highest number of movies produced?
# - The highest number of genres produced in the period of the data set and the specific type
# 

# In[104]:


# Import statements for all of the packages intended for use.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Data Wrangling

# ### Data wrangling and cleaning steps
# 
# 1. Loading the csv data
# 2. Checking the first and last five row of the data to ensure it loaded properly
# 3. Checking the shape of the data in terms of the number of rows and columns
# 4. Checking the overall statistics of the numerical columns in entire data set to help quickly assess variables with missing data using describe
# 5. - Through general information, check for missing values, to ensure alignment with what the summary data suggested.
#    - This general information about data set also informs us about; data types, no. of columns, rows and memory size
# 6. checking for the number of missing values in the dataset per column to determine the impact of missing values on your analysis and the decision as regards to handling missing data
# 7. Visualizing the missing data through a heatmap to get a visual outlook in comparison to the data from previous code
# 8. Checking for duplicates and the duplicates total to determine how to handle the duplicates thereafter based on the nature of the data set
# 9. Deleting the duplicates
# 10. Confimring the duplicates deletion success by checking the shape of the data again, that is, the number of rows and columns
# 11. Checking the number of uniques data in the data set per variable

# #### By displaying the data in the tom five rows the table below helps us see how our data was loaded from CSV and the status it is in at the tom. You can extract information such as the first row in our data and how many columns are populated. We can then conclude that our data has uploaded successfully.

# In[105]:


# Loading csv data
df=pd.read_csv('tmdb-movies.csv')
df.head()


# #### By displaying the data in the bottom five rows the table below helps us see how our data was loaded from CSV and the status it is in at the bottom. You can extract information such as the last row in our data and how many columns are populated. We can then conclude that our data has uploaded successfully.

# In[106]:


# a view of the last five rows of the data set
df.tail()


# ### Data Cleaning

# In[107]:


# number of rows and columns in the data set
print(df.shape)


# In[108]:


#Output of all columns
df.columns


# #### The table below gives the overall statistics of the numerical columns in entire data set which help quickly assess variables with missing data and different aspects of our data set. For instance, from here we can conclude that we have a total of 10866 rows in our data set.####

# In[109]:


#Summary statistics. Overall statistics of the numerical columns in entire data set will help quickly assess variables with missing data
df.describe()


# In[110]:


#Checking for missing values, should align with what the summary data suggested
#General information about data set; data types, no. of columns, rows and others as below
df.info()


# In[111]:


# checking for the number of missing values in the dataset per column
df.isnull().sum()


# In[112]:


#checking for duplicate values
df.duplicated().sum()


# In[113]:


#Output all rows that are duplicates
df[df.duplicated()]


# In[114]:


#removing duplicate values from our data set
df.drop_duplicates(inplace=True)


# In[115]:


#validating the removal of duplicate values
print(df.shape)


# In[116]:


#Unique values
df.nunique()


# ## Exploratory Data Analysis

# ### Which year has the highest average rating?

# In[117]:


#For ease of reference of columns
df.columns


# In[118]:


df.groupby('release_year')['vote_average'].mean().sort_values(ascending=False)


# #### Below is a visualization of the highest average rating by year, where can extract the average rating of all respective years. We can then conclude that the year with the highest average rating is the year 1973.

# In[119]:


#visualization of the highest average rating by year
sns.set(rc={'figure.figsize':(15,8)})
sns.barplot(x='release_year',y='vote_average',data=df)
locs,labels=plt.xticks()
plt.setp(labels,rotation=90)
plt.title("Average Rating By Year")
plt.show()


# In[120]:


# a function that calls the top average rating
def top_rating():
    print("6.703636, ","1973")


# In[121]:


# a function that calls the lowest average rating
def low_rating():
    print("5.799830, ","2012")


# ### Which year has the highest average revenue?

# In[122]:


df.groupby('release_year')['revenue_adj'].mean().sort_values(ascending=False)


# #### The following is a visualization of the average highest revenue by year, where can extract the average revenue of all respective years. We can then conclude that the year with the highest average revenue is the year 1977.

# In[123]:


#visualization of the highest average revenue by year
sns.set(rc={'figure.figsize':(15,8)})
sns.barplot(x='release_year',y='revenue_adj',data=df)
locs,labels=plt.xticks()
plt.setp(labels,rotation=90)
plt.title("Average Revenue By Year")
plt.show()


# In[124]:


# a function that calls the top average revenue
def top_revenue():
    print("1.376362e+08, ","1977")


# In[125]:


# a function that calls the lowest average revenue
def low_revenue():
    print("1.237527e+07, ","1966")


# ### Who are the directors of the top ten most popular movies?

# In[126]:


df.columns


# #### The table below shows the top ten movies through all the years in the data set by popularity. We can extract other information related to the top ten popular movies such as genre, release year, director, budget and revenue. From here we can conclude that the most popular movie through all the years is Jurassic World.

# In[127]:


#top ten popular genres and their respective variables as following
top10_popular=df.nlargest(10,'popularity')[['popularity','original_title','release_year','genres','director','budget_adj','revenue_adj']]


# In[128]:


top10_popular


# In[129]:


#visualization of the top 10 popular movies by revenue
sns.set(rc={'figure.figsize':(15,8)})
sns.barplot(x='popularity',y='revenue_adj',data=top10_popular)
locs,labels=plt.xticks()
plt.setp(labels,rotation=90)
plt.title("Average Revenue By Popularity")
plt.show()


# #### Here is a visualization of the budget versus the popularity of the top ten popular movies, where can extract the average budget in comparison to popularity for the top ten movies. We can then conclude that the higher the budget is not necessarity the higher the popularity.

# In[130]:


#visualization of the top 10 popular movies by budget
sns.set(rc={'figure.figsize':(15,8)})
sns.barplot(x='popularity',y='budget_adj',data=top10_popular)
locs,labels=plt.xticks()
plt.setp(labels,rotation=90)
plt.title("Average Revenue By Budget")
plt.show()


# #### Below is visualization of the spread of the top ten movies across the years represented in the data set. We can extract the exact years in which the top ten movies were produced and at what rate of popularity per year. We can conclude that the most popular movies in the top ten list were produced in the year 2015.

# In[131]:


#visualization of the top 10 popular movies by year
sns.set(rc={'figure.figsize':(15,8)})
sns.barplot(x='release_year',y='popularity',data=top10_popular)
locs,labels=plt.xticks()
plt.setp(labels,rotation=90)
plt.title("Average Revenue By Popularity")
plt.show()


# ### Which year has the highest average popularity?

# In[132]:


df.groupby('release_year')['popularity'].mean().sort_values(ascending=False)


# In[133]:


#visualization of the highest average popularity by year
sns.set(rc={'figure.figsize':(15,8)})
sns.barplot(x='release_year',y='popularity',data=df)
locs,labels=plt.xticks()
plt.setp(labels,rotation=90)
plt.title("Popularity By Year")
plt.show()


# #### Above is a visualization of the spread movies popularity across the years represented in the data set. We can extract the trend of movies popularity across the years. We conclude that the most popular movies were produced in the year 2015.¶

# In[134]:


# a function that calls the highest average popularity
def top_popularity():
    print("1.030657, ","2015")


# In[153]:


# a function that calls the lowest average popularity
def low_popularity():
    print("0.304112, ","1966")


# ### Do movies with higher popularity receive better ratings?

# In[136]:


# get the median amount of popularity
df.popularity.median()


# In[137]:


# select samples with popularity less than the median
low_popularity = df.query('popularity < 0.383831')

# select samples with popularity greater than or equal to the median
high_popularity = df.query('popularity >= 0.383831')

# ensure these queries included each sample exactly once
num_samples = df.shape[0]
num_samples == low_popularity['vote_average'].count() + high_popularity['vote_average'].count() # should be True


# In[138]:


# get mean rating for the low popularity and high popularity groups
low_popularity.vote_average.mean(), high_popularity.vote_average.mean()


# ### Do movies with higher popularity bring in higher revenue?

# In[139]:


# ensure these queries included each sample exactly once
num_samples = df.shape[0]
num_samples == low_popularity['revenue_adj'].count() + high_popularity['revenue_adj'].count() # should be True


# In[140]:


# get mean revenue for the low popularity and high popularity groups
low_popularity.revenue_adj.mean(), high_popularity.revenue_adj.mean()


# ### Do movies with a higher runtime bring in more revenue?

# In[141]:


# get the median amount of runtime
df.runtime.median()


# In[142]:


# select samples with runtime less than the median
low_runtime = df.query('runtime < 99.0')

# select samples with popularity greater than or equal to the median
high_runtime = df.query('runtime >= 99.0')

# ensure these queries included each sample exactly once
num_samples = df.shape[0]
num_samples == low_runtime['revenue_adj'].count() + high_runtime['revenue_adj'].count() # should be True


# In[143]:


# get mean revenue for the low runtime and high runtime groups
low_runtime.revenue_adj.mean(), high_runtime.revenue_adj.mean()


# ### Do movies with a higher budget bring in more revenue?

# In[144]:


# get the median amount of budget
df.budget_adj.mean()


# In[145]:


# select samples with budget less than the mean
low_budget_adj = df.query('budget_adj < 17549894.037320614')

# select samples with popularity greater than or equal to the median
high_budget_adj = df.query('budget_adj >= 17549894.037320614')

# ensure these queries included each sample exactly once
num_samples = df.shape[0]
num_samples == low_budget_adj['revenue_adj'].count() + high_budget_adj['revenue_adj'].count() # should be True


# In[146]:


# get mean revenue for the low budget and high budget groups
low_budget_adj.revenue_adj.mean(), high_budget_adj.revenue_adj.mean()


# ### Which year was the highest number of movies produced?

# In[147]:


df['release_year'].value_counts()


# #### Below is visualization of the count of movies produced across the years represented in the data set. From here we can extract the number of movies produced per year. We can conclude that most movies were produced in the year 2014.¶

# In[148]:


sns.set(rc={'figure.figsize':(15,8)})
sns.countplot(x='release_year', data=df)
locs,labels=plt.xticks()
plt.setp(labels,rotation=90)
plt.title("Movie Count per Year")
plt.show()


# ### The highest number of genres produced in the period of the data set and the specific type

# In[149]:


df['genres'].value_counts()


# #### Below is visualization of the count of genres produced across the years represented in the data set. From here we can extract the number of genres produced per year. We can conclude that most genres were produced in the year 2014.¶

# In[150]:


sns.set(rc={'figure.figsize':(15,8)})
sns.countplot(x='release_year', data=df)
locs,labels=plt.xticks()
plt.setp(labels,rotation=90)
plt.title("Genre Count per Year")
plt.show()


# #### From the following functions we can tell the year with the top average revenue is not necessarily the same year with the top average rating nor the top popularity. The same can be concluded for the lowest of these average figures.
# 
# #### These functions make the analysis user friendly as it is easy to refer to these figures without necessarily scrolling through the codes.

# In[151]:


top_revenue()
top_rating()
top_popularity()


# In[154]:


low_revenue()
low_rating()
low_popularity()


# ## Conclusions

# ### Summary findings and results
# 
# **Which year has the highest average rating?** The highest average rating is in the year 1973 at 6.7.
# 
# **Which year had the highest average revenue?** The highest average revenue is in the year 1977 at 1.4 Billion.
# 
# **Who are the directors of the top ten most popular movies??** Colin Trevorrow, George Miller, Christopher Nolan, James Gunn, Robert Schwentke, Joe Russo and Anthony Russo, George Lucas, Chad Stahelski and David Leitch, J.J. Abrams and finally Francis Lawrence.
# 
# 
# **Which year had the highest average popularity?** The year with the average popularity is 2015 at 1.03.
# 
# **Do movies with higher popularity receive better ratings?** The analysis shows that movies with a higher popularity have a higher rating, which is a positive correlation between the two variables. This is arrived at from categorizing popularity into three groups; low popularity, median popularity and high popularity. The average ratings of high popularity turns out to be higher than that of low popularity.
# 
# **Do movies with higher popularity bring in higher revenue?** The analysis reflects a positive correlation between movies with a higher popularity and revenue. This is arrived at from categorizing popularity into three groups; low popularity, median popularity and high popularity. The average revenue of high popularity turns out to be higher than that of low popularity.
# 
# 
# **Do movies with a higher runtime bring in more revenue?** The analysis confirms that movies with a higher runtime are positively correlated with a higher revenue. This is arrived at from categorizing runtime into three groups; low runtimet, median runtime and high runtime. The average revenue of high runtime turns out to be higher than that of low runtime.
# 
# 
# **Do movies with a higher budget bring in more revenue?** The analysis confirms that movies with a higher budget are positively correlated with revenue. This is arrived at from categorizing budget into three groups; low budget, mean budget and high budget. The average revenue of high budget turns out to be higher than that of low budget.
# 
# **Which year was the highest number of movies produced?** The highest number of movies were produced in the year 2014 at 700 movies
# 
# **The highest number of genres produced in the period of the data set and the specific type.** The genres most produced are Comedy and Drama movies at 712 counts each over the data set period of 56 years 
# 
# In conclusion, additional research can be done to analyze the power of competition with regards to subtitute movies in similary genre in correlarion to revenue. As well as the total number of movies produced in a year in correlation to revenue.
# 
# ### Limitations
# 
# One key limitation of this research is that the mean or median computations computed in say the average revenue, average rating, average popularity may be a bit skewed to the right or to the left depending on which side has the highest number of zero figures.
