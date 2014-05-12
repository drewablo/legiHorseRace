from bs4 import BeautifulSoup
import urllib2
import re

def name():
	nameID = {1897: ['Ira I. Silverstein'], 1899: ['Michael Connelly'], 1924: ['Emil Jones, III'], 1930: ['Kirk W. Dillard'], 1933: ['Jim Oberweis'], 1934:['Michael Noland'], 1935:['Darin M. LaHood'], 1936:['Mattie Hunter'], 1937:['William R.Haine'], 1938:['Dan Kotowski'], 2030:['Pat McGuire'], 1947:['John M. Sullivan'], 1948:['William E. Brady'], 2033:['Martin A. Sandoval'], 1960:['Gary Forby'], 1961:['Mike Jacobs'], 1963:['David Koehler'], 1964:['KarenMcConnaughay'], 1906:['Dave Syverson'], 1970:['Antonio Munoz'], 1975:['Dale A. Righter'], 1869:['Terry Link'], 1864:['Jacqueline Y. Collins'], 1865:['Thomas Cullerton'], 1866:['Dan Duffy'], 1995:['Kyle McCarter'], 1997:['Kimberly A. Lightford'], 1870:['David S. Luechtefeld'], 1999:['Steven M. Landek'], 1872:['Matt Murphy'], 1873:['Kwame Raoul'], 1874:['Steve Stadelman'], 1875:['Donne E. Trotter'], 1876:['Patricia Van Pelt'], 1880:['Melinda Bush'], 2010:['Julie A. Morrison'], 1871:['Andy Manar'], 2018:['Jennifer Bertino-Tarrant'], 2020:['Tim Bivins'], 2022:['Daniel Biss'], 2023:['James F. Clayborne, Jr.'], 2024:['John J. Cullerton'], 2025:['Bill Cunningham'], 2026:['William Delgado'], 2027:['Michael E. Hastings'], 2028:['Linda Holmes'], 2029:['Iris Y. Martinez'], 1902:['Wm. Sam McCann'], 2031: ['John G. Mulroe'], 2032:['Christine Radogno'], 1905:['Napoleon Harris, III'], 2034:['Heather A. Steans'], 1908:['Chapin Rose'], 1909:['Don Harmon'], 1910:['Toi W. Hutchinson'], 1911:['Pamela J. Althoff'], 1914:['Michael W. Frerichs'], 1917: ['Sue Rezin']}
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
	direct = dict(dirt)
	return direct
	
	
def ask_name (nameID):
	member = str(raw_input("Who are you looking for "))
	for nameIDkey, value in nameID.items():
		for v in value:
			if member in v:
				return nameIDkey
	
def individual(direct,nameIDkey):
	url2 = urllib2.urlopen(direct[nameIDkey])
	content2 = url2.read()
	soup2 = BeautifulSoup(content2)
	table2 = soup2.find('table', cellpadding=3)
	for item in table2.findAll('tr')[1:]:
			col = item.findAll('td')
			sponsor = col[1].string
			last_action = col[4].string
			sponsor = sponsor.encode('ascii','ignore')
			#link = re.findall(r'(http?://\S+)',links)
			if re.findall('Public Act', last_action):
				if (col[0].string is None) or (sponsor is None):
					print 'error'
					print col[0].string +' '+sponsor
				else:
					print col[0].string +' '+sponsor


individual(main(),ask_name(name()))
