from .SearchEngineParser import SearchEngineParser
from ..FileDownload import FileDownload
from BeautifulSoup import BeautifulSoup

class GoogleParser(SearchEngineParser):
	'''
	A parser for google search Engine
	'''

	def google_url(self,song_name,website):
		''' It will return the google url to be searched'''
		name='+'.join(song_name)
		prefix='https://www.google.co.in/search?q='	
		website=website.split(" ")
		suffix='+'.join(website)
		url=prefix+name+suffix
		#print url
		return url

	def parse_google(self,html):
		'''It will parse google html response
			and return the first url
		 '''
		soup = BeautifulSoup(html)
		href=soup.find('div','g').find('a').get('href')
		href_list=href.split('&')
		download_url=href_list[0]
		download_url=download_url.strip()
		download_url=download_url.replace('/url?q=','')
		return download_url


	def Parse(self,song_name,website):
		'''
		song_name is a list of strings
		website is a string
		It will return the url from where music file needs to be downloaded
		'''
		url_to_be_parsed=self.google_url(song_name,website)
		file_download=FileDownload()
		html=file_download.get_html_response(url_to_be_parsed)
		website_url=self.parse_google(html)
		return website_url



