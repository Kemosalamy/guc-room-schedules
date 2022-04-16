#Script which scrapes the initial request to find out the viewstates and schedule IDs
import urllib.parse
import re

pagefile = open("mainpage.html","r")
page = pagefile.read()

open('ids.txt', 'w').close() #Clearing file
idfile = open("ids.txt", "a")

open('headers.txt', 'w').close()
headerfile = open("headers.txt", 'a')

#Get the list of IDs
idre = '''<option value\="(.*?)\">'''
idmatch = re.findall(idre,page)
for id in idmatch:
    idfile.write(id + "\n")

idfile.close()

#Get the viewstates and event validation
viewstatere='''id="__VIEWSTATE" value="(.*)" \/>'''
viewstategeneratorre='''id="__VIEWSTATEGENERATOR" value="(.*)" \/>'''
eventvalidationre='''id="__EVENTVALIDATION" value="(.*)" \/>'''

viewstatematch = re.findall(viewstatere,page)
viewstategeneratormatch = re.findall(viewstategeneratorre,page)
eventvalidationmatch = re.findall(eventvalidationre,page)

hdrcontent = "__EVENTTARGET=scdTpLst&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=" + urllib.parse.quote(viewstatematch[0], safe='')
hdrcontent += "&__VIEWSTATEGENERATOR=" +  urllib.parse.quote(viewstategeneratormatch[0], safe='')
hdrcontent += "&__EVENTVALIDATION=" + urllib.parse.quote(eventvalidationmatch[0], safe='')

headerfile.write(hdrcontent)
headerfile.close()

pagefile.close()
