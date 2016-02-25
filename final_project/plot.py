import os
import sys
import pickle
import numpy as np
import matplotlib.pyplot as plt

financial_features = ['salary', 'deferral_payments', 'total_payments',
 'loan_advances', 'bonus', 'restricted_stock_deferred', 'deferred_income', 
 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 
 'long_term_incentive', 'restricted_stock', 'director_fees']
email_features = ['to_messages', 'from_poi_to_this_person', 
'from_messages', 'from_this_person_to_poi', 'shared_receipt_with_poi']
features_list = ['poi'] + ['exercised_stock_options', 'total_payments'] 

def adddel(data_dict):
	basepath = 'D:\\dev\\ud120-projects\\maildir'

	for p in data_dict:
		name = p.split()
		d = name[0] + "-" + name[1][0]
		d = d.lower()

		deleted_items = os.path.join(basepath, d + '\\deleted_items')
		try:
		    os.chdir(deleted_items)
		except:
		    data_dict[p]['deleted_messages'] = 'NaN'
		else:
			delm = len(os.listdir(os.getcwd()))
			data_dict[p]['deleted_messages'] = len(os.listdir(os.getcwd()))

	return data_dict

## Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

data_dict.pop("TOTAL", 0)
data_dict.pop("THE TRAVEL AGENCY IN THE PARK", 0)

data_dict = adddel(data_dict)

for d in data_dict:
	eso = data_dict[d]['exercised_stock_options']
	tp = data_dict[d]['deleted_messages']
	poi = data_dict[d]['poi']
	if poi:
		color = "ro"
	else:
		color = "bo"

	plt.plot(eso, tp, color)


plt.xlabel("eso")
plt.ylabel("tp")
plt.show()
