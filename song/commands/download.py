# skele/commands/download.py
"""The hello command."""
 
 
from json import dumps
 
from .base import Base
from .parse import Parse
 
 
class Download(Base):
    """Say hello, world!"""
 
    def run(self):
        #print 'Hello, world!'
        #print 'You supplied the following options:', dumps(self.options, indent=2, sort_keys=True)
        name=self.options["TEXT"]
        p=Parse(name)
       	download_url=p.get_download_url()
    	file_url=p.get_file_download_url(download_url)
    	p.file_download(file_url)
