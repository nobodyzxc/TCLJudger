#!/usr/bin/env python
import urllib2
from HTMLParser import HTMLParser
####################### SETTING ########################

status_url = "http://judge.nccucs.org/RealtimeStatus"

####################### IMPLEMENT ######################

class rsParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.getData = False
        self.lastTag = ""
        self.probID = ""
    def handle_starttag(self , tag , attrs):
        self.lastTag = tag
        if tag == "td":
            for(attr , value) in attrs:
                if attr == 'id':
                    print value , " "  , 
                if attr == 'width' and value == '12%':
                    self.getData = True
                if attr == 'width' and value == '40%':
                    self.probID = True
        if tag == "a":
            if('title' , '') in attrs:
                for(attr , value) in attrs:
                    if attr == 'href':
                        if self.probID == True:#show probID
                            print "%5s " %(value.split('=')[-1]) , " " ,
                        else:#show name
                            print "%15s" %(value.split('=')[-1]) , " " , 
    def handle_data(self , data):
        if self.getData == True:
            if self.lastTag == 'td':
                if data.strip() != "":
                    print data.strip() , " " ,
            if self.lastTag == 'span':
                if data.strip() != "":
                    print data.strip() , " " , 
    def handle_endtag(self , tag):
        if tag == 'td' and self.getData == True:
            print ""
            self.getData = False
        if tag == 'td' and self.probID == True:
            self.probID = False

#######################    MAIN   ######################

if __name__ == '__main__':
    req = urllib2.Request(status_url)
    response = urllib2.urlopen(req)
    page = response.read() #Get html file
    RSP = rsParser()
    RSP.feed(page)
