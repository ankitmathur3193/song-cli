from .MrJattParser import MrJattParser
from .YoutubeParser import YoutubeParser
class MusicWebsiteFactory:

	def getParser(self,parser_name):
		#print "fuck yeh"
		#print parser_name
		parser_name.lower()
		if parser_name.lower()=="mr jatt":
			return MrJattParser()
		elif parser_name.lower()=="youtube":	
			return YoutubeParser()
		else:
			raise NotImplementedError('parser for this music website not implemented')	