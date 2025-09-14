import pandas as pd
import pycountry_convert as pc

data = pd.read_csv(r'C:\Users\Admin\Desktop\python-assignmentt\ETL Job\survey_results_public.csv')
satisfaction_data = data[['JobSat', 'CareerSat', 'Gender', 'Country']].dropna(subset=['Gender', 'Country'])

def categorize_gender(gender):
    gender = str(gender).strip().upper()
    if gender in ['MAN', 'MALE']:
        return 'MAN'
    elif gender in ['WOMAN', 'FEMALE']:
        return 'WOMAN'
    else:
        return 'OTHERS'

satisfaction_data['Gender'] = satisfaction_data['Gender'].apply(categorize_gender)

def country_to_continent(country_name):
    try:
        code = pc.country_name_to_country_alpha2(country_name)
        continent = pc.country_alpha2_to_continent_code(code)
        return pc.convert_continent_code_to_continent_name(continent)
    except:
        return None

satisfaction_data['Continent'] = satisfaction_data['Country'].apply(country_to_continent)
satisfaction_data = satisfaction_data.dropna(subset=['Continent'])

job_report = satisfaction_data.groupby(['Continent', 'Gender'])['JobSat'].value_counts(normalize=True).unstack(fill_value=0) * 100
print("✅ Job Satisfaction Report (by Continent & Gender)")
print(job_report.round(2))

career_report = satisfaction_data.groupby(['Continent', 'Gender'])['CareerSat'].value_counts(normalize=True).unstack(fill_value=0) * 100
print("\n✅ Career Satisfaction Report (by Continent & Gender)")
print(career_report.round(2))
