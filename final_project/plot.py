import os
import sys
import pickle
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

financial_features = ['salary', 'deferral_payments', 'total_payments',
 'loan_advances', 'bonus', 'restricted_stock_deferred', 'deferred_income', 
 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 
 'long_term_incentive', 'restricted_stock', 'director_fees']
email_features = ['to_messages', 'from_poi_to_this_person', 
'from_messages', 'from_this_person_to_poi', 'shared_receipt_with_poi']
features_list = ['poi'] + ['exercised_stock_options', 'total_payments'] 

def adddel(data_dict):
	basepath = 'D:\\dev\\ud120-projects\\maildir'
	macpath = '/users/Robert/dev/ud120-projects-master/maildir'

	for p in data_dict:
		name = p.split()
		d = name[0] + "-" + name[1][0]
		d = d.lower()

		deleted_items = os.path.join(macpath, d + '\\deleted_items')
		try:
		    os.chdir(deleted_items)
		except:
		    data_dict[p]['deleted_messages'] = 'NaN'
		else:
			delm = len(os.listdir(os.getcwd()))
			data_dict[p]['deleted_messages'] = len(os.listdir(os.getcwd()))

	return data_dict

def minMaxFeature(d,f):
	a = []
	for p in d:
		n = d[p][f]
		if d[p][f] == 'NaN': n = 0
		a.append(n)
	return [min(a), max(a)]

def scaledMinMax(n, min, max):
	return (n - min) / (max - min)


## Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

data_dict.pop("TOTAL", 0)
data_dict.pop("THE TRAVEL AGENCY IN THE PARK", 0)

data_dict = adddel(data_dict)

esomm = minMaxFeature(data_dict, 'exercised_stock_options')
tsvmm = minMaxFeature(data_dict, 'total_stock_value')

for d in data_dict:
	poi = data_dict[d]['poi']

	eso = data_dict[d]['exercised_stock_options']
	tsv = data_dict[d]['total_stock_value']
	rs = data_dict[d]['restricted_stock']
	rsd = data_dict[d]['restricted_stock_deferred']

	if poi:
		print data_dict[d]["email_address"]


	x, y = eso, tsv
	

	if x == 'NaN' or x == 0: next #x = 0
	if y == 'NaN' or y == 0: next #y = 0


	if poi:
		color = "ro"
	else:
		next
		color = "bo"

	plt.annotate(d, xy=(x,y), xytext=(x,y))

	#pca = PCA(n_components=1)
	#pca.fit(data)
	#transformed = pca.transform(data)
 	plt.plot(x, y, color)


plt.xlabel("x")
plt.ylabel("y")

plt.show()
