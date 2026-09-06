import pandas as pd
import numpy as np
import app

def test_load_data():
    data = app.load_data('test_data.csv')
    assert isinstance(data, pd.DataFrame)

def test_clean_data():
    data = pd.DataFrame({'Name': ['John', 'Anna', ''], 'Age': [28, 26, np.nan]})
    clean_data = app.clean_data(data)
    assert clean_data.isnull().sum().sum() == 0
    
def test_get_average_age():
    data = pd.DataFrame({'Name': ['John', 'Anna'], 'Age': [28, 26]})
    avg_age = app.get_average_age(data)
    assert avg_age == 27.0