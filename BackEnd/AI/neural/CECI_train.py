# IMPORTAR LIBRERIAS
import pandas as pd
import sklearn as sk
import tensorflow as tf
from sklearn import tree
import pickle as pk
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
# IMPORTAR Y ORGANIZAR DATASET
total_dataset = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
train_dataset = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
X_dataset = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
y_dataset = [33]
X=pd.read_csv('dataset_train.csv',header = 0,sep = ";",usecols = X_dataset, decimal = ":")
y=pd.read_csv('dataset_train.csv',header = 0,sep = ";",usecols = y_dataset)
#TRAIN
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .8)
my_classifier = tree.DecisionTreeClassifier()
my_classifier.fit(X_train, y_train)


filename = "ceci_clf.sav"
pk.dump(my_classifier, open(filename, 'wb'))

#loaded_model = pk.load(open(filename, 'rb'))
#predictions = loaded_model.predict(X_test)
#print(accuracy_score(y_test, predictions))
