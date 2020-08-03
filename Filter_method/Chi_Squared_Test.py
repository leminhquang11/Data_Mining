from functools import reduce
from library import *
from scipy.stats import chi2_contingency, chi2

#calculate p-value of 2 categorical variable
def chi_score(contigency_table, significance = 0.05):
    stat, p, df, expected = chi2_contingency(contigency_table)
    if (p>= significance):
        print("Fail to reject H0 that 2 Features are independent ")
    else: print("Reject H0, 2 Features are dependent")
    return p

#Example:
df = pd.read_csv("/home/ad/Downloads/DataMining_Lab/crop_data_anva/crop_data.csv")
n = len(df.columns)-1
for i in combination(df.columns[:n]):
    print('------------------------------')
    print(chi_score(create_contigency_from_2CA(df, i[0], i[1])))
    print('------------------------------')