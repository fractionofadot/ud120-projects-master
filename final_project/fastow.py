#From fastow
import pickle
import os

## Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

data_dict.pop("TOTAL", 0)
data_dict.pop("THE TRAVEL AGENCY IN THE PARK", 0)

pois = ["Lay Kenneth",
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

everybody = ["METTS MARK",
"BAXTER JOHN C",
"ELLIOTT STEVEN",
"CORDES WILLIAM R",
"HANNON KEVIN P",
"MORDAUNT KRISTINA M",
"MEYER ROCKFORD G",
"MCMAHON JEFFREY",
"HORTON STANLEY C",
"PIPER GREGORY F",
"HUMPHREY GENE E",
"UMANOFF ADAM S",
"BLACHMAN JEREMY M",
"SUNDE MARTIN",
"GIBBS DANA R",
"LOWRY CHARLES P",
"COLWELL WESLEY",
"MULLER MARK S",
"JACKSON CHARLENE R",
"WESTFAHL RICHARD K",
"WALTERS GARETH W",
"WALLS JR ROBERT H",
"KITCHEN LOUISE",
"CHAN RONNIE",
"BELFER ROBERT",
"SHANKMAN JEFFREY A",
"WODRASKA JOHN",
"BERGSIEKER RICHARD P",
"URQUHART JOHN A",
"BIBI PHILIPPE A",
"RIEKER PAULA H",
"WHALEY DAVID A",
"BECK SALLY W",
"HAUG DAVID L",
"ECHOLS JOHN B",
"MENDELSOHN JOHN",
"HICKERSON GARY J",
"CLINE KENNETH W",
"LEWIS RICHARD",
"HAYES ROBERT E",
"MCCARTY DANNY J",
"KOPPER MICHAEL J",
"LEFF DANIEL P",
"LAVORATO JOHN J",
"BERBERIAN DAVID",
"DETMERING TIMOTHY J",
"WAKEHAM JOHN",
"POWERS WILLIAM",
"GOLD JOSEPH",
"BANNANTINE JAMES M",
"DUNCAN JOHN H",
"SHAPIRO RICHARD S",
"SHERRIFF JOHN R",
"SHELBY REX",
"LEMAISTRE CHARLES",
"DEFFNER JOSEPH M",
"KISHKILL JOSEPH G",
"WHALLEY LAWRENCE G",
"MCCONNELL MICHAEL S",
"PIRO JIM",
"DELAINEY DAVID W",
"SULLIVAN-SHAKLOVITZ COLLEEN",
"WROBEL BRUCE",
"LINDHOLM TOD A",
"MEYER JEROME J",
"LAY KENNETH L",
"BUTTS ROBERT H",
"OLSON CINDY K",
"MCDONALD REBECCA",
"CUMBERLAND MICHAEL S",
"GAHN ROBERT S",
"MCCLELLAN GEORGE",
"HERMANN ROBERT J",
"SCRIMSHAW MATTHEW",
"GATHMANN WILLIAM D",
"HAEDICKE MARK E",
"BOWEN JR RAYMOND M",
"GILLIS JOHN",
"FITZGERALD JAY L",
"MORAN MICHAEL P",
"REDMOND BRIAN L",
"BAZELIDES PHILIP J",
"BELDEN TIMOTHY N",
"DURAN WILLIAM D",
"THORN TERENCE H",
"FASTOW ANDREW S",
"FOY JOE",
"CALGER CHRISTOPHER F",
"RICE KENNETH D",
"KAMINSKI WINCENTY J",
"LOCKHART EUGENE E",
"COX DAVID",
"OVERDYKE JR JERE C",
"PEREIRA PAULO V. FERRAZ",
"STABLER FRANK",
"SKILLING JEFFREY K",
"BLAKE JR. NORMAN P",
"SHERRICK JEFFREY B",
"PRENTICE JAMES",
"GRAY RODNEY",
"PICKERING MARK R",
"NOLES JAMES L",
"KEAN STEVEN J",
"FOWLER PEGGY",
"WASAFF GEORGE",
"WHITE JR THOMAS E",
"CHRISTODOULOU DIOMEDES",
"ALLEN PHILLIP K",
"SHARP VICTORIA T",
"JAEDICKE ROBERT",
"WINOKUR JR. HERBERT S",
"BROWN MICHAEL",
"BADUM JAMES P",
"HUGHES JAMES A",
"REYNOLDS LAWRENCE",
"DIMICHELE RICHARD G",
"BHATNAGAR SANJAY",
"CARTER REBECCA C",
"BUCHANAN HAROLD G",
"YEAP SOON",
"MURRAY JULIA H",
"GARLAND C KEVIN",
"DODSON KEITH",
"YEAGER F SCOTT",
"HIRKO JOSEPH",
"DIETRICH JANET R",
"DERRICK JR. JAMES V",
"FREVERT MARK A",
"PAI LOU L",
"BAY FRANKLIN R",
"HAYSLETT RODERICK J",
"FUGH JOHN L",
"FALLON JAMES B",
"KOENIG MARK E",
"SAVAGE FRANK",
"IZZO LAWRENCE L",
"TILNEY ELIZABETH A",
"MARTIN AMANDA K",
"BUY RICHARD B",
"GRAMM WENDY L",
"CAUSEY RICHARD A",
"TAYLOR MITCHELL S",
"DONAHUE JR JEFFREY M",
"GLISAN JR BEN F"]

dpois = []

for d in data_dict:
	if data_dict[d]['poi']:
		name = str.split(d)
		dpois.append(name[0])

print len(pois), len(dpois)

nomatch = []

match = 0

for p in pois:
	p = str.upper(p)
	l, f = str.split(p)
	for d in dpois:
		if d == l:
			match = 1
			break
	if match:
		match = 0
	else:
		nomatch.append(l + " " + f)

print nomatch

def minMaxFeature(d,f):
	a = []
	for p in d:
		n = d[p][f]
		if d[p][f] == 'NaN': n = 0
		a.append(n)
	return [min(a), max(a)]

def maildir():
	outcasts = []
	included = []
	basepath = 'D:\\dev\\ud120-projects\\maildir'
	macpath = '/users/Robert/dev/ud120-projects-master/maildir'

	for p in data_dict:
		name = p.split()
		d = name[0] + "-" + name[1][0]
		d = d.lower()

		userdir = os.path.join(macpath, d)
		try:
		    os.chdir(userdir)
		except:
		    if data_dict[p]['poi']: outcasts.append(d)
		else:
			if data_dict[p]['poi']: included.append(d)

	return included

print maildir()

pois = []
nonpois = []

for p in data_dict:
	if data_dict[p]['poi']:
		pois.append(data_dict[p]['total_stock_value'])
	else:
		nonpois.append(p)


tsvmin, tsvmax = minMaxFeature(data_dict, 'total_stock_value')
#print len(pois), len(nonpois)

import matplotlib.pyplot as plt
plt.plot(pois, "ro")
plt.ylabel('some numbers')
#plt.show()








