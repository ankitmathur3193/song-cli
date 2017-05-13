import requests
import os


class FileDownload:

	def get_html_response(self,url):
		'''It will download the html page specified by url and return the html response '''
		print "Downloading page %s .."%url
		try:
			response=requests.get(url,timeout=50)
		except requests.exceptions.SSLError:
			try:
				response=requests.get(url,verify=False,timeout=50)
			except requests.exceptions.RequestException as e:
				print e
				quit()
		except requests.exceptions.RequestException as e:
			print e	
			quit()

		return response.content	


	def file_download_using_requests(self,url):
		'''It will download file specified by url using requests module'''
		file_name=url.split('/')[-1]
		print 'Downloading file %s '%file_name
		#print 'Downloading from %s'%url
		try:
			r=requests.get(url,stream=True,timeout=50)
		except requests.exceptions.SSLError:
			try:
				response=requests.get(url,stream=True,verify=False,timeout=50)
			except requests.exceptions.RequestException as e:
				print e
				quit()		
		except requests.exceptions.RequestException as e:
				print e
				quit()	

		total_size=float(r.headers['Content-Length'])/(1024*1024)
		print 'Total size of file to be downloaded %.2f MB '%total_size
		total_downloaded_size=0.0
		with open(file_name,'wb') as f:
			for chunk in r.iter_content(chunk_size=1*1024*1024):
				if chunk:
					size_of_chunk=float(len(chunk))/(1024*1024)
					total_downloaded_size+=size_of_chunk
					print '{0:.0%} Downloaded'.format(total_downloaded_size/total_size)
					f.write(chunk)

		print 'Downloaded file %s '%file_name


	def file_download_using_wget(self,url):
		'''It will download file specified by url using wget utility of linux '''
		file_name=url.split('/')[-1]
		print 'Downloading file %s '%file_name
		command='wget -c --read-timeout=50 --tries=3 -q --show-progress --no-check-certificate '
		url='"'+url+'"'
		command=command+url
		os.system(command)						
			