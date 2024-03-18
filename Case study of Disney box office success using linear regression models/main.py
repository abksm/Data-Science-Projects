# Description du projet tirée des instructions officielles : 

# Since the 1930s, Walt Disney Studios has released more than 600 films covering a wide range of genres. While some movies are indeed directed towards kids, many are intended for a broad audience. 
# In this project, you will analyze data to see how Disney movies have changed in popularity since its first movie release. You will also perform hypothesis testing to see what aspects of a movie contribute to its success. 
# This project assumes that you can manipulate data using pandas and can make basic plots using Seaborn. You should also be familiar with statistical inference and be able to perform two-sample bootstrap hypothesis tests for difference of means. 
# The dataset used in this project is a modified version of the Disney Character Success dataset from Kelly Garrett.

import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

gross = pd.read_csv("Datasets/disney_movies_total_gross.csv",
                    parse_dates=['release_date'])
inflation_adjusted_gross_desc=gross.sort_values(by='inflation_adjusted_gross',
                                                ascending=False)
print("The top 10 movies by box office earnings are :")
inflation_adjusted_gross_desc.head(10)

gross['release_year'] = pd.DatetimeIndex(gross["release_date"]).year
gross2=gross[['genre','release_year','total_gross','inflation_adjusted_gross']]
group = gross2.groupby(['genre','release_year']).mean()
genre_yearly = group.reset_index()
display(genre_yearly.head(10))

plot = sns.relplot(x='release_year', y='inflation_adjusted_gross', kind='line', hue='genre', data=genre_yearly)
plot.fig.suptitle('Genre Popularity Trend')

genre_dummies=pd.get_dummies(data=gross['genre'], drop_first=True).astype(int);
genre_dummies.head()

regr=LinearRegression()
regr.fit(genre_dummies, gross["inflation_adjusted_gross"])
action=regr.intercept_
adventure=regr.coef_[[0]][0]
print("The estimated intercept and coefficient values are : \n",(action,adventure))

inds=np.arange(len(gross['genre']))
size=500
bs_action_reps=np.empty(size)
bs_adventure_reps=np.empty(size)
for i in range(size) :
    bs_inds=np.random.choice(inds, size=len(inds))
    bs_genre=gross['genre'][bs_inds]
    bs_gross=gross['inflation_adjusted_gross'][bs_inds]
    bs_dummies=pd.get_dummies(data=gross['genre'], drop_first=True)
    regr=LinearRegression().fit(bs_dummies, bs_gross)
    bs_action_reps[i]=regr.intercept_
    bs_adventure_reps[i]=regr.coef_[[0]][0]

confidence_interval_action=np.percentile(bs_action_reps, [2.5, 97.5])
confidence_interval_adventure=np.percentile(bs_adventure_reps, [2.5, 97.5])
print("The confidence interval for the intercept is : \n",confidence_interval_action)
print("The confidence interval for the coefficient is : \n",confidence_interval_adventure)

# Should Disney studios make more action and adventure movies ?
more_action_adventure_movies=True