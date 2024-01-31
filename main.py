import pandas as pd

def excel_to_csv(input_file, output_path):
  read_file = pd.read_excel (r'input_file')
  transformed_file = read_file.to_csv (r'{output_path}\transformed_file.csv', index = None, header=True)

excel_to_csv("INPUT FILE NAME HERE", "OUTPUT PATH HERE")