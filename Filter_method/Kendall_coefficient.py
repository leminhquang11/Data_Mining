from library import *
from scipy.stats import kendalltau

#CALCULATE SPEARMAN COEFFICIENT OF RANKED DATAFRAME
def kendall(df):
    coef = dict()
    for couple in combination(df.columns):
        coef[(couple[0], couple[1])] = kendalltau(df[couple[0]], df[couple[1]])[0]
    return coef

df = pd.read_csv("/home/ad/Downloads/DataMining_Lab/crop_data_anva/crop_data.csv")

print(kendall(convert_continuousDf_rankingDf(df)))