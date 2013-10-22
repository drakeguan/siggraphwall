# file: kesen_parser.py
# date: 08/25/2013
# author: Tzu-Mao Li
# description: This is a parser to fetch webpage information from Ke-Sen Huang's website and write to their bibtex files
#              Ke-Sen uses a anti-bot firewall to block http request, so it is better
#              to manually download the website and parse them.
#              I am not sure if it is legal to upload his webpage, so you may have to do it locally :p
#              To use the program, download the webpage (e.g. http://kesen.realtimerendering.com/sig2013.html )
#              to the same directory of this file with the bibtex folder, and execute it like this:
#              python kesen_parser.py sig2013.html siggraph_2013
#              where siggraph_2013 is the path point to the folder containing all the bibtex
#              The program will automatically find the bibtex for each entry in Ke-Sen's website and
#              write the website information.
#
#              The code is written in a rush and is a quick hack, so it can be super buggy, be careful!

import urllib2
import sys
import os
from HTMLParser import HTMLParser
from bibpy import bib

class KesenWebpageParser(HTMLParser):
    def __init__(self, bibtexDirectory):
        HTMLParser.__init__(self)
        self.paperModeFlag = False
        self.titleModeFlag = False
        self.currentTitle = ''
        self.currentUrl = ''
        self.bibtexDirectory = bibtexDirectory
        self.currentPath = bibtexDirectory + os.path.sep
        self.currentFile = None
        self.currentFileContent = ''
        self.currentRecords = None
        self.firstTag = True
    def handle_starttag(self, tag, attrs):
        if(tag == 'dt'):
            self.paperModeFlag = True
            self.firstTag = True
        elif(self.paperModeFlag and tag == 'b'):
            self.titleModeFlag = True
        elif(self.paperModeFlag and self.currentFile != None and tag == 'a'):
            dictAttr = dict(attrs)
            self.currentUrl = dictAttr['href']
        elif(self.paperModeFlag and self.currentUrl != '' and \
                self.currentFile != None and tag == 'img'):
            dictAttr = dict(attrs)
            try:
                alt = dictAttr['alt'].lower().replace(' ', '_')
                if self.firstTag and 'website' not in self.currentRecords:
                    self.currentFileContent.insert(\
                            len(self.currentFileContent)-1, \
                            '  ' + '{:<9}'.format('website') + ' = {' + self.currentUrl + '},\n')
                    self.firstTag = False
                if alt not in self.currentRecords:
                    self.currentFileContent.insert(\
                            len(self.currentFileContent)-1, \
                            '  ' + '{:<9}'.format(alt) + ' = {' + self.currentUrl + '},\n')
            except KeyError:
                pass

    def handle_endtag(self, tag):
        if(tag == 'dt'):
            self.paperModeFlag = False
            self.currentTitle = ''

            if self.currentFile != None:
                self.currentFile.close()
                #print self.currentFileContent
                self.currentFile = open(self.currentPath, 'w')
                self.currentFile.writelines(self.currentFileContent)
                self.currentFile.close()
                self.currentFile = None
                self.currentFileContent = ''
                self.currentRecords = None

        elif(self.paperModeFlag and tag == 'b'):
            if(self.titleModeFlag):
                self.titleModeFlag = False
                # do some string processing to conver title to file name
                title = self.currentTitle
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
                #print 'title:' + title
                self.currentPath = self.bibtexDirectory + os.path.sep + title + '.bib'
                try:
                    self.currentFile = open(self.currentPath, 'r')
                    bibParser = bib.Bibparser(bib.clear_comments(self.currentFile.read()))
                    bibParser.parse()
                    self.currentRecords = bibParser.records[bibParser.records.items()[0][0]]
                    self.currentFile.seek(0, 0)
                    self.currentFileContent = self.currentFile.readlines()
                    line = self.currentFileContent[len(self.currentFileContent)-2].rstrip()
                    if line[len(line)-1] != ',':
                        self.currentFileContent[len(self.currentFileContent)-2] = line + ',\n'
                except IOError:
                    pass

    def handle_data(self, data):
        if(self.titleModeFlag):
            self.currentTitle = self.currentTitle + data

def main():
    if len(sys.argv) < 3:
        print 'Usage: python kesen_parser.py [html_file] [bibtex_directory]\n'
        print 'e.g. python kesen_parser.py sig2013.html SIGGRAPH_2013'
        sys.exit(0)

    htmlFile = open(sys.argv[1], 'r')
    bibtexDirectory = sys.argv[2]

    content = htmlFile.read()
    parser = KesenWebpageParser(bibtexDirectory)
    parser.feed(content)

if __name__ == '__main__':
    main()


