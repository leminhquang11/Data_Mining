import numpy as np
from sklearn.datasets import load_diabetes
from library import *
from scipy.stats import spearmanr

#CALCULATE SPEARMAN COEFFICIENT OF RANKED DATAFRAME
def spearman(df):
    coef = dict()
    for couple in combination(df.columns):
        coef[(couple[0], couple[1])] = spearmanr(df[couple[0]], df[couple[1]])[0]
    return coef

'''data = load_diabetes()
df = convert_Bench2Dataframe(data)
df = convert_continuousDf_rankingDf(df)'''

df = pd.read_csv("/home/ad/Downloads/DataMining_Lab/crop_data_anva/crop_data.csv")

print(spearman(convert_continuousDf_rankingDf(df)))