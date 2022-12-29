# Spam Email Detection

## Introduction
In this project, I tackled the problem of detecting spam emails from a federated learning approach.

## Federated Learning
Nowadays, there are thousands of valuable datasets around the world. 
With the help of such datasets, countless machine learning models can be developed; however, due to the data privacy constraints this has not been possible.

Federated Learning can be a solution to this problem since it does not violate the privacy of the user's data. In this approach, clients will get an instance of the model; Each will try to train the model locally on the data they possess; After training, they will send the weights of their trained models back to the server, and the server will update the global model according to its received parameters; finally, the clients will again receive the updated model, and the cycle continues.

## Why Federated Learning for Spam Email Detection?
One might think that current approaches for spam email detection are effective enough to overlook the other possible solutions; nonetheless, I believe this problem can be further imporved with the help of Federated Learning, since:
1. The problem of detecting spam emails is an online problem, and it needs an online solution, like Federated Learning. The email that is considered spam in the future might not be spam today.
2. People share sensitive information through emails. Hence, they might not feel comfortable sharing their emails with a public dataset to train a model. Federated Learning can resolve this burden since no one will get access to the client's local data.


## Steps
Now that we have disucessed the reasons behind this project, we are going to talk about the steps I took in developing this project.

### Step 1: Data and Data Cleaning
The dataset I used is the Kaggle Simple Spam Filter. It can be found [here](https://www.kaggle.com/code/mohitr/simple-spam-filter/data).
After downloading the dataset, I took several steps to clean it and make it ready for training, all of such steps are evident in the [SED_FL_Data_Cleaning notebook](/SED_FL_Data_Cleaning.ipynb).


### Step 2: Naive Bayes Approach
There are several ways to classify a text, one of the most popular ones is Naive Bayes. The implementation of this approach can be found in the [SED_FL_NaiveـBayes notebook](/SED_FL_Naive_Bayes_Approach.ipynb).

### Step 3: Centralized BERT
BERT is a highly sophisticated languaged model that is used for various NLP tasks. My ultimate goal was to use this model in my federated learning approach; hence, to get an idea of how to work with it and train it, I developed [SED_FL_Centralized_Bert notebook](/SED_FL_Centralized_Bert.ipynb).

### Step 4: Federated Learning BERT
After developing the bert model with pytorch, I used FedAvg algorithm to train a federated learning BERT model in [SED_FL_Federated Learning Bert notebook](/SED_FL_Federated%20Learning%20Bert.ipynb).


## Results
As it is evident from the notebooks, the results of this approach were highly promising--98.4% on the test dataset.

In [Figure 1](/Figure_1.png), you can find the plots explaining train accuracy, train loss, validation accuracy, and validation loss through out the training session.

On a little note I should mention that this project was the thesis of my Bachelor's degree. :)

If you have any question, I would be delighted to answer you.