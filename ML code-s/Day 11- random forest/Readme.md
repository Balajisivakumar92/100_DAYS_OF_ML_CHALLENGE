# What is Random forest algorithm?

Random forest algorithm is a supervised classification algorithm. 
As the name suggest, this algorithm creates the forest with a number of trees.

The more number of trees in the forest gives the **high accuracy result**.

<p align="center">
  <img width="500" height="350" src="https://github.com/Balajisivakumar92/100_DAYS_OF_ML_CHALLENGE/blob/master/ML%20code-s/Day%2011-%20random%20forest/img/images.png">
</p>
     
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
       
## Random forest algorithm applications.
          
    Below are some the application where random forest algorithm is widely used.

    1.Banking
    2.Medicine
    3.Stock Market
    4.E-commerce
    
<p align="center">
  <img width="300" height="300" src="https://github.com/Balajisivakumar92/100_DAYS_OF_ML_CHALLENGE/blob/master/ML%20code-s/Day%2011-%20random%20forest/img/Random-Forest-Applications.jpg">
</p>

1.Banking:

     In the banking sector, random forest algorithm widely used in two main application. These are for finding the loyal customer and finding the fraud customers.

     The loyal customer means not the customer who pays well, but also the customer whom can take the huge amount as loan and pays the loan interest properly to the bank. As the growth of the bank purely depends on the loyal customers. The bank customers data highly analyzed to find the pattern for the loyal customer based the customer details.

     In the same way, there is need to identify the customer who are not profitable for the bank, like taking the loan and paying the loan interest properly or find the outlier customers. If the bank can identify theses kind of customer before giving the loan the customer.  Bank will get a chance to not approve the loan to these kinds of customers. In this case, also random forest algorithm is used to identify the customers who are not profitable for the bank.

2.Medicine

     In medicine field, random forest algorithm is used identify the correct combination of the components to validate the medicine. Random forest algorithm also helpful for identifying the disease by analyzing the patient’s medical records.

3.Stock Market

     In the stock market, random forest algorithm used to identify the stock behavior as well as the expected loss or profit by purchasing the particular stock.

4.E-commerce

     In e-commerce, the random forest used only in the small segment of the recommendation engine for identifying the likely hood of customer liking the recommend products base on the similar kinds of customers.

     Running random forest algorithm on very large dataset requires high-end GPU systems. If you are not having any GPU system. You can always run the machine learning models in cloud hosted desktop. You can use clouddesktoponline platform to run high-end machine learning models from sitting any corner of the world.
