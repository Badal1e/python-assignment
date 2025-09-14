import pandas as pd

data = pd.read_csv(r'C:\Users\Admin\Desktop\python-assignmentt\ETL Job\survey_results_public.csv')

if 'Age1stCode' not in data.columns:
    raise ValueError("Age1stCode column not found in dataset!")

data['Age1stCodeNum'] = pd.to_numeric(data['Age1stCode'], errors='coerce')
clean_data = data.dropna(subset=['Age1stCodeNum'])
average_age = clean_data['Age1stCodeNum'].mean()
print(f"✅ Average age of developers when they wrote their first line of code: {average_age:.2f}")
