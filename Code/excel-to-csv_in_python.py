import pandas as pd

def excel_to_csv(input_path, output_path):
  read_file = pd.read_excel(input_path)
  
  transformed_file = read_file.to_csv (fr'{output_path}\transformed_file.csv',
                                       index= None,
                                       header= True)

excel_to_csv(r"<INPUT PATH>",
             r"<OUTPUT PATH>")