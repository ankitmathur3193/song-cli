from MusicWebsiteParser.MusicWebsiteFactory import MusicWebsiteFactory
from SearchEngineParser.SearchEngineFactory import SearchEngineFactory

class FactoryProducer:

	 def getFactory(self,factory_name):
	 	if factory_name.lower()=="search engine parser factory":
	 		return SearchEngineFactory()
	 	elif factory_name.lower()=="music website parser factory":
	 		return MusicWebsiteFactory()
	 	else:
	 		raise NotImplementedError("%s not implemented"%factory_name)		
	