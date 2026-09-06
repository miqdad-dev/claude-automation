import pandas as pd
import numpy as np

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    data.replace("", np.nan, inplace=True)
    data.dropna(inplace=True)
    return data

def get_average_age(data):
    return data['Age'].mean()

def main():
    data = load_data('data.csv')
    clean_data = clean_data(data)
    avg_age = get_average_age(clean_data)
    print(f'Average age: {avg_age}')

if __name__ == "__main__":
    main()