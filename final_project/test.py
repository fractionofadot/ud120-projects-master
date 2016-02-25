#!/usr/bin/python

import os
import sys
import pickle

## Load the dictionary containing the dataset
# with open("final_project_dataset.pkl", "r") as data_file:
#     data_dict = pickle.load(data_file)

# data_dict.pop("TOTAL", 0)
# data_dict.pop("THE TRAVEL AGENCY IN THE PARK", 0)


def add_deleted_items(data_dict):
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

def writecsv():
	features = ['salary', 'deferral_payments', 'total_payments',
	 'loan_advances', 'bonus', 'restricted_stock_deferred', 'deferred_income', 
	 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 
	 'long_term_incentive', 'restricted_stock', 'director_fees']

	sys.stdout.write("name,")
	for f in sorted(features):
		sys.stdout.write(str(f))
		sys.stdout.write(",")
	sys.stdout.write("\n")

	for d in sorted(data_dict):
		p = data_dict[d]
		sys.stdout.write(str(d))
		sys.stdout.write(",")
		for f in sorted(features):
			sys.stdout.write(str(p[f]))
			sys.stdout.write(",")
		sys.stdout.write("\n")
			
		# print "%s, %s, %s, %s, %s" % (d, p['salary'], p['bonus'], p['long_term_incentive'], p['deferred_income'], p[''])

