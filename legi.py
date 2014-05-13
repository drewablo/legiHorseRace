from bs4 import BeautifulSoup
import urllib2
import re
from sys import exit

def name():
	nameID = {1911: ['PAMELA ALTHOFF'],2018:['JASON BARICKMAN'],2022:['JENNIFER BERTINO-TARRANT'],2020:['DANIEL BISS'],1948:	['TIM BIVINS'],1880:['WILLIAM BRADY'], 2023:['MELINDA BUSH'], 1864:['JAMES CLAYBORNE, JR.'], 1899:['JACQUELINE COLLINS'], 2024: ['MICHAEL CONNELLY'], 1865: ['JOHN CULLERTON'],2025:['THOMAS CULLERTON'],2026:['BILL CUNNINGHAM'],1930:	['WILLIAM DELGADO'],1866:['KIRK DILLARD'],1960:['DAN DUFFY'],1914:['GARY FORBY'],1937:['MICHAEL FRERICHS'],1909:['WILLIAM HAINE'],1905:['DON HARMON'],2027:['NAPOLEON HARRIS, III'],2028:['MICHAEL HASTINGS'],1936:	['LINDA HOLMES'],1910:['MATTIE HUNTER'],1961:['TOI HUTCHINSON'],1924:['MIKE JACOBS'],1963:	['EMIL JONES, III'],1938:['DAVID KOEHLER'],1935:['DAN KOTOWSKI'],1999:['DARIN LAHOOD'],1997:	['STEVEN LANDEK'],1869:['KIMBERLY LIGHTFORD'],1870:['TERRY LINK'],1871:['DAVID LUECHTEFELD'],2029: ['ANDY MANAR'],1902:['IRIS MARTINEZ'],1995:['WM. SAM MCCANN'],1964:	['KYLE MCCARTER'],2030:	['KAREN MCCONNAUGHAY'],2010:['PAT MCGUIRE'],2031:['JULIE MORRISON'],1970:['JOHN MULROE'],1872:['ANTONIO MUNOZ'],1934:['MATT MURPHY'],1933: ['MICHAEL NOLAND'],2032: ['JIM OBERWEIS'],1873: ['CHRISTINE RADOGNO'],1917: ['KWAME RAOUL'],1975: ['SUE REZIN'],1908:['DALE RIGHTER'],2033:['CHAPIN ROSE'],1897: ['MARTIN SANDOVAL'],1874:	['IRA SILVERSTEIN'],2034:['STEVE STADELMAN'],1947: ['HEATHER STEANS'],1906: ['JOHN SULLIVAN'],1875:['DAVE SYVERSON'],1876: ['DONNE TROTTER'],2035:['PATRICIA VAN PELT']}
	return nameID
	
def main():
	links = []
	id = []
	x=0
	url = urllib2.urlopen("http://www.ilga.gov/senate")
	content = url.read()
	soup = BeautifulSoup(content)
	append1 = links.append
	append2 = id.append
	for a in soup.findAll('a',href=True):
		if re.findall('Bills', a['href']):
			l = ("http://www.ilga.gov/senate/" + a['href']+'&Primary=True')
			append1(str(l))
			append2(re.findall('\d+', links[x]))
			x+=1
			new_id = [val for subl in id for val in subl]
			new_id = map(int, new_id)
	dirct = zip(new_id,links)
	directory = dict(dirct)
	return directory
	
def ask_name (nameID):
	member = str(raw_input("Who are you looking for ").upper())
	for nameIDkey, value in nameID.items():
		for v in value:
			if member in v:
				return nameIDkey	
					
def individual(directory,nameIDkey):
	legisl = directory.get(nameIDkey)
	bill_count = 0
	if legisl is None:
		print "LEGISLATOR NOT FOUND"
	else:
		url = urllib2.urlopen(directory[nameIDkey])
		content = url.read()
		soup = BeautifulSoup(content)
		table = soup.find('table', cellpadding=3)
		la = str(raw_input('Public Act = p, Passed both chambers = bc, or Stuck in the system = r :'))
		for item in table.findAll('tr')[1:]:
				col = item.findAll('td')
				sponsor = col[1].string
				last_action = col[4].string
				sponsor = sponsor.encode('ascii','ignore')
				#link = re.findall(r'(http?://\S+)',links)
				bill = col[0].string
				if la == 'p':
					for x in re.findall('Public Act', last_action):
						if (col[0].string is None) or (sponsor is None):
							print 'error'
						else:
							bill_count+=1
							print bill+' '+sponsor	
				elif la == 'bc':
					for x in re.findall('Both', last_action):
						if (col[0].string is None) or (sponsor is None):
							print 'error'
						else:
							bill_count+=1
							print bill+' '+sponsor
				elif la == 'r':
					if re.findall('ferred', last_action):
						if (col[0].string is None) or (sponsor is None):
							print 'error'
						else:
							bill_count+=1
							print bill+' '+sponsor
				else:
					print 'Please enter either p, bc, or r'
					la = str(raw_input('Public Act = p, Passed both chambers = bc, or Stuck in the system = r :'))
	print 'BILLS FOUND: ',bill_count
	
print "Search by either first or last name, but not both"
while True:
	individual(main(),ask_name(name()))	
