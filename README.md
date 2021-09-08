<h1> ADG ML CLASS </h1>

##### This is a class used to find the best parameters to train your machine learning module, also useful for plotting a cool confusion matrix.

<a href="https://colab.research.google.com/github/ADGVLOGS/adgmlclass/blob/main/ADGMLCLASSDemo.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Interactive Demo"/></a>



#### Downloading Module

````
pip install adgmlclass
````

#### Usage 

##### Importing module
````
import adgmlclass
ml = adgmlclass.adgmodel()
````

##### Functions 
````
FindBestModel - finds best model to use
````

````
plot_confusion_matrix - returns a matlab confusion matrix
````

````
Train - Trains a model and returns accuracy matrics with Confusion Matrix.
````

##### Basic Usage
````
ml train currently supports - 
{
svm,tree,knn,LogisticRegression
}

Parameters for function

Model,X_test,Y_test,X_train,Y_train,Parameters for Model

Example - Parameters for Model dictionary 
{'criterion': ['gini', 'entropy'], 'splitter': ['best', 'random'], 'max_depth': [2, 4, 6, 8, 10, 12, 14, 16, 18], 'max_features': ['auto', 'sqrt'], 'min_samples_leaf': [1, 2, 4], 'min_samples_split': [2, 5, 10]} 


Default if want to use ADG Fine tuned default dictionary.
ml.Train('svm',X_test,Y_test,X_train,Y_train,'')
````

#### Return Confusion Matrix
````
Parameters
(from train split)
y_test 

(from predicting model)
y_pred

(what you want to name your graph)
title

(name of True Y AXIS)
truelbl

(name of False Y AXIS)
falselbl

ml.plot_confusion_matrix(y_test, y_pred, title, truelbl, falselbl)
````


#### Find best Function to use for training - Uses ADG ML Tuned Formula
````
Parameters you get from Train Split function
Eg X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=2)


ml.FindBestModel(X_test, Y_test, X_train, Y_train)
````


##### Copyright ADGSTUDIOS 2021

------------------------------
| Date        | Changes      |
|-------------|--------------|
| 2021/09/01  | First Commit |
| 2021/09/02  | Github Workflow + Documentation| 

