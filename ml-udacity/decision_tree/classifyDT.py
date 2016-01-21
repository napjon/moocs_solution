
def classify(features_train, labels_train):
    from sklearn import tree
    clf = tree.DecisionTreeClassifier()
    clf.fit(features_train, labels_train)
    
    return clf