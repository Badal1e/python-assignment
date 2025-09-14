import os
import pandas as pd

def convert_excel_to_csv(excel_file):
    if not os.path.exists(excel_file):
        print(f"Oops! The file '{excel_file}' was not found.")
        return

    folder_name = os.path.splitext(os.path.basename(excel_file))[0]

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    workbook = pd.ExcelFile(excel_file)

    for sheet in workbook.sheet_names:
        data = pd.read_excel(excel_file, sheet_name=sheet)
        csv_path = os.path.join(folder_name, f"{sheet}.csv")
        data.to_csv(csv_path, index=False)
        print(f"Sheet '{sheet}' converted to '{csv_path}'")

if __name__ == "__main__":
    excel_file = "Sample_sheet.xlsx"
    convert_excel_to_csv(excel_file)
