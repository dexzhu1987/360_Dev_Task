import os
import importlib
import csv, json

import pandas as pd

TIMEVISITEDTOBELOYALS = 10

def import_csv_data(fn):
    '''
    Function to import .csv data and add column headers.
    Input(s):  string  :  Str specifying the .csv file name.
    Output(s):  dataframe  :  DataFrame object of with heads
    '''
    df = pd.read_csv(
        fn,
        sep = ',',
        names = [
            "datetime",
            "user",
            "os_id",
            "device_id"
        ]
        
    )

    return df

def get_unique_visitors(data_df):
    '''
    Function to return the number of unique website visitors from the input dataframe.
    Input (s): dataframe : dataframe object of tabular data.  
    Output (s): array : unique visitors array.
    '''
    return pd.unique(data_df.user)


def get_number_of_loyal_visitors(data_df):
    '''
    Function to get the number of loyal visitors to the website.
    Input(s):  dataframe : dataframe object of tabular data.
    Output(s): int  : loyal visitors number visted more than certain times (defined on top)
    '''
    
    visits = {}

    for each_user in pd.unique(data_df.user):
        visits[each_user] = data_df.datetime[data_df.user == each_user]

    loyal_visitors = 0

    for each_user in visits.keys():
        if visits[each_user].size >= TIMEVISITEDTOBELOYALS:
             loyal_visitors+=1

    return loyal_visitors


def parse_data_by_device_id(data_df, device_id_string_array):
    '''
    Method to parse the data according to the device_id
    Inputs:  data_df  : dataframe :  DataFrame object containing the original data imported from 'data.csv'.
             array  : array specifying the Device ID 
    Outputs: dataframe  :  dataframe with seleted rows
    '''
    device_int_id = []
    for value in device_id_string_array:
        device_int_id.append(int(value))
    df = data_df[data_df['device_id'].isin(device_int_id)]


    return df

def parse_data_by_os_id(data_df, os_id_string_array):
    '''
    Method to parse the input csv data based on the OS ID:
    Inputs: csv_format_df  : dataframe : dataFrame object containing the original data
            array  : array  object specifying the OS id
    Ouputs: dataframe  :  dataframe with seleted rows
    '''
    os_int_id = []
    for value in os_id_string_array:
        os_int_id.append(int(value))
    df = data_df[data_df['os_id'].isin(os_int_id)]
   
    return df



