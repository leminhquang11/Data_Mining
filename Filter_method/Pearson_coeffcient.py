from scipy.stats import pearsonr
import pandas as pd
import numpy as np
from library import *

#CALCULATE PEARSON COEFFICIENT OF DATAFRAME FUNCTION FOR ALL COMBINATION 2 FEATURES OF DATAFRAME
def pearson(df):
    coef = dict()
    for couple in combination(df.columns):
        coef[(couple[0], couple[1])] = pearsonr(df[couple[0]], df[couple[1]])[0]
    return coef

#READ DATA TABLE FROM CSV FILE
df = pd.read_csv("/home/ad/Downloads/DataMining_Lab/crop_data_anva/crop_data.csv")

print(pearson(df))

