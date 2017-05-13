class MusicWebsiteParser:
	'''
	Base class for music website parsers
	Every parser needs to implement it

	'''
	def Parse(self,url):
		'''It will parse the html page specified by url
		and return the resource url from where the music file needs to be downloaded
		'''
		raise NotImplementedError('You must implement the Parse() method yourself!')