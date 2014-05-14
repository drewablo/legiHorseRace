from bs4 import BeautifulSoup
import urllib2
import re
import itertools


def stew(site):
	url = urllib2.urlopen(site)
	content = url.read()
	soup = BeautifulSoup(content)
	return soup

def main(soup):
	links = []
	id = []
	x=0
	soup
	append1 = links.append
	append2 = id.append
	table = soup.find('table', cellpadding=3)
	for a in soup.findAll('a',href=True):
		if re.findall('Bills', a['href']):
			l = (site + a['href']+'&Primary=True')
			append1(str(l))
			append2(re.findall('\d+', links[x]))
			x+=1
			new_id = [val for subl in id for val in subl]
			new_id = map(int, new_id)
	dirct = zip(new_id,links)
	siteDirectory = dict(dirct)
	return siteDirectory, new_id

def names(new_id,soup):
	names = []
	soup
	table = soup.find('table', cellpadding=3)
	for item in table.findAll('tr')[2:]:
		col = item.findAll('td')
		nameID = col[0].string
		nameID = nameID.encode('ascii','replace')
		nameID = nameID.upper()
		names.append(nameID)
	combo = dict(itertools.izip(new_id,names))
	return combo

def search(combo):
	member = str(raw_input("Who are you looking for ").upper())
	for nameIDkey, value in combo.items():
		if member in value:
			return  nameIDkey	
	
def individual(siteDirectory,nameIDkey,soup):
	legisl = siteDirectory.get(nameIDkey)
	bill_count = 0
	if legisl is None:
		print "LEGISLATOR NOT FOUND"
	else:
		soup
		table = soup.find('table', cellpadding=3)
		la = raw_input('Public Act = P, Passed both chambers = BC, or Stuck in the system = R :').upper()
		for item in table.findAll('tr')[1:]:
				col = item.findAll('td')
				sponsor = col[1].string
				last_action = col[4].string
				sponsor = sponsor.encode('ascii','replace')
				#link = re.findall(r'(http?://\S+)',links)
				bill = col[0].string
				last_action_date = col[5].string
				if la == 'P':
					for z in re.findall('2014', last_action_date):					
						for y in re.findall(chamber_abbr, bill):
							for x in re.findall('Public Act', last_action):
								if (col[0].string is None) or (sponsor is None):
									print 'error'
								else:
									bill_count+=1
									print bill+' '+sponsor+' '+last_action_date
				elif la == 'BC':
					for z in re.findall('2014', last_action_date):					
						for y in re.findall(chamber_abbr, bill):				
							for x in re.findall('Both', last_action):
								if (col[0].string is None) or (sponsor is None):
									print 'error'
								else:
									bill_count+=1
									print bill, sponsor, last_action_date
				elif la == 'R':
					for z in re.findall('2014', last_action_date):					
						for y in re.findall(chamber_abbr, bill):				
							if re.findall('ferred', last_action):
								if (col[0].string is None) or (sponsor is None):
									print 'error'
								else:
									bill_count+=1
									print bill, sponsor, last_action_date
				else:
					print 'Please enter either p, bc, or r'
					la = raw_input('Public Act = P, Passed both chambers = BC, or Stuck in the system = R :').upper()
	print 'BILLS FOUND: ',bill_count

chamber=raw_input('House or Senate? ').upper()
if 'N' in chamber:
	site = 'http://www.ilga.gov/senate/'
	chamber_abbr = 'SB'
elif 'U' in chamber:
	site = 'http://www.ilga.gov/house/'
	chamber_abbr = 'HB'
else:
	print 'incorect selection'
print "Search by either first or last name"


while True:
	varD = stew(site)
	varA, varB = main(varD)
	varC = search(names(varB,varD))
	varE = stew(varA[varC])
	individual(varA,varC,varE)
