from bs4 import BeautifulSoup
import urllib2
import re
import csv

def stew(site):
	url = urllib2.urlopen(site)
	content = url.read()
	soup = BeautifulSoup(content)
	return soup

def main(soup):
	links = []
	x=0
	soup
	append1 = links.append
	table = soup.find('table', cellpadding=3)
	for a in soup.findAll('a',href=True):
		if re.findall('Bills', a['href']):
			l = (site + a['href']+'&Primary=True')
			append1(str(l))
			x+=1
	return links
site = 'http://www.ilga.gov/house/'
links = main(stew(site))
chamber_abbr = 'HB'
master_list = []
for link in links:
	soup = stew(link)
	table = soup.find('table', cellpadding=3)
	for item in table.findAll('tr')[1:]:
		col = item.findAll('td')
		bill = col[0].string
		sponsor = col[1].string
		sponsor = sponsor.encode('ascii','replace')
		last_action = col[4].string
		last_action_date = col[5].string
		for z in re.findall('2014', last_action_date):
			for q in re.findall(chamber_abbr, bill):
				master_list.append([sponsor, bill, last_action, last_action_date])	
				with open('house.csv', 'wb') as f:
					writer = csv.writer(f)
					writer.writerows(master_list)
site = 'http://www.ilga.gov/senate/'
links = main(stew(site))
chamber_abbr = 'SB'
master_list = []
for link in links:
	soup = stew(link)
	table = soup.find('table', cellpadding=3)
	for item in table.findAll('tr')[1:]:
		col = item.findAll('td')
		bill = col[0].string
		sponsor = col[1].string
		sponsor = sponsor.encode('ascii','replace')
		last_action = col[4].string
		last_action_date = col[5].string
		for z in re.findall('2014', last_action_date):
			for q in re.findall(chamber_abbr, bill):
				master_list.append([sponsor, bill, last_action, last_action_date])	
				with open('senate.csv', 'wb') as f:
					writer = csv.writer(f)
					writer.writerows(master_list)		
