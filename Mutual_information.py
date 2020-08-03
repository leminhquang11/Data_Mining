from sklearn.feature_selection import mutual_info_regression, mutual_info_classif
from library import *
#CALCULATE THE MUTUAL INFORMATION BETWEEN THE LAST COLUMN AND EACH LEFT FEATURES

#RETURN AN ARRAY OF MI SCORE FOR CONTINUOUS TARGET VARIABLE
def mutual_info_continuous(dataframe):
    n_feature = len(dataframe.columns) - 1
    mi = mutual_info_regression(dataframe[dataframe.columns[:n_feature]],
                                np.array(dataframe[dataframe.columns[n_feature:]]).reshape(-1))
    return mi

#RETURN AN ARRAY OF MI SCORE FOR CATEGORICAL TARGET VARIABLE
def mutual_info_categorical(dataframe):
    n_feature = len(dataframe.columns) - 1
    mi = mutual_info_classif(dataframe[dataframe.columns[:n_feature]],
                             np.array(dataframe[dataframe.columns[n_feature:n_feature+1]]).reshape(-1))
    return mi

df = pd.read_csv("/home/ad/Downloads/DataMining_Lab/crop_data_anva/crop_data.csv")
print(mutual_info_continuous(df))

from sklearn.datasets import load_iris
data = load_iris()
df = convert_Bench2Dataframe(data)
print(mutual_info_categorical(df))