# Our modules

# NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np
# Matplotlib is a plotting library for python and pyplot gives us a MatLab like plotting framework. We will use this in our plotter function to plot data.
import matplotlib.pyplot as plt
# Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics
import seaborn as sns
# Allows us to test parameters of classification algorithms and find the best one
from sklearn.model_selection import GridSearchCV
# Logistic Regression classification algorithm
from sklearn.linear_model import LogisticRegression
# Support Vector Machine classification algorithm
from sklearn.svm import SVC
# Decision Tree classification algorithm
from sklearn.tree import DecisionTreeClassifier
# K Nearest Neighbors classification algorithm
from sklearn.neighbors import KNeighborsClassifier
# Confusion Matrix classification
from sklearn.metrics import confusion_matrix


# ADGSTUDIOS 2021
class adgmodel:   
    def plot_confusion_matrix(self, y_test, y_pred, title, truelbl, falselbl):
        try:
            print("")
            ticklabels = []
            ticklabels.append(truelbl)
            ticklabels.append(falselbl)
            cm = confusion_matrix(y_test, y_pred)
            ax = plt.subplot()
            sns.heatmap(cm, annot=True, ax=ax)
            ax.set_xlabel('Predicted labels')
            ax.set_ylabel('True labels')
            ax.set_title(title)
            ax.xaxis.set_ticklabels(ticklabels)
            ax.yaxis.set_ticklabels(ticklabels)
        except Exception as e:
            print('Error : ADGMLCLASS \n', e)

    def __logregcv(self, X_test, Y_test, X_train, Y_train, Parameters):
        if len(Parameters) > 0:
            parameters = Parameters
            pass
        else:
            parameters = {"C": [0.01, 0.1, 1], 'penalty': [
                'l2'], 'solver': ['lbfgs']}  # l1 lasso l2 ridge
            print("using parameters", parameters,
                  "Logistic Regression Algorithm")

        try:
            lr = LogisticRegression()
            gscv = GridSearchCV(lr, parameters, scoring='accuracy', cv=10)
            logreg_cv = gscv.fit(X_train, Y_train)
            print("tuned hyperparameters :(best parameters) ",
                  logreg_cv.best_params_)
            print("accuracy :", logreg_cv.best_score_)

            yhat = logreg_cv.predict(X_test)
            self.plot_confusion_matrix(
                Y_test, yhat, 'Confusion Matrix', '+', '-')
            return logreg_cv.best_score_
        except Exception as e:
            print('Error : ADGMLCLASS \n', e)

    def __svmcv(self, X_test, Y_test, X_train, Y_train, Parameters):
        if len(Parameters) > 0:
            parameters = Parameters
        else:

            parameters = {'kernel': ('linear', 'rbf', 'poly', 'rbf', 'sigmoid'),
                          'C': np.logspace(-3, 3, 5),
                          'gamma': np.logspace(-3, 3, 5)}

            print("using parameters", parameters,
                  "Support Vector Machine Algorithm")

        try:
            svm = SVC()
            gscv = GridSearchCV(svm, parameters, scoring='accuracy', cv=10)
            svm_cv = gscv.fit(X_train, Y_train)
            print("tuned hyperparameters :(best parameters) ", svm_cv.best_params_)
            print("accuracy :", svm_cv.best_score_)

            yhat = svm_cv.predict(X_test)
            self.plot_confusion_matrix(
                Y_test, yhat, 'Confusion Matrix', '+', '-')
            return svm_cv.best_score_

        except Exception as e:
            print('Error : ADGMLCLASS \n', e)

    def __tree(self, X_test, Y_test, X_train, Y_train, Parameters):
        if len(Parameters) > 0:
            parameters = Parameters
        else:
            parameters = {'criterion': ['gini', 'entropy'],
                          'splitter': ['best', 'random'],
                          'max_depth': [2*n for n in range(1, 10)],
                          'max_features': ['auto', 'sqrt'],
                          'min_samples_leaf': [1, 2, 4],
                          'min_samples_split': [2, 5, 10]}

            print("using parameters", parameters,
                  "Support Vector Machine Algorithm")
        try:
            tree = DecisionTreeClassifier()
            gscv = GridSearchCV(tree, parameters, scoring='accuracy', cv=10)
            tree_cv = gscv.fit(X_train, Y_train)

            print("tuned hyperparameters :(best parameters) ",
                  tree_cv.best_params_)
            print("accuracy :", tree_cv.best_score_)

            yhat = tree_cv.predict(X_test)
            self.plot_confusion_matrix(
                Y_test, yhat, 'Confusion Matrix', '+', '-')
            return tree_cv.best_score_
        except Exception as e:
            print('Error : ADGMLCLASS \n', e)

    def __knn(self, X_test, Y_test, X_train, Y_train, Parameters):
            if len(Parameters) > 0:
                parameters = Parameters
                pass
            else:
                parameters = {'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                              'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
                              'p': [1, 2]}

                print("using parameters", parameters, "KNN Algorithm")

            try:
                KNN = KNeighborsClassifier()
                gscv = GridSearchCV(KNN, parameters, scoring='accuracy', cv=10)
                knn_cv = gscv.fit(X_train, Y_train)

                print("tuned hyperparameters :(best parameters) ",
                      knn_cv.best_params_)
                print("accuracy :", knn_cv.best_score_)
                yhat = knn_cv.predict(X_test)
                self.plot_confusion_matrix(
                    Y_test, yhat, 'Confusion Matrix', '+', '-')
                return knn_cv.best_score_
            except Exception as e:
                print('Error : ADGMLCLASS \n', e)

    def Train(self, Model, X_test, Y_test, X_train, Y_train, Parameters):
        try:
            if Model == 'svm':
                self.__svmcv(X_test, Y_test,
                             X_train, Y_train, Parameters)
            if Model == 'tree':
                self.__tree(X_test, Y_test, X_train, Y_train, Parameters)
            if Model == 'knn':
                self.__knn(X_test, Y_test, X_train, Y_train, Parameters)
            if Model == 'LogisticRegression':
                self.__logregcv(X_test, Y_test,
                                X_train, Y_train, Parameters)

        except Exception as e:
            print('Error : ADGMLCLASS \n', e)
            print('\n')
            print('Current Models that are supported is this version is :',
                  'svm,tree,knn,LogisticRegression - Type it as a string when using the function')

    def FindBestModel(self, X_test, Y_test, X_train, Y_train):
        print(
            'Finding best model please wait using the default ADG Optimized ML Formula...')
        algorithms = {'KNN': self.__knn(X_test, Y_test, X_train, Y_train,''), 'Tree': self.__tree(X_test, Y_test, X_train, Y_train,''),
                      'LogisticRegression': self.__tree( X_test, Y_test, X_train, Y_train,''), 'SVM': self.__svmcv(X_test, Y_test, X_train, Y_train,'')}
        bestalgorithm = max(algorithms, key=algorithms.get)
        print('Best Algorithm is', bestalgorithm,
              'with a score of', algorithms[bestalgorithm])
