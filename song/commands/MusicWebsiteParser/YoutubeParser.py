from .MusicWebsiteParser import MusicWebsiteParser
from ..FileDownload import FileDownload
from BeautifulSoup import BeautifulSoup

class YoutubeParser(MusicWebsiteParser):

	def Parse(self,song_name):
		song_name = '+'.join(song_name)
		url="https://www.youtube.com/results?search_query="
		url=url+song_name
		file_download=FileDownload()
		html=file_download.get_html_response(url)
		soup=BeautifulSoup(html)
		download_url = soup.find('a',attrs={'class':'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link '})
		temp_url='https://www.youtube.com'
		final_url=temp_url+download_url.get('href')
		return final_url

		