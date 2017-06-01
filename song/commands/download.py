# skele/commands/download.py
"""The hello command."""


from json import dumps

from base import Base
from FactoryProducer import FactoryProducer
from FileDownload import FileDownload
class Download(Base):

    def run(self):
        name=self.options["TEXT"]
        download_all_flag = self.options["--download-all"]
        if self.options['-y'] == True:
            self.download_from_youtube(name)
        elif self.options['-d'] == True:
            self.download_from_mr_jatt(name,download_all_flag)
        elif self.options['-t'] == True:
            songfile = self.options["TEXTFILE"][0]
            #include for loop + code here to download files from a list
            with open(songfile) as f:
                content = f.readlines()
            content = [x.strip() for x in content]
            for ind in range(0, len(content)):
                self.download_from_youtube(content[ind].split())


    def download_from_youtube(self,name):
        factory = FactoryProducer()
        p = factory.getFactory("search engine parser factory")
        print "Download from youtube"
        q = factory.getFactory("music website parser factory")
        q = q.getParser("youtube")
        link = q.Parse(name)
        file_download=FileDownload()
        file_download.file_download_using_youtube_dl(link)


    def download_from_mr_jatt(self,name,flag):
        factory = FactoryProducer()
        p = factory.getFactory("search engine parser factory")
        p=p.getParser("google")
        website_url = p.Parse(name,"mr jatt")
        q = factory.getFactory("music website parser factory")
        q = q.getParser("mr jatt")
        download_url = q.Parse(website_url,name,flag)
        file_download=FileDownload()
        if flag == True:
            print "All songs will be downloaded for %s"%(' '.join(name))
            for url in download_url:
                print url[0],url[1]
                temp = q.Parse(url[0],url[1],False)
                file_download.file_download_cross_platform(temp)
        else:
            file_download.file_download_cross_platform(download_url)
