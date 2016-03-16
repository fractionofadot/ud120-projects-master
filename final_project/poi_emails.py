import os

poi = ["Lay Kenneth",
"Skilling Jeffrey",
"Howard Kevin",
"Krautz Michael",
"Yeager Scott",
"Hirko Joseph",
"Shelby Rex",
"Bermingham David",
"Darby Giles",
"Mulgrew Gary",
"Bayley Daniel",
"Brown James",
"Furst Robert",
"Fuhs William",
"Causey Richard",
"Calger Christopher",
"DeSpain Timothy",
"Hannon Kevin",
"Koenig Mark",
"Forney John",
"Rice Kenneth",
"Rieker Paula",
"Fastow Lea",
"Fastow Andrew",
"Delainey David",
"Glisan Ben",
"Richter Jeffrey",
"Lawyer Larry",
"Belden Timothy",
"Kopper Michael",
"Duncan David",
"Bowen Raymond",
"Colwell Wesley",
"Boyle Dan",
"Loehr Christopher"]

poi_emails = ["kevin.hannon@enron.com",
"wes.colwell@enron.com",
"paula.rieker@enron.com",
"michael.kopper@enron.com",
"rex.shelby@enron.com",
"david.delainey@enron.com",
"kenneth.lay@enron.com",
"raymond.bowen@enron.com",
"tim.belden@enron.com",
"andrew.fastow@enron.com",
"christopher.calger@enron.com",
"ken.rice@enron.com",
"jeff.skilling@enron.com",
"scott.yeager@enron.com",
"joe.hirko@enron.com",
"mark.koenig@enron.com",
"richard.causey@enron.com",
"ben.glisan@enron.com"]

prefix = "emails_by_address/from_"  
suffix = ".txt"

for p in poi_emails:
	email = prefix  + p + suffix
	try:
		with open(email, "r") as file:
			print "yes", email
	except Exception as inst:
		print "no", email

# for p in poi:
# 	last, first = p.split()
# 	emails = prefix + first.lower() + "." + last.lower() + suffix
# 	path = os.path.normcase(emails)
# 	try:
# 		with open(path, "r") as allemails:
# 			print first, last
# 	except Exception as inst:
# 		print "no"
