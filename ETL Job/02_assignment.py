import pandas as pd

data = pd.read_csv(r'C:\Users\Admin\Desktop\python-assignmentt\ETL Job\survey_results_public.csv')
relevant_data = data[['Country', 'LanguageWorkedWith']].dropna()
relevant_data['KnowsPython'] = relevant_data['LanguageWorkedWith'].str.contains('Python', case=False, na=False)
country_python_pct = relevant_data.groupby('Country')['KnowsPython'].mean() * 100
country_python_pct = country_python_pct.sort_values(ascending=False)
print("✅ Percentage of developers knowing Python by country (top 20):")
print(country_python_pct.head(20))
