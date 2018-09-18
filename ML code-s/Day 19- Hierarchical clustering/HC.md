# Hierarchical Clustering

### Importing the libraries
```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
```

### Importing the dataset
```python
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3, 4]].values
```

### Using the dendrogram to find the optimal number of clusters
```python
import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()
```
<p align = "center">
  <img width = "500" height = "350" src = "https://github.com/Balajisivakumar92/100_DAYS_OF_ML_CHALLENGE/blob/master/ML%20code-s/Day%2019-%20Hierarchical%20clustering/img/dendro%20gram%20result.png">
</p>

### Fitting Hierarchical Clustering to the dataset
```python
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)
```

### Visualising the clusters
```python
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
```
<p align = "center">
  <img width = "500" height = "350" src = "https://github.com/Balajisivakumar92/100_DAYS_OF_ML_CHALLENGE/blob/master/ML%20code-s/Day%2019-%20Hierarchical%20clustering/img/final%20output.png">
</p>
