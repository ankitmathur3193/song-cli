class SearchEngineParser:
	'''It is the base class for Search Engine Parser
	Every Search Engine Parser needs to implement this class
	'''
	def Parse(self,song_name,website):
		'''
		It will search for "song_name website"  in the Search Engine results 
		and return the url of website
		'''
		raise NotImplementedError('You must implement the Parse() method yourself!')