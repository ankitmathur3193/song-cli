import requests
from BeautifulSoup import BeautifulSoup

class Parse:

	def __init__(self,name):
		self.name=name

	def get_html_response(self,url):
		#print "Downloading page %s .."%url
		response=requests.get(url)
		return response.content

	def parse_google(self,html):
		soup = BeautifulSoup(html)
		href=soup.find('div','g').find('a').get('href')
		href_list=href.split('&')
		download_url=href_list[0]
		download_url=download_url.strip()
		download_url=download_url.replace('/url?q=','')
		return download_url

	def google_url(self):
		name='+'.join(self.name)
		prefix='https://www.google.co.in/search?q='	
		suffix='+mr+jatt'
		url=prefix+name+suffix
		#print url
		return url

	def get_download_url(self):
		search_url=self.google_url()
		html=self.get_html_response(search_url)
		return self.parse_google(html)	

	def file_download(self,url):
		file_name=url.split('/')[-1]
		print 'Downloading file %s '%file_name
		#print 'Downloading from %s'%url
		r=requests.get(url,stream=True)
		total_size=float(r.headers['Content-Length'])/(1024*1024)
		total_downloaded_size=0.0
		with open(file_name,'wb') as f:
			for chunk in r.iter_content(chunk_size=1024*1024):
				if chunk:
					size_of_chunk=float(len(chunk))/(1024*1024)
					total_downloaded_size+=size_of_chunk
					print '{0:.0%} Downloaded'.format(total_downloaded_size/total_size)
					f.write(chunk)

		print 'Downloaded file %s '%file_name			


	def get_file_download_url(self,url):
		html=self.get_html_response(url)
		soup=BeautifulSoup(html)
		a_list=soup.findAll('a','touch')
		#print a_list
		text=[str(x) for x in a_list]
		text=''.join(text)
		string1='Download in 48 kbps'
		string2='Download in 128 kbps'
		string3='Download in 320 kbps'

		href=''
		if string3 in text:
			print 'Downloading in 320 kbps'
			href=a_list[2].get('href')
			
		elif string2 in text:
			print 'Downloading in 128 kbps'
			href=a_list[1].get('href')
			
		elif string1 in text:
			print 'Downloading in 48 kbps'	
			href=a_list[0].get('href')	

		return href 
			


		