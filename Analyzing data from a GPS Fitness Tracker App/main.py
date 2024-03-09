# Description du projet tirée des instructions officielles :

# With the explosion in fitness tracker popularity, runners all of the world are collecting data with gadgets (smartphones, watches, etc.) to keep themselves motivated. They look for answers to questions like:

# How fast, long, and intense was my run today?
# Have I succeeded with my training goals?
# Am I progressing?
# What were my best achievements?
# How do I perform compared to others?

# The data is a CSV file where each row is a single training activity. In this project, you'll create import, clean, and analyze my data to answer the above questions. You can then apply the same strategy to your training data if you wish!

import pandas as pd
import matplotlib.pyplot as plt
import statsmodel.api as sm
%matplotlib inline

runkeeper_file = 'Datasets/cardioActivities.csv'
df_activities=pd.read_csv(runkeeper_file, parse_dates=True, index_col="Date")
cols_to_drop=['Friend\'s Tagged','Route Name', 'GPX File', 'Activity Id', 'Calories Burned', 'Notes']
df_activities.drop(cols_to_drop, axis=1, inplace=True)
display(df_activities['Type'].value_counts())
df_activities['Type'] = df_activities['Type'].str.replace('Other', 'Unicycling')
df_activities.isnull().sum()

plt.style.use('ggplot')
runs_subset_2013_2018 = df_activities.loc['20191231':'20130101']
runs_subset_2013_2018.plot(subplots=True,
                           sharex=False,
                           figsize=(12,16),
                           linestyle='none',
                           marker='o',
                           markersize=3)
plt.show()

runs_subset_2015_2018 = df_run.loc['20181231':'20150101']
print('How my average run looks in last 4 years:')
display(runs_subset_2015_2018.resample('A').mean())
print('Weekly averages of last 4 years:')
display(runs_subset_2015_2018.resample('W').mean().mean())
weekly_counts_average = runs_subset_2015_2018['Distance (km)'].resample('W').count().mean()
print('How many trainings per week I had on average:', weekly_counts_average)

runs_distance = runs_subset_2015_2018['Distance (km)']
runs_hr = runs_subset_2015_2018['Average Heart Rate (bpm)']
fig, (ax1, ax2) = plt.subplots(2, sharex=True, figsize=(12, 8))
runs_distance.plot(ax=ax1)
ax1.set(ylabel='Distance (km)', title='Historical data with averages')
ax1.axhline(runs_distance.mean(), color='blue', linewidth=1, linestyle='-.')
runs_hr.plot(ax=ax2, color='gray')
ax2.set(xlabel='Date', ylabel='Average Heart Rate (bpm)')
ax2.axhline(runs_hr.mean(), color='blue', linewidth=1, linestyle='-.')
plt.show()

df_run_dist_annual = df_run.sort_index()['20130101':'20181231']['Distance (km)'] \
                    .resample('A').sum()
fig = plt.figure(figsize=(8, 5))
ax = df_run_dist_annual.plot(marker='*', markersize=14, linewidth=0, 
                             color='blue')
ax.set(ylim=[0, 1210], 
       xlim=['2012','2019'],
       ylabel='Distance (km)',
       xlabel='Years',
       title='Annual totals for distance')
ax.axhspan(1000, 1210, color='green', alpha=0.4)
ax.axhspan(800, 1000, color='yellow', alpha=0.3)
ax.axhspan(0, 800, color='red', alpha=0.2)
plt.show()

df_run_dist_wkly = df_run.loc['20190101':'20130101']['Distance (km)'] \
                    .resample('W').bfill()
decomposed = sm.tsa.seasonal_decompose(df_run_dist_wkly, 
                                       extrapolate_trend=1, freq=52)
fig = plt.figure(figsize=(12, 5))
ax = decomposed.trend.plot(label='Trend', linewidth=2)
ax = decomposed.observed.plot(label='Observed', linewidth=0.5)
ax.legend()
ax.set_title('Running distance trend')
plt.show()

hr_zones = [100, 125, 133, 142, 151, 173]
zone_names = ['Easy', 'Moderate', 'Hard', 'Very hard', 'Maximal']
zone_colors = ['green', 'yellow', 'orange', 'tomato', 'red']
df_run_hr_all = df_run.loc['20190101':'20150301']['Average Heart Rate (bpm)']
fig, ax = plt.subplots(figsize=(8, 5))
n, bins, patches = ax.hist(df_run_hr_all, bins=hr_zones, alpha=0.5)
for i in range(0, len(patches)):
    patches[i].set_facecolor(zone_colors[i])
    ax.set(title='Distribution of HR', ylabel='Number of runs')
ax.xaxis.set(ticks=hr_zones)
ax.set_xticklabels(labels=zone_names, rotation=-30, ha='left')
plt.show()

df_run_walk_cycle = df_run.append([df_walk, df_cycle]).sort_index(ascending=False)
dist_climb_cols, speed_col = ['Distance (km)', 'Climb (m)'], ['Average Speed (km/h)']
df_totals = df_run_walk_cycle.groupby('Type')[dist_climb_cols].sum()
print('Totals for different training types:')
display(df_totals)
df_summary = df_run_walk_cycle.groupby('Type')[dist_climb_cols + speed_col].describe()
for i in dist_climb_cols:
    df_summary[i, 'total'] = df_totals[i]
    print('Summary statistics for different training types:')
df_summary.stack()