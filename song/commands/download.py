# skele/commands/download.py
"""The hello command."""
 
 
from json import dumps
 
from .base import Base
from .FactoryProducer import FactoryProducer
from .FileDownload import FileDownload
class Download(Base):
    """Say hello, world!"""
 
    def run(self):
        #print 'Hello, world!'
        #print 'You supplied the following options:', dumps(self.options, indent=2, sort_keys=True)
        name=self.options["TEXT"]
        '''p=Parse(name)
       	download_url=p.get_download_url()
    	file_url=p.get_file_download_url(download_url)
    	p.file_download_using_wget(file_url)
    	'''
        factory = FactoryProducer()
    	p = factory.getFactory("search engine parser factory")
    	p=p.getParser("google")
    	website_url = p.Parse(name,"mr jatt")
    	q = factory.getFactory("music website parser factory")
    	q = q.getParser("mr jatt")
    	download_url = q.Parse(website_url,name)
        file_download=FileDownload()
    	file_download.file_download_using_wget(download_url)

