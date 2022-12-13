import pandas as pd
from models.Activity import Activity
from models.CostCode import CostCode
import json
import pickle

def filter_cost_code(dataframe, cost_code):
    return dataframe[dataframe['Cost Code'] == cost_code]

def remove_columns(dataframe, columns):
    return dataframe.drop(columns, axis=1)

schedule_path = f'C:/Users/bperez/Iovino Enterprises, LLC/M007-NYCHA-Coney Island Sites - Documents/General/27 - PERSONAL FOLDERS/Brian Perez/Coney Island/02 - M007 Cost/Cost Report/Cost Report 11 - 2022/November 2022 Schedule - Data.xlsx'
scheudle_df = pd.read_excel(schedule_path, sheet_name='Activities')
schedule_df = remove_columns(scheudle_df, ['WBS Code', 'ID1', 'ID2', 'ID3', 'ID4', '(*)WBS Name','(*)WBS Path'])

# activities = []
# for y in range(len(schedule_df)):
#     new_activity = Activity(
#         activity_status=schedule_df.iloc[y]['Activity Status'],
#         area=schedule_df.iloc[y]['Building/Area'],
#         activity_id=schedule_df.iloc[y]['Activity ID'],
#         type=schedule_df.iloc[y]['Type'],
#         name=schedule_df.iloc[y]['Activity Name'],
#         start_date=schedule_df.iloc[y]['(*)Start'],
#         end_date=schedule_df.iloc[y]['(*)Finish'],
#         original_duration=schedule_df.iloc[y]['Original Duration(h)'],
#         remaining_duration=schedule_df.iloc[y]['Remaining Duration(h)'],
#         percent_complete=schedule_df.iloc[y]['Activity % Complete'],
#         sub=schedule_df.iloc[y]['Sub'],
#         category_1=schedule_df.iloc[y]['Actvity Category 1'],
#         category_2=schedule_df.iloc[y]['Actvity Category 2'],
#         cost_code=schedule_df.iloc[y]['Cost Code'],
#         sub_cost_code=schedule_df.iloc[y]['Sub-Cost Code']
#     )
#     activities.append(new_activity)

# with open('./data/activities.pickle', 'wb') as f:
#     pickle.dump(activities,f)

