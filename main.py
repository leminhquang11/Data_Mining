import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_regression, mutual_info
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy.stats import kendalltau



np.random.seed(0)
X = np.random.rand(1000, 3)
y = X[:,0] + np.sin(6* np.pi * X[:,1]) + 0.1 * np.random.rand(1000)

mi = mutual_info_regression(X,y)
#mi /= np.max(mi)

pe = np.empty([3])
sp = np.empty([3])
ke = np.empty([3])
for i in range(3):
    pe[i], _ = pearsonr(X[:,i],y)
    sp[i], _ = spearmanr(X[:,i],y)

print(pe)
print(sp)

plt.figure(figsize=(15,5))

for i in range(3):
    plt.subplot(1,3,i+1)
    plt.scatter(X[:,i], y, edgecolors='black', s = 20)
    plt.xlabel("$x_{}$".format(i+1, fontsize = 14))
    if i ==0:
        plt.ylabel("$y$", fontsize = 14)
    plt.title("MI = {:.2f}, PE = {:.2f}, SP = {:.2}".format(mi[i], pe[i], sp[i], fontsize = 16))

plt.show()