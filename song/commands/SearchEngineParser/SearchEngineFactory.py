from .GoogleParser import GoogleParser

class SearchEngineFactory:

	def getParser(self,parser_name):
		if parser_name.lower()=="google":
			return GoogleParser()
		else:
			raise NotImplementedError("parser for this search engine is not implemented yet")	