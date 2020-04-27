import pandas as pd 
import numpy as np
from sklearn import preprocessing

titanic_data = pd.read_csv('train.csv')
#print(titanic_data.head())

titanic_data.drop(['PassengerId','Name','Ticket','Cabin'],'columns',inplace=True)
#print(titanic_data.head())

# Convert gender to 0 or 1
label_enc =preprocessing.LabelEncoder()
titanic_data['Sex'] = label_enc.fit_transform(titanic_data['Sex'].astype(str))
#print(titanic_data.head())

# One-hot encoding of 'Embarked' with pd.get_dummies
titanic_data = pd.get_dummies(titanic_data,columns=['Embarked'])
#print(titanic_data.head())

# print('Before drop-------------')
# print(len(titanic_data))
# dropped = (len(titanic_data) - len(titanic_data.dropna()))
titanic_data = titanic_data.dropna()
# print('After drop--------------')
# print(len(titanic_data))
# print('{} has been dropped because of n/a values'.format(dropped))

# what is the best bandwidth to use for our dataset?
# The smaller values of bandwith result in tall skinny kernels & larger values result in short fat kernels.
from sklearn.cluster import estimate_bandwidth
print(estimate_bandwidth(titanic_data))

from sklearn.cluster import MeanShift
analyzer = MeanShift(bandwidth=30) 
analyzer.fit(titanic_data)
print(analyzer)

labels = analyzer.labels_
#print(labels)
print(np.unique(labels))

#We will add a new column in dataset which shows the cluster the data of a particular row belongs to.
titanic_data['cluster_group'] = np.nan
data_length=len(titanic_data)
for i in range(data_length): # loop 714 rows
    titanic_data.iloc[i,titanic_data.columns.get_loc('cluster_group')] = labels[i] #set the cluster label on each row
#print(titanic_data.head())

print(titanic_data.describe())

#Grouping passengers by Cluster
titanic_cluster_data = titanic_data.groupby(['cluster_group']).mean()
#Count of passengers in each cluster
titanic_cluster_data['Counts'] = pd.Series(titanic_data.groupby(['cluster_group']).size())
print(titanic_cluster_data)