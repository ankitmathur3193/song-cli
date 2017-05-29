from .MusicWebsiteParser import MusicWebsiteParser
from ..FileDownload import FileDownload
from BeautifulSoup import BeautifulSoup
import re

class MrJattParser(MusicWebsiteParser):
	'''
	Parser for https://mr-jatt.com/

	'''
	

	def missing_schema(self,html,song_name):
		'''
		It will print the list of songs that can be downloaded
		'''
		#html=self.get_html_response(url)
		soup=BeautifulSoup(html)
		name=' '.join(song_name)
		print '%s not found'%name
		print "But you can download any of the following songs :"
		a_list=soup.findAll('a','touch')
		for x in xrange(len(a_list)-1):
			r=a_list[x]
			p=str(r)
			q=re.sub(r'<a.*/>|<span.*">|</span>|</a>|<a.*html">|<font.*">|</font>','',p)
			print q

	def list_of_all_href(self,html):
		'''
		It will return all hyper links found in the mr-jatt page for download
		'''	
		soup=BeautifulSoup(html)
		links=[]
		a_list=soup.findAll('a','touch')
		for x in xrange(len(a_list)-1):
			link = a_list[x].get('href')
			name = a_list[x]
			name = str(name)
			name=re.sub(r'<a.*/>|<span.*">|</span>|</a>|<a.*html">|<font.*">|</font>','',name)
			name=re.sub(r'^[0-9]+\.','',name)
			links.append([link,name])

		#quit()
		return links	

	def check_if_song_name(self,html):
		'''
		Returns true if user entered artist or movie name
		'''
		soup=BeautifulSoup(html)
		a_list=soup.findAll('a','touch')
		#print a_list
		text=[str(x) for x in a_list]
		text=''.join(text)
		text=text.lower()
		string1='download in 48 kbps'
		string2='download in 128 kbps'
		string3='download in 320 kbps'

		href=''
		if string3 in text:
			#print 'Downloading in 320 kbps'
			href=a_list[2].get('href')
			
		elif string2 in text:
			#print 'Downloading in 128 kbps'
			href=a_list[1].get('href')
			
		elif string1 in text:
			#print 'Downloading in 48 kbps'	
			href=a_list[0].get('href')
		else:
			return (True,'nothing')		

		return (False,href)
		
	def Parse(self,url,song_name,flag):
		'''
		It will the resource URL if song is found,
		Otherwise it will return the list of songs that can be downloaded
		'''
		file_download=FileDownload()
		html=file_download.get_html_response(url)
		if flag == False:
			soup=BeautifulSoup(html)
			a_list=soup.findAll('a','touch')
			#print a_list
			text=[str(x) for x in a_list]
			text=''.join(text)
			text=text.lower()
			string1='download in 48 kbps'
			string2='download in 128 kbps'
			string3='download in 320 kbps'

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
			else:
				self.missing_schema(html,song_name)
				quit()		

			return href 
		else:
			x,href=self.check_if_song_name(html)
			links = []
			if x==True:
				links=self.list_of_all_href(html)
			else:
				file_download=FileDownload()
				file_download.file_download_cross_platform(href)
				quit()	
			

			return links	
			

