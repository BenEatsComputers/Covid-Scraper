import requests
import bs4
import time

site = requests.get("https://www.worldometers.info/coronavirus/")

x = 1

while True:
	site_src = site.text

	soup = bs4.BeautifulSoup(site_src, "lxml")

	title = soup.title.text

	cases = title[27:38]

	with open(f"covidData/week{x}report.txt", "w+") as f:
		f.write(f"Cases Worldwide: {cases}")

	x += 1
	
	time.sleep(604800)