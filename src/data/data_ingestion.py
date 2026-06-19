import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import yaml
import logging

def load_params(params_path: str) -> dict:
    try:
        with open(params_path,'r') as file:
            params = yaml.safe_load(file)
        logging.debug('Parameters Retrieved from %s', params_path)
        return params
    except FileNotFoundError:
        logging.error('File not found: %s', params_path)
        raise
    except yaml.YAMLError as e:
        logging.error('YAML error: %s', e)
        raise
    except Exception as e:
        logging.error('Unexpected error: %s', e)
        raise

def load_data(data_url: str) -> pd.DataFrame:
    try:
        df= pd.read_csv(data_url)
        logging.info('Data loaded from %s')