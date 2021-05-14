
# No other modules apart from 'bs4' and 'requests' need to be imported
# as they aren't required to solve the assignment

# Import required module/s
from bs4 import BeautifulSoup
import requests


def getUserName(url_website, full_name):
	"""Gets the username from a website of the person whose full name is provided as input.

	Parameters
	----------
	url_website : str
		URL of website to scrape
	full_name : str
		Full name of person whose username is to be returned by scraping the given website

	Returns
	-------
	str
		Username of person for the provided Full name
	
	Example
	-------
	>>> url_website = "https://www.cse.iitb.ac.in/archive/page222?batch=MTech1"
	>>> full_name = "PRIYANSH KIMTEE"
	>>> getUserName(url_website, full_name)
	priyansh

	>>> url_website = "https://www.cse.iitb.ac.in/archive/page222?batch=MTech1"
	>>> full_name = "AKASH VERMA"
	>>> getUserName(url_website, full_name)
	Full Name does not exist on website
	"""

	username = ""

	##############	ADD YOUR CODE HERE	##############
	
	website_url =requests.get(url_website).text
	soup=BeautifulSoup(website_url ,'lxml')
	#print(soup.prettify)	
	
	for i in soup.find_all('tr'):
		for j in i.find_all('td'):
			print(j.b.string)
	
 	

	##################################################

	return username


if __name__ == "__main__":
	"""Main function, code begins here
	"""
	url_website = "https://www.cse.iitb.ac.in/archive/page222?batch=MTech1"
	full_name = "A.V.S BHARADWAJ"

	username = getUserName(url_website, full_name)
	print("The username of " + full_name + " is: " + username)
