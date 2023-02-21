import numpy as np 
import pandas as pd 
import math
file = pd.read_csv(r'dataset_not_final',header = None)
data=file.values
print(data.shape)