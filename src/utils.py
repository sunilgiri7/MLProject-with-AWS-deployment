import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import dill
import pickle

def save_obj(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f)
    except Exception as e:
        raise Exception(e,sys)