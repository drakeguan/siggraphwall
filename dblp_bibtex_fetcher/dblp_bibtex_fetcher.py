# file: dblp_bibtex_fetcher.py
# date: 08/24/2013
# author: Tzu-Mao Li
# description: a parser to obtain the bibtex files from a dblp webpage
#              input the url(e.g. http://www.informatik.uni-trier.de/~ley/db/journals/tog/tog31.html )
#              and the program will automatically create folders and files under the current directory

import urllib2
import sys
import os
from HTMLParser import HTMLParser

bibtexBaseUrl = 'http://dblp.uni-trier.de/rec/bibtex/'

class DBLPBibtexParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.bibModeFlag = False
        self.bibtexContent = ''
    def handle_starttag(self, tag, attrs):
        if(tag == 'pre'):
            self.bibModeFlag = True
    def handle_endtag(self, tag):
        if(tag == 'pre'):
            self.bibModeFlag = False            
    def handle_data(self, data):
        if(self.bibModeFlag):
            self.bibtexContent = self.bibtexContent + data

class DBLPWebpageParser(HTMLParser):    
    def __init__(self):
        HTMLParser.__init__(self)
        self.headerModeFlag = False
        self.issueModeFlag = False
        self.titleModeFlag = False
        self.currentTitle = ''
    def handle_starttag(self, tag, attrs):        
        if(tag == 'header'):
            self.headerModeFlag = True
        elif(tag == 'h2'):
            self.issueModeFlag = True
        elif(tag == 'li'):
            dictAttr = dict(attrs)
            try:                
                if(dictAttr['class'] == 'entry article'):
                    articleId = dictAttr['id']
                    self.articleId = articleId
                    self.bibtexUrl = bibtexBaseUrl + articleId                    
            except KeyError:
                pass
        elif(tag == 'span'):
            dictAttr = dict(attrs)
            try:                
                if(dictAttr['class'] == 'title'):
                    self.titleModeFlag = True                 
            except KeyError:
                pass            
            
    def handle_endtag(self, tag):
        if(tag == 'header'):
            self.headerModeFlag = False
        elif(tag == 'h2'):
            self.issueModeFlag = False
        elif(tag == 'span'):
            if(self.titleModeFlag):
                self.titleModeFlag = False            
                # do some string processing to conver title to file name                
                title = self.currentTitle[0:len(self.currentTitle)-1] # remove period
                title = title.replace(' ', '_') # replace space by underline
                # remove special characters
                title = title.replace('\\', '')
                title = title.replace('/', '')            
                title = title.replace(':', '')
                title = title.replace('*', '')
                title = title.replace('?', '')
                title = title.replace('\"', '')
                title = title.replace('<', '')
                title = title.replace('>', '')
                title = title.replace('|', '')
                title = title.lower()
                print 'articleId:' + self.articleId
                print 'title:' + title
                self.currentTitle = ''

                # write bibtex to file
                f = open(self.currentPath + title + '.bib', 'w')
                response = urllib2.urlopen(self.bibtexUrl)
                content = response.read()
                parser = DBLPBibtexParser()
                parser.feed(content)
                f.write(parser.bibtexContent)
                f.close()
    def handle_data(self, data):
        if(self.issueModeFlag):
            dirName = data.replace(',', '').replace(' ', '_')
            if not os.path.isdir(dirName):
                os.mkdir(dirName)
            self.currentPath = dirName + os.path.sep
        elif(self.titleModeFlag):
            self.currentTitle = self.currentTitle + data


def main():
    if len(sys.argv) < 2:
        print 'Usage: python dblp_bibtex_fetcher.py [url]'
        sys.exit()

    for i in xrange(1, len(sys.argv)):        
        url = sys.argv[i]
        
        response = urllib2.urlopen(url)
        content = response.read()
        parser = DBLPWebpageParser()
        parser.feed(content)

if __name__ == '__main__':
    main()
