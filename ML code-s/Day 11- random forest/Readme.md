# What is Random forest algorithm?

Random forest algorithm is a supervised classification algorithm. 
As the name suggest, this algorithm creates the forest with a number of trees.

##### * The more number of trees in the forest gives the high accuracy result.

     > You might be thinking are we creating more number of decision trees and how can we create more number of decision trees. As all the calculation of nodes selection will be same for the same dataset.

     > Yes. You are true. To model more number of decision trees to create the forest you are not going to use the same apache of constructing the decision with information gain or gini index approach.

     > In decision tree algorithm calculating these nodes and forming the rules will happen using the information gain and gini index calculations.

     > But In random forest algorithm, Instead of using information gain or gini index for calculating the root node, the process of finding the root node and splitting the feature nodes will happen randomly.
## Take any Sample dataset
#### step 1:
      Pick at random "k" data points from the training set.
#### step 2:
      Build the decision tree associated to these "k" data points.
#### step 3:
      Choose the number Ntree of trees you want to build and repeat step 1 & 2.
#### step 4:
       For a new data points make each one of your Ntree trees predict the category to which the data points belongs, and assign the new data points to the category that wins the majority vote.



