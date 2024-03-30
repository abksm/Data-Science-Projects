import pandas as pd
words=['buy', 'discount', 'promotion', 'cheap', 'offer', 'purchase', 'sale']
products=['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']
keywords=[]
for product in products:
    for word in words:
        keywords.append([product, product+' '+word])
        keywords.append([product, word+' '+product])

keywords_df=pd.DataFrame(keywords, columns=['product', 'keyword'])
keywords_df.columns = ['Ad Group', 'Keyword']
keywords_df['Campaign'] = 'AdSofas'
keywords_df['Criterion Type'] = 'Exact'

keywords_phrase = keywords_df.copy()
keywords_phrase['Criterion Type'] = 'Phrase'
keywords_df_final = pd.concat([keywords_df, keywords_phrase])

keywords_df_final.to_csv('keywords.csv', index=False)
summary = keywords_df_final.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()