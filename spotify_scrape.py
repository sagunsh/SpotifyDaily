# Import necessary libraries/modules
from bs4 import BeautifulSoup
import requests
from itertools import chain


def get_soup(url):
	''' Returns a soup object for a url '''

	retry = 0
	html = None
	while not html:
		if retry > 5:
			return None

		# Send request, try after 5 second if failed
		try:
			html = requests.get(url).content
			retry += 1
		except:
			print('Max retries exceeded, Waiting for 5 seconds...')
			time.sleep(5)
			continue

	soup = BeautifulSoup(html, 'html.parser')
	return soup


def get_spotify_list():
	''' Returns a list of list containing the spotify daily chart '''

	url = 'http://kworb.net/spotify/country/global_daily.html'
	soup = get_soup(url)
	data = []

	# Find the element to scrape and parse
	elems = soup.find('tbody').find_all('tr', recursive=False)
	for elem in elems:
		position = elem.find_all('td')[0].text
		artist = elem.find_all('td')[2].find_all('a')[0].text
		song = elem.find_all('td')[2].find_all('a')[1].text
		peak_position = elem.find_all('td')[4].text
		streams = elem.find_all('td')[6].text
		total_streams = elem.find_all('td')[-1].text
		row = [position, artist, song, peak_position, streams, total_streams]
		data.append(row)

	return data


def export_to_google(data, headers):
	''' Export data to google spreadsheets'''

	# Setting up google spreadsheet
	scope = ['https://spreadsheets.google.com/feeds']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client.json', scope)
	client = gspread.authorize(creds)
	sheet = client.open('Spotify')
	sheet1 = sheet.get_worksheet(1)

	# Insert header at the top of data
	data.insert(0, headers)
	num_of_cols = len(headers)

	# Flatten nested list
	data = list(chain.from_iterable(data))
	
	# Uploading data to google sheet
	cell_list = sheet1.range(1,1,len(data)/num_of_cols,num_of_cols)
	for i,cell in enumerate(cell_list):
		cell.value = data[i]

	sheet1.update_cells(cell_list)


if __name__ == '__main__':
	data = get_spotify_list()
	headers = ['Position', 'Artist', 'Song', 'Peak Position', 'Today Streams', 'Total Streams']
	export_to_google(data, headers)