# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 10:56:11 2016

@author: ramesh
"""
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn import tree
def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    #clf = GaussianNB()    
    #clf = svm.SVC()
    clf = tree.DecisionTreeClassifier()    
    clf = tree.DecisionTreeClassifier(min_samples_split=50)
    clf.fit(features_train, labels_train)
    return clf
    
    ### your code goes here!
    
