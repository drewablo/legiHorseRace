from bs4 import BeautifulSoup
import urllib2
import re

def name():
	nameID = {1911: ['Pamela J. Althoff'],2018:	['Jason A. Barickman'],2022:['Jennifer Bertino-Tarrant'],2020:['Daniel Biss'],1948:	['Tim Bivins'],1880:['William E. Brady'], 2023:['Melinda Bush'], 1864:['James F. Clayborne, Jr.'], 1899:['Jacqueline Y. Collins'], 2024: ['Michael Connelly'], 1865: ['John J. Cullerton'],2025:['Thomas Cullerton'],2026:['Bill Cunningham'],1930:	['William Delgado'],1866:['Kirk W. Dillard'],1960:['Dan Duffy'],1914:['Gary Forby'],1937:['Michael W. Frerichs'],1909:['William R. Haine'],1905:['Don Harmon'],2027:['Napoleon Harris, III'],2028:['Michael E. Hastings'],1936:	['Linda Holmes'],1910:['Mattie Hunter'],1961:['Toi W. Hutchinson'],1924:['Mike Jacobs'],1963:	['Emil Jones, III'],1938:['David Koehler'],1935:['Dan Kotowski'],1999:['Darin M. LaHood'],1997:	['Steven M. Landek'],1869:['Kimberly A. Lightford'],1870:['Terry Link'],1871:['David S. Luechtefeld'],2029: ['Andy Manar'],1902:['Iris Y. Martinez'],1995:['Wm. Sam McCann'],1964:	['Kyle McCarter'],2030:	['Karen McConnaughay'],2010:['Pat McGuire'],2031:['Julie A. Morrison'],1970:['John G. Mulroe'],1872:['Antonio Munoz'],1934:['Matt Murphy'],1933: ['Michael Noland'],2032: ['Jim Oberweis'],1873: ['Christine Radogno'],1917: ['Kwame Raoul'],1975: ['Sue Rezin'],1908:['Dale A. Righter'],2033:['Chapin Rose'],1897: ['Martin A. Sandoval'],1874:	['Ira I. Silverstein'],2034:['Steve Stadelman'],1947: ['Heather A. Steans'],1906: ['John M. Sullivan'],1875:['Dave Syverson'],1876:	['Donne E. Trotter'],2035:['Patricia Van Pelt']}

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

while True:
	individual(main(),ask_name(name()))	
