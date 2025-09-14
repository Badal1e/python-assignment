import pandas as pd
import pycountry_convert as pc

data = pd.read_csv(r'C:\Users\Admin\Desktop\python-assignmentt\ETL Job\survey_results_public.csv')
hobby_data = data[['Hobbyist', 'Gender', 'Country']].dropna()

def categorize_gender(gender):
    gender = str(gender).strip().upper()
    if gender in ['MAN', 'MALE']:
        return 'MAN'
    elif gender in ['WOMAN', 'FEMALE']:
        return 'WOMAN'
    else:
        return 'OTHERS'

hobby_data['Gender'] = hobby_data['Gender'].apply(categorize_gender)

def country_to_continent(country_name):
    try:
        code = pc.country_name_to_country_alpha2(country_name)
        continent = pc.country_alpha2_to_continent_code(code)
        return pc.convert_continent_code_to_continent_name(continent)
    except:
        return None

hobby_data['Continent'] = hobby_data['Country'].apply(country_to_continent)
hobby_data = hobby_data.dropna(subset=['Continent'])
hobby_data = hobby_data[hobby_data['Hobbyist'].str.upper() == 'YES']
hobby_counts = hobby_data.groupby(['Continent', 'Gender']).size().unstack(fill_value=0)
print("✅ Number of hobbyist developers by continent and gender:")
print(hobby_counts)
