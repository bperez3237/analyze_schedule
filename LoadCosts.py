
import pandas as pd
from models.Activity import Activity
from models.CostCode import CostCode
import json
import pickle

def filter_cost_code(dataframe, cost_code):
    return dataframe[dataframe['Cost Code'] == cost_code]

def remove_columns(dataframe, columns):
    return dataframe.drop(columns, axis=1)

cost_rprt_path = f'C:/Users/bperez/Iovino Enterprises, LLC/M007-NYCHA-Coney Island Sites - Documents/General/08 - BUDGET & COST/Cost Codes/Contract Forecasting Spreadsheet/Period 12 Export 12.09.22.xlsx'
cost_rprt_df = pd.read_excel(cost_rprt_path)

# costs = []
# for y in range(len(cost_rprt_df)):
#     new_cost = CostCode(
#         bill_code = cost_rprt_df.iloc[y]['Bill Code'],
#         phase_code = cost_rprt_df.iloc[y]['Phase'],
#         name = cost_rprt_df.iloc[y]['Name'],
#         qty = cost_rprt_df.iloc[y]['Output Projected Qty'],
#         uom = cost_rprt_df.iloc[y]['Output WM Code'],
#         mhs = cost_rprt_df.iloc[y]['Input Projected Qty'],
#         forecast = cost_rprt_df.iloc[y]['Projected Cost Forecast'],
#         spent = cost_rprt_df.iloc[y]['Spent/Committed Total'],
#         qtd = cost_rprt_df.iloc[y]['Output Completed Qty'],
#         mtd = cost_rprt_df.iloc[y]['Input Completed Qty']
#     )
#     costs.append(new_cost)

# with open('./data/costs.pickle', 'wb') as f:
#     pickle.dump(costs,f)

