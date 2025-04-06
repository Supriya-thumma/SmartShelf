# data_handler.py
import pandas as pd

def load_data(file_paths):
    data_dict = {}
    for file_path in file_paths:
        data_name = file_path.split("\\")[-1].split(".")[0]
        data_dict[data_name] = pd.read_csv(file_path)
    return data_dict

def preprocess_data(data):
    if 'Date' in data.columns:
        data['Date'] = pd.to_datetime(data['Date'])
    return data
