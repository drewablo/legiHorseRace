from bs4 import BeautifulSoup
import urllib2
import re
from sys import exit

def name():
	nameID = {1911: ['pamela j. althoff'],2018:['jason a. barickman'],2022:['jennifer bertino-tarrant'],2020:['daniel biss'],1948:	['tim bivins'],1880:['william e. brady'], 2023:['melinda bush'], 1864:['james f. clayborne, jr.'], 1899:['jacqueline y. collins'], 2024: ['michael connelly'], 1865: ['john j. cullerton'],2025:['thomas cullerton'],2026:['bill cunningham'],1930:	['william delgado'],1866:['kirk w. dillard'],1960:['dan duffy'],1914:['gary forby'],1937:['michael w. frerichs'],1909:['william r. haine'],1905:['don harmon'],2027:['napoleon harris, iii'],2028:['michael e. hastings'],1936:	['linda holmes'],1910:['mattie hunter'],1961:['toi w. hutchinson'],1924:['mike jacobs'],1963:	['emil jones, iii'],1938:['david koehler'],1935:['dan kotowski'],1999:['darin m. lahood'],1997:	['steven m. landek'],1869:['kimberly a. lightford'],1870:['terry link'],1871:['david s. luechtefeld'],2029: ['andy manar'],1902:['iris y. martinez'],1995:['wm. sam mccann'],1964:	['kyle mccarter'],2030:	['karen mcconnaughay'],2010:['pat mcguire'],2031:['julie a. morrison'],1970:['john g. mulroe'],1872:['antonio munoz'],1934:['matt murphy'],1933: ['michael noland'],2032: ['jim oberweis'],1873: ['christine radogno'],1917: ['kwame raoul'],1975: ['sue rezin'],1908:['dale a. righter'],2033:['chapin rose'],1897: ['martin a. sandoval'],1874:	['ira i. silverstein'],2034:['steve stadelman'],1947: ['heather a. steans'],1906: ['john m. sullivan'],1875:['dave syverson'],1876:	['donne e. trotter'],2035:['patricia van pelt']}
	return nameID
	
def main():
	links = []
	id = []
	x=0
	url = urllib2.urlopen("http://www.ilga.gov/senate")
	content = url.read()
	soup = BeautifulSoup(content)
	for a in soup.findAll('a',href=True):
		if re.findall('SenatorBills', a['href']):
			l = ("http://www.ilga.gov/senate/" + a['href']+'&Primary=True')
			links.append(str(l))
			id.append(re.findall('\d+', links[x]))
			x+=1
			new_id = [val for subl in id for val in subl]
			new_id = map(int, new_id)
	dirt = zip(new_id,links)
	directory = dict(dirt)
	return directory
	
def ask_name (nameID):
	member = str(raw_input("Who are you looking for ").lower())
	if member == 'exit':
		exit(0)
	else:
		for nameIDkey, value in nameID.items():
			for v in value:
				if member in v:
					return nameIDkey
		
def individual(directory,nameIDkey):
	legisl = directory.get(nameIDkey)
	if legisl is None:
		print "Legislator does not exist"
	else:
		url2 = urllib2.urlopen(directory[nameIDkey])
		content2 = url2.read()
		soup2 = BeautifulSoup(content2)
		table2 = soup2.find('table', cellpadding=3)
		for item in table2.findAll('tr')[1:]:
				col = item.findAll('td')
				sponsor = col[1].string
				last_action = col[4].string
				sponsor = sponsor.encode('ascii','ignore')
				#link = re.findall(r'(http?://\S+)',links)
				bill = col[0].string
				if re.findall('Public Act', last_action):
					if (col[0].string is None) or (sponsor is None):
						print 'error'
					else:
						print bill+' '+sponsor


while True:
	print "Search by either first or last name, but not both"
	individual(main(),ask_name(name()))	
