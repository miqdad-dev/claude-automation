import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

def import_data():
    balance_data = pd.read_csv('balance-scale.data', sep= ',', header= None)
    return balance_data

def split_dataset(balance_data):
    X = balance_data.values[:, 1:5]
    Y = balance_data.values[:,0]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 100)
    return X, Y, X_train, X_test, Y_train, Y_test

def train_using_gini(X_train, X_test, Y_train):
    clf_gini = RandomForestClassifier(criterion = "gini", random_state = 100, max_depth=3, min_samples_leaf=5)
    clf_gini.fit(X_train, Y_train)
    return clf_gini

def prediction(X_test, clf_object):
    Y_pred = clf_object.predict(X_test)
    print("Predicted values:")
    print(Y_pred)
    return Y_pred

def cal_accuracy(Y_test, Y_pred):
    print("Confusion Matrix: ", confusion_matrix(Y_test, Y_pred))
    print ("Accuracy : ", accuracy_score(Y_test,Y_pred)*100)
    print("Report : ", classification_report(Y_test, Y_pred))

def main():
    data = import_data()
    X, Y, X_train, X_test, Y_train, Y_test = split_dataset(data)
    clf_gini = train_using_gini(X_train, X_test, Y_train)
    print("Results Using Gini Index:")
    Y_pred_gini = prediction(X_test, clf_gini)
    cal_accuracy(Y_test, Y_pred_gini)

if __name__=="__main__":
    main()