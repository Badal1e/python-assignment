import pandas as pd

data = pd.read_csv(r'C:\Users\Admin\Desktop\python-assignmentt\ETL Job\survey_results_public.csv')
desired_lang = data['LanguageDesireNextYear'].dropna()
all_languages = desired_lang.str.split(';').explode()
language_counts = all_languages.value_counts()
top_language = language_counts.idxmax()
top_count = language_counts.max()
print(f"✅ The most desired programming language for 2020 is {top_language} with {top_count} developers wanting to learn it.")
