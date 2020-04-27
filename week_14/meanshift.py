import pandas as pd
import numpy as np

# 1. Load 'iris_data.csv' into a dataframe
# 2. Get unique labels (Species column)
# 3. Plot with a scatter plot each iris flower sample colored by label (3 different colors)
# 4. Use: MeanShift and estimate_bandwidth from sklearn.cluster to first estimate bandwidth and then get the clusters (HINT: estimate_bandwidth() takes an argument: quantile set it to 0.2 for best result
#    print out labels, cluster centers and number of clusters (as returned from the MeanShift function
# 5. Create a new scatter plot where each flower is colored according to cluster label
# 6. Add a dot for the cluster centers
# 7. Compare the 2 plots (colored by actual labels vs. colored by cluster label)

# 1. Load 'iris_data.csv' into a dataframe
data = pd.read_excel('iris_data.xlsx')
#print(data.head())

# 2. Get unique labels (Species column)
labels_unique = np.unique(data['Species'])

# 3. Plot with a scatter plot each iris flower sample colored by label (3 different colors)
import matplotlib.pyplot as plt

# for label in labels_unique:
#     plt.scatter(x='Sepal length', y='Petal length', data=data[data.Species==label])
#     plt.scatter(x='Sepal width', y='Petal width', data=data[data.Species==label])
# plt.show()

# 4. Use: MeanShift and estimate_bandwidth from sklearn.cluster to first estimate bandwidth and then get the clusters (HINT: estimate_bandwidth() takes an argument: quantile set it to 0.2 for best result
#    print out labels, cluster centers and number of clusters (as returned from the MeanShift function
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn import preprocessing

label_enc =preprocessing.LabelEncoder()
data['Species'] = label_enc.fit_transform(data['Species'].astype(str))

def mean_shift(data, n_samples=1000):
    bandwidth = estimate_bandwidth(data, quantile=0.2, 
                                   n_samples=n_samples)

    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(data)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters = len(labels_unique)

    print('Number of estimated clusters : {}'.format(n_clusters))
    
    return labels, cluster_centers, n_clusters

labels, cluster_centers, n_clusters = mean_shift(data)
print(labels, cluster_centers, n_clusters)

# 5. Create a new scatter plot where each flower is colored according to cluster label
