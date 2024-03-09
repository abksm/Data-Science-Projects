import pandas  as pd
df = pd.read_csv('dob_job_application_filings_subset.csv')

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df_subset.head())
print(df_subset.tail())
print(df.info())
print(df_subset.info())
print(df['Borough'].value_counts(dropna=False))
print(df['State'].value_counts(dropna=False))
print(df['Site Fill'].value_counts(dropna=False))

import matplotlib.pyplot as plt

df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

plt.show()



import pandas as pd
import matplotlib.pyplot as plt


df.boxplot(column='initial_cost', by='Borough', rot=90)


plt.show()



import pandas as pd
import matplotlib.pyplot as plt


df.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()


df_subset .plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()


print(airquality.head())


airquality_melt = pd.melt(airquality, id_vars=['Month', 'Day'])


print(airquality_melt.head())



print(airquality.head())


airquality_melt = pd.melt(airquality, id_vars=['Month', 'Day'], ar_name='measurement', value_name='reading')


print(airquality_melt.head())







print(airquality_pivot.index)


airquality_pivot = airquality_pivot.reset_index()


print(airquality_pivot.index)


print(airquality_pivot.head())




airquality_pivot = airquality_dup.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading', aggfunc=np.mean)


airquality_pivot = airquality_pivot.reset_index()


print(airquality_pivot.head())


print(airquality.head())



tb_melt = pd.melt(tb, id_vars=['country', 'year'])


tb_melt['gender'] = tb_melt.variable.str[0]


tb_melt['age_group'] = tb_melt.variable.str[1:]


print(tb_melt.head())



ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')


ebola_melt['str_split'] = ebola_melt.type_country.str.split('_')


ebola_melt['type'] = ebola_melt.str_split.str.get(0)


ebola_melt['country'] = ebola_melt.str_split.str.get(1)


print(ebola_melt.head())



print(categories)


print('Cleanliness: ', airlines['cleanliness'].unique(), "\n")
print('Safety: ', airlines['safety'].unique(), "\n")
print('Satisfaction: ', airlines['satisfaction'].unique(), "\n")


cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])


cat_clean_rows = airlines['cleanliness'].isin(cat_clean)


print(airlines[cat_clean_rows])


print(airlines[~cat_clean_rows])


 

print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())


print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())


airlines['dest_region'] = airlines['dest_region'].str.lower()
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})


airlines['dest_size'] = airlines['dest_size'].str.strip()


print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())




label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']


airlines['wait_type'] = pd.cut(airlines['wait_min'], bins = label_ranges, 
                                labels = label_names)


mappings = {'Monday':'weekday', 'Tuesday':'weekday', 'Wednesday': 'weekday', 
            'Thursday': 'weekday', 'Friday': 'weekday', 
            'Saturday': 'weekend', 'Sunday': 'weekend'}

airlines['day_week'] = airlines['day'].replace(mappings)




airlines['full_name'] = airlines['full_name'].str.replace("Dr.","")


airlines['full_name'] =airlines['full_name'].str.replace("Mr.","")


airlines['full_name'] =airlines['full_name'].str.replace("Miss","")


airlines['full_name'] =airlines['full_name'].str.replace("Ms.","")


assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False



resp_length = airlines['survey_response'].str.len()


airlines_survey = airlines[resp_length > 40]


assert airlines_survey['survey_response'].str.len().min() > 40


print(airlines_survey['survey_response'])




row_concat = pd.concat([uber1, uber2,uber3])


print(row_concat.shape)


print(row_concat.head())



ebola_tidy = pd.concat([ebola_melt,status_country],axis=1)


print(ebola_tidy.shape)


print(ebola_tidy.head())



import glob
import pandas as pd


pattern = '*.csv'


csv_files = glob.glob(pattern)


print(csv_files)


csv2 = pd.read_csv(csv_files[1])


print(csv2.head())



frames = []


for csv in csv_files:

    
    df = pd.read_csv(csv)
    
    
    frames.append(df)


uber = pd.concat(frames)


print(uber.shape)


print(uber.head())




o2o = pd.merge(left=site, right=visited , left_on='name', right_on='site' )


print(o2o)



m2o = pd.merge(left=site, right=visited , left_on='name', right_on='site')



print(m2o)



m2m = pd.merge(left=site, right=visited, left_on='name', right_on='site')


m2m = pd.merge(left=m2m, right=survey, left_on='ident', right_on='taken')


print(m2m.head(20))





acct_eu = banking['acct_cur'] == 'euro'


banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1 


banking.loc[acct_eu, 'acct_cur'] = 'dollar'


assert banking['acct_cur'].unique() == 'dollar'




print(banking['account_opened'].head())


banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           
                                           infer_datetime_format = True,
                                           
                                           errors = 'coerce') 


banking['acct_year'] = banking['account_opened'].dt.strftime('%Y')


print(banking['acct_year'])




fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']


inv_equ = banking[fund_columns].sum(axis = 1) == banking['inv_amount']


consistent_inv = banking[inv_equ]
inconsistent_inv = banking[~inv_equ]


print("Number of inconsistent investments: ", inconsistent_inv.shape[0])




print(banking.isna().sum())


msno.matrix(banking)
plt.show()


missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]


banking_sorted = banking.sort_values(by='age')
msno.matrix(banking_sorted)
plt.show()




banking_fullid = banking.dropna(subset = ['cust_id'])


acct_imp =  banking_fullid['inv_amount'] * 5 


banking_imputed = banking_fullid.fillna({'acct_amount':acct_imp})


print(banking_imputed.isna().sum())





tips.sex = tips.sex.astype('category')


tips.smoker = tips.smoker.astype('category')


print(tips.info())



tips['total_bill'] = pd.to_numeric(tips['total_bill'], errors='coerce')


tips['tip'] = pd.to_numeric(tips['tip'], errors='coerce')


print(tips.info())



import re


prog = re.compile('\d{3}-\d{3}-\d{4}')


result = prog.match('123-456-7890')
print(bool(result))


result = prog.match('1123-456-7890')
print(bool(result))



import re


matches = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')


print(matches)



pattern1 = bool(re.match(pattern='\d{3}-\d{3}-\d{4}', string='123-456-7890'))
print(pattern1)


pattern2 = bool(re.match(pattern='\$\d*\.\d{2}', string='$123.45'))
print(pattern2)


pattern3 = bool(re.match(pattern='[A-Z]\w*', string='Australia'))
print(pattern3)




def recode_sex(sex_value):

    
    if sex_value == 'Male':
        return 1
    
    
    elif sex_value == 'Female':
        return 0
    
    
    else:
        return np.nan 


tips['sex_recode'] = tips.sex.apply(recode_sex)


print(tips.head())




tips['total_dollar_replace'] = tips.total_dollar.apply(lambda x: x.replace('$', ''))


tips['total_dollar_re'] = tips.total_dollar.apply(lambda x: re.findall('\d+\.\d+', x)[0])


print(tips.head())



tracks = billboard[['year','artist', 'track', 'time']]


print(tracks.info())


tracks_no_duplicates = tracks.drop_duplicates()


print(tracks_no_duplicates.info())



oz_mean = airquality.Ozone.mean()


airquality['Ozone'] = airquality.Ozone.fillna(oz_mean)


print(airquality.info())




assert pd.notnull(ebola).all().all()


assert (ebola >= 0).all().all()




import matplotlib.pyplot as plt


g1800s.plot(kind='scatter', x='1800', y='1899')


plt.xlabel('Life Expectancy in 1800')
plt.ylabel('Life Expectancy in 1899')


plt.xlim(20, 55)
plt.ylim(20, 55)


plt.show()


def check_null_or_valid(row_data):
    """Function that takes a row of data,
    drops all missing values,
    and checks if all remaining values are greater than or equal to 0
    """
    no_na = row_data.dropna()[1:-1]
    numeric = pd.to_numeric(no_na)
    ge0 = numeric >= 0
    return ge0


assert  g1800s.columns[0] == 'Life expectancy'


assert g1800s.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()


assert g1800s['Life expectancy'].value_counts()[0] == 1



gapminder = pd.concat([g1800s, g1900s,g2000s])


print(gapminder.shape)


print(gapminder.head())



gapminder_melt = pd.melt(gapminder, id_vars='Life expectancy')


gapminder_melt.columns = ['country', 'year', 'life_expectancy']


print(gapminder_melt.head())




gapminder.year = pd.to_numeric(gapminder['year'])


assert gapminder.country.dtypes == np.object


assert gapminder.year.dtypes == np.int64


assert gapminder.life_expectancy.dtypes == np.float64



countries = gapminder['country']


countries = countries.drop_duplicates()


pattern = '^[A-Za-z\.\s]*$'


mask = countries.str.contains(pattern)


mask_inverse = ~mask


invalid_countries = countries.loc[mask_inverse]


print(invalid_countries)



assert pd.notnull(gapminder.country).all()


assert pd.notnull(gapminder.year).all()


gapminder = gapminder.dropna(how='any')


print(gapminder.shape)




plt.subplot(2, 1, 1) 


gapminder['life_expectancy'].plot(kind='hist')


gapminder_agg = gapminder.groupby('year')['life_expectancy'].mean()


print(gapminder_agg.head())


print(gapminder_agg.tail())


plt.subplot(2, 1, 2)


gapminder.life_expectancy.plot(kind='hist')
gapminder_agg.plot()


plt.title('Life expectancy over the years')
plt.ylabel('Life expectancy')
plt.xlabel('Year')


plt.tight_layout()
plt.show()


gapminder.to_csv('gapminder.csv' )
gapminder_agg.to_csv('gapminder_agg.csv') 