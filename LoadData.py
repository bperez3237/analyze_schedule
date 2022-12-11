import pandas as pd

def filter_cost_code(dataframe, cost_code):
    return dataframe[dataframe['Cost Code'] == cost_code]

def remove_columns(dataframe, columns):
    return dataframe.drop(columns, axis=1)

schedule_path = f'C:/Users/bperez/Iovino Enterprises, LLC/M007-NYCHA-Coney Island Sites - Documents/General/27 - PERSONAL FOLDERS/Brian Perez/Coney Island/02 - M007 Cost/Cost Report/Cost Report 11 - 2022/November 2022 Schedule - Data.xlsx'
scheudle_df = pd.read_excel(schedule_path, sheet_name='Activities')
schedule_df = remove_columns(scheudle_df, ['WBS Code', 'ID1', 'ID2', 'ID3', 'ID4', '(*)WBS Name','(*)WBS Path'])

cost_rprt_path = f'C:/Users/bperez/Iovino Enterprises, LLC/M007-NYCHA-Coney Island Sites - Documents/General/08 - BUDGET & COST/Cost Codes/Contract Forecasting Spreadsheet/Period 12 Export 12.09.22.xlsx'
cost_rprt_df = pd.read_excel(cost_rprt_path)



