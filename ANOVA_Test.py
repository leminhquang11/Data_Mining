from library import *
from scipy.stats import f_oneway
df = pd.read_csv("https://raw.githubusercontent.com/researchpy/Data-sets/master/difficile.csv")

#CALCULATE ANOVA SCORE WITH A FEATURES CORRESPONDING WITH CONTINUOUS TARGET VARIABLE
def anova(df):
    str_command = 'stat, p = f_oneway('
    for i in range(len(df.columns)):
        str_command += 'df[df.columns['+str(i)+']]'
        str_command += '' if (i==len(df.columns)-1) else ','
    str_command += ')'
    exec (str_command, globals())
    return stat, p

print(anova(df))