from numpy import number
import xlsxwriter as xl
import pandas as pd
from datetime import date
import pprint as pp
import json
import pickle
from formats import *
import matplotlib.pyplot as plt 

from LoadCosts import cost_rprt_df
from LoadActivities import schedule_df

def filter_code_from_schedule(dataframe, cost_code):
    return dataframe[dataframe['Cost Code'] == cost_code]


# pp.pprint(schedule_df.columns)
status = 'Activity Status'
start = '(*)Start'
end = '(*)Finish'
duration = 'Original Duration(h)'
remaining = 'Remaining Duration(h)'
percent = 'Activity % Complete'
sub_code = 'Sub-Cost Code'
location = 'Building/Area'
name = 'Activity Name'

def dataframe_convert_timestamp_to_date(dataframe, columns):
    for x in columns:
        dataframe[x] = pd.to_datetime(dataframe[x]).dt.date
    return dataframe


def days_without_weekends(start, end):
    days = (end - start).days + 1
    weeks, days = divmod(days, 7)
    days -= min(days, 5)
    return weeks * 5 + days

def get_days_by_location(code_df):
    days_by_location = {}
    for x in range(len(code_df)):
        #todays date
        today = date.today()
        starting = today if code_df.iloc[x][start] < today else code_df.iloc[x][start]
        ending = code_df.iloc[x][end] if code_df.iloc[x][end] > today else today

        days = days_without_weekends(starting, ending)

        if code_df.iloc[x][location] in days_by_location:
            days_by_location[code_df.iloc[x][location]] += days
        else:
            days_by_location[code_df.iloc[x][location]] = days
    return days_by_location

def total_days(code_df):
    total = 0
    for x in range(len(code_df)):
        #todays date
        today = date.today()
        starting = today if code_df.iloc[x][start] < today else code_df.iloc[x][start]
        ending = code_df.iloc[x][end] if code_df.iloc[x][end] > today else today

        days = days_without_weekends(starting, ending)
        total += days
    return total




# formwork_eb = filter_code_from_schedule(schedule_df, '03-1100')
# formwork_eb = formwork_eb[formwork_eb[status] != 'Completed']
# formwork_eb = dataframe_convert_timestamp_to_date(formwork_eb, [start, end])
# print(get_days_by_location(formwork_eb))
# print(total_days(formwork_eb))



# for x in range(len(formwork_eb)):
# for x in range(0, 10):
#     start = formwork_eb.iloc[x][start]
#     end = formwork_eb.iloc[x][end]
#     duration = formwork_eb.iloc[x][duration]
#     remaining = formwork_eb.iloc[x][remaining]
#     percent = formwork_eb.iloc[x][percent]
#     sub_code = formwork_eb.iloc[x][sub_code]
#     location = formwork_eb.iloc[x][location]
#     name = formwork_eb.iloc[x][name]

#     print(f'Start is: {start}, End is: {end}, dif: {end - start}, duration: {duration}')







