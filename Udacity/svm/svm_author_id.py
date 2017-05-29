#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
from sklearn import svm
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

import numpy as np
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

clf = svm.SVC()
clf.fit(features_train, labels_train)

predict=clf.predict(features_test)

print np.dot(predict,labels_test)





#########################################################


