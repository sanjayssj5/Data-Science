import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt
# Mean
x = np.array([1,3,5,6])
mean_x = np.mean(x)
# in case the data contains Nan values
x_nan = np.array([1,3,5,6, math.nan])
mean_x_nan = np.nanmean(x_nan)
print(mean_x,mean_x_nan)


#Variance
x = np.array([1,3,5,6])
variance_x = np.var(x)

print(variance_x)

sns.scatterplot(x=np.arange(4),y=x)
plt.show()

print(math.sqrt(variance_x))


#Covariance

x = np.array([1,3,5,6])
y = np.array([-2,-4,-5,-6])
#this will return the covariance matrix of x,y containing x_variance, y_variance on diagonal elements and covariance of x,y
cov_xy = np.cov(x,y)
cov_xy=cov_xy.flatten()
print(cov_xy)
sns.scatterplot(x=np.arange(4),y=x)
sns.scatterplot(x=np.arange(4),y=y)
print(np.var(x),np.var(y))
sns.scatterplot(x=np.arange(4),y=cov_xy)

plt.show()


#Corelation
x = np.array([1,3,5,6])
y = np.array([-2,-4,-5,-6])
corr = np.corrcoef(x,y)
print(corr)
