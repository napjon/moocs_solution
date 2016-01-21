
"""
    starter code for the validation mini-project
    the first step toward building your POI identifier!

    start by loading/formatting the data

    after that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.tree import DecisionTreeClassifier

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)


features_train,features_test,labels_train,labels_test = cross_validation.train_test_split(features,labels,test_size=0.3,
                                                                                          random_state=42)
clf = DecisionTreeClassifier()
clf.fit(features_train,labels_train)
clf.score(features_test,labels_test)