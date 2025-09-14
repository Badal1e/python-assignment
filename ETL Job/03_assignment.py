import pandas as pd
import pycountry_convert as pc

data = pd.read_csv(r'C:\Users\Admin\Desktop\python-assignmentt\ETL Job\survey_results_public.csv')
salary_data = data[['Country', 'ConvertedComp']].dropna(subset=['ConvertedComp'])

def country_to_continent(country_name):
    try:
        country_code = pc.country_name_to_country_alpha2(country_name)
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        return pc.convert_continent_code_to_continent_name(continent_code)
    except:
        return None

salary_data['Continent'] = salary_data['Country'].apply(country_to_continent)
salary_data = salary_data.dropna(subset=['Continent'])
avg_salary = salary_data.groupby('Continent')['ConvertedComp'].mean().sort_values(ascending=False)
print("✅ Average developer salary by continent (descending order):")
print(avg_salary)
