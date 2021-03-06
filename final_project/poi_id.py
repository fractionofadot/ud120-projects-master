#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
from test import add_deleted_items

# The features in the data fall into three major types, namely financial features, 
# email features and POI labels. financial features: ['salary', 'deferral_payments', 
# 'total_payments', 'loan_advances', 'bonus', 'restricted_stock_deferred', 
# 'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options', 
# 'other', 'long_term_incentive', 'restricted_stock', 'director_fees'] (all units 
# 	are in US dollars) email features: ['to_messages', 'email_address', 
# 'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi', 'poi', 
# 'shared_receipt_with_poi'] (units are generally number of emails messages; notable 
# 	exception is 'email_address', which is a text string) POI label: ['poi'] 
# (boolean, represented as integer)

# You are encouraged to make, transform or rescale new features from the starter features. 
# If you do this, you should store the new feature to my_dataset, and if you use the new 
# feature in the final algorithm, you should also add the feature name to my_feature_list, 
# so your coach can access it during testing. For a concrete example of a new feature that 
# you could add to the dataset, refer to the lesson on Feature Selection.

# salary
# to_messages
# deferral_payments
# total_payments
# exercised_stock_options
# bonus
# restricted_stock
# shared_receipt_with_poi
# restricted_stock_deferred
# total_stock_value
# expenses
# loan_advances
# from_messages
# other
# from_this_person_to_poi
# poi
# director_fees
# deferred_income
# long_term_incentive
# email_address
# from_poi_to_this_person

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".

financial_features = ['salary', 'deferral_payments', 'total_payments',
 'loan_advances', 'bonus', 'restricted_stock_deferred', 'deferred_income', 
 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 
 'long_term_incentive', 'restricted_stock', 'director_fees']
email_features = ['to_messages', 'from_poi_to_this_person', 
'from_messages', 'from_this_person_to_poi', 'shared_receipt_with_poi']
features_list = ['poi'] + ['exercised_stock_options', 'deleted_messages'] 
# You will need to use more features

from sklearn.feature_selection import SelectKBest, SelectPercentile, f_classif

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
data_dict.pop("TOTAL", 0)
data_dict.pop("THE TRAVEL AGENCY IN THE PARK", 0)
data_dict.pop("BELFER ROBERT", 0)
data_dict.pop("BHATNAGAR SANJAY", 0)

### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
data_dict = add_deleted_items(data_dict)
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

clf = SVC()



### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
from sklearn.cross_validation import train_test_split

features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.25, random_state=42)


clf.fit(features_train, labels_train)
#print "feature importances: ", clf.feature_importances_
print "score: ", clf.score(features_test, labels_test)



### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)