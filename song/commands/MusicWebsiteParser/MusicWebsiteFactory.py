from .MrJattParser import MrJattParser

class MusicWebsiteFactory:

	def getParser(self,parser_name):
		if parser_name.lower()=="mr jatt":
			return MrJattParser()
		else:
			raise NotImplementedError('parser for this music website not implemented')	