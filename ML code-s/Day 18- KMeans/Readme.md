# KMeans clustering

K-means clustering is a type of unsupervised learning, which is used when you have unlabeled data (i.e., data without defined categories or groups). The goal of this algorithm is to find groups in the data, with the number of groups represented by the variable K. The algorithm works iteratively to assign each data point to one of K groups based on the features that are provided. Data points are clustered based on feature similarity. The results of the K-means clustering algorithm are:

    >The centroids of the K clusters, which can be used to label new data
    >Labels for the training data (each data point is assigned to a single cluster)

## steps involed in KMeans clustering 

### step1:
Choose the number k of cluster.

### step2:
select at random k point, the centroids (not necessariy from your dataset).

### step3:
Assign each data point to the closest centroid -> That forms the K cluster.

### step4:
compute and place the new centroid of each cluster.

### step5:
Reassign each data point to the new closest centroid.

# DONE
