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
        elif self.options['--ty'] == True: #determines if the '-yt' tag is there and returns object at that value
            songfile = self.options["SONGFILE"][0] #determines if options list has SONGFILE (name defined in cli.py in comments)
            #and takes the 0th element in the songfile array, which gives the actual file of the song, not just a list with one element
            with open(songfile) as f:
                content = f.readlines() #content is a list with lines of the textfile which should be song titles
            content = [x.strip() for x in content] #removes ending whitespaces and endlines
            for song in content:
                self.download_from_youtube(song.split()) #creates a list with each word of the song separated by spaces
                #this is done so YoutubeParser.py can concatenate them with '+' signs to generate a URL to search youtube


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
