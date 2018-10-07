# Word Embeddings :-

A computer can match two strings and tell you whether they are same or not. But how do we make computers tell you about football or Ronaldo when you search for Messi?

The answer to the above questions lie in creating a representation for words that capture their meanings, semantic relationships and the different types of contexts they are used in.

And all of these are implemented by using Word Embeddings or numerical representations of texts so that computers may handle them.

## 1. What are Word Embeddings?

In very simplistic terms, Word Embeddings are the texts converted into numbers. 

But before we dive into the details of Word Embeddings, the following question should be asked – Why do we need Word Embeddings?

As it turns out, many Machine Learning algorithms and almost all Deep Learning Architectures are incapable of processing strings or plain text in their raw form. They require numbers as inputs to perform any sort of job, be it classification, regression etc.

Let us now define Word Embeddings formally. A Word Embedding format generally tries to map a word using a dictionary to a vector. Let us break this sentence down into finer details to have a clear view.

Take a look at this example – sentence=” Word Embeddings are Word converted into numbers ”

A word in this sentence may be “Embeddings” or “numbers ” etc.

A dictionary may be the list of all unique words in the sentence. So, a dictionary may look like – [‘Word’,’Embeddings’,’are’,’Converted’,’into’,’numbers’]

A vector representation of a word may be a one-hot encoded vector where 1 stands for the position where the word exists and 0 everywhere else. The vector representation of “numbers” in this format according to the above dictionary is [0,0,0,0,0,1] and of converted is[0,0,0,1,0,0].

This is just a very simple method to represent a word in the vector form. Let us look at different types of Word Embeddings or Word Vectors and their advantages and disadvantages over the rest.

## 2. Different types of Word Embeddings

The different types of word embeddings can be broadly classified into two categories-

    I.Frequency based Embedding
    II.Prediction based Embedding

Let us try to understand each of these methods in detail.

### 2.1 Frequency based Embedding

There are generally three types of vectors that we encounter under this category.

    I.Count Vector
    II.TF-IDF Vector
    III.Co-Occurrence Vector

Let us look into each of these vectorization methods in detail.

### 2.1.1 Count Vector

Consider a Corpus C of D documents {d1,d2…..dD} and N unique tokens extracted out of the corpus C. The N tokens will form our dictionary and the size of the Count Vector matrix M will be given by D X N. Each row in the matrix M contains the frequency of tokens in document D(i).

Let us understand this using a simple example.

    D1: He is a lazy boy. She is also lazy.

    D2: Neeraj is a lazy person.

The dictionary created may be a list of unique tokens(words) in the corpus =[‘He’,’She’,’lazy’,’boy’,’Neeraj’,’person’]

Here, D=2, N=6

The count matrix M of size 2 X 6 will be represented as –

<p align = "center">
    <img src = "https://github.com/Balajisivakumar92/100_DAYS_OF_ML_CHALLENGE/blob/master/ML%20code-s/Day%2025%20-%20word2vec/img/count%20vector.png">
</p>

Now, a column can also be understood as word vector for the corresponding word in the matrix M. For example, the word vector for ‘lazy’ in the above matrix is [2,1] and so on.Here, the rows correspond to the documents in the corpus and the columns correspond to the tokens in the dictionary. The second row in the above matrix may be read as – D2 contains ‘lazy’: once, ‘Neeraj’: once and ‘person’ once.

### 2.1.2 TF-IDF vectorization

## 2.2 Prediction based Vector

### 2.2.1 CBOW (Continuous Bag of words)

The way CBOW work is that it tends to predict the probability of a word given a context. A context may be a single word or a group of words. But for simplicity, I will take a single context word and try to predict a single target word.

Suppose, we have a corpus C = “Hey, this is sample corpus using only one context word.” and we have defined a context window of 1. This corpus may be converted into a training set for a CBOW model as follow. The input is shown below. The matrix on the right in the below image contains the one-hot encoded from of the input on the left.

<p align = "center">
    <img src = "https://github.com/Balajisivakumar92/100_DAYS_OF_ML_CHALLENGE/blob/master/ML%20code-s/Day%2025%20-%20word2vec/img/cbow1.png">
</p>

This matrix shown in the above image is sent into a shallow neural network with three layers: an input layer, a hidden layer and an output layer. The output layer is a softmax layer which is used to sum the probabilities obtained in the output layer to 1. Now let us see how the forward propagation will work to calculate the hidden layer activation.

Let us first see a diagrammatic representation of the CBOW model.

<p align = "center">
    <img src = "https://github.com/Balajisivakumar92/100_DAYS_OF_ML_CHALLENGE/blob/master/ML%20code-s/Day%2025%20-%20word2vec/img/Screenshot-from-2017-06-04-22-40-29.png">
</p>

### The flow is as follows:

        The input layer and the target, both are one- hot encoded of size [1 X V]. Here V=10 in the above example.
        There are two sets of weights. one is between the input and the hidden layer and second between hidden and output layer.
        Input-Hidden layer matrix size =[V X N] , hidden-Output layer matrix  size =[N X V] : Where N is the number of dimensions we choose to represent our word in. It is arbitary and a hyper-parameter for a Neural Network. Also, N is the number of neurons in the hidden layer. Here, N=4.
        There is a no activation function between any layers.( More specifically, I am referring to linear activation)
        The input is multiplied by the input-hidden weights and called hidden activation. It is simply the corresponding row in the input-hidden matrix copied.
        The hidden input gets multiplied by hidden- output weights and output is calculated.
        Error between output and target is calculated and propagated back to re-adjust the weights.
        The weight  between the hidden layer and the output layer is taken as the word vector representation of the word.


link - https://www.analyticsvidhya.com/blog/2017/06/word-embeddings-count-word2veec/
