import re

#WARNING - Horrible code inbound

schedules = open("schedules.html", "r")
content = schedules.read()

parsedsch = open("parsedschedules.txt", "w")

# DAILY regular expressions
# satre = '''<tr id="Xrw1">((?:.|\n)*?)<tr id="(?:XaltR2|Xrw2)">'''
# sunre = '''<tr id="Xrw2">((?:.|\n)*?)<tr id="(?:XaltR3|Xrw3)">'''
# monre = '''<tr id="Xrw3">((?:.|\n)*?)<tr id="(?:XaltR4|Xrw4)">'''
# tuere = '''<tr id="Xrw4">((?:.|\n)*?)<tr id="(?:XaltR5|Xrw5)">'''
# wedre = '''<tr id="Xrw5">((?:.|\n)*?)<tr id="(?:XaltR6|Xrw6)">'''
# thure = '''<tr id="Xrw6">((?:.|\n)*?)<tr id="(?:XaltR7|Xrw7)">'''

dayre1 = '''<tr id="Xrw'''
dayre2 = '''">((?:.|\n)*?)<tr id="(?:XaltR'''
dayre3 = '''|Xrw'''
dayre4 = ''')">'''
sltre = '''<TD width((?:.|\n)*?)<\/table>'''
infre = '''<tr>\n\t*<(?:.)*>(.*)<\/font><\/td>\n\t*<.*>(.*)<\/font><\/td>\n\t*<.*>((?:.|\n|)*?)<\/font>\n\t*<\/td>\n\t*<\/tr>'''

days = ["SAT","SUN","MON","TUE","WED","THU"]

for i in range(0,6):
    slot = 1
    day = days[i]
    dayre = dayre1 + str(i+1) + dayre2 + str(i+2) + dayre3 + str(i+2) + dayre4
    daymatch = re.findall(dayre,content)
    for i in daymatch:
        slot = 1
        sltmatch = re.findall(sltre,i)
        for j in sltmatch:
            cellmatch = re.findall(infre,j)
            for k in cellmatch:
                room = k[1].replace(" ","")
                subject = k[2].replace("\t","")
                subject = subject.replace("\n"," ")
                tutorial = k[0].replace("\t","")
                tutorial = tutorial.replace("\n", "")
                tutorial = tutorial.replace(" ","")
                parsedsch.write(room + " " + day + " " + str(slot) + " " + subject + tutorial + "\n")
            
            slot+=1

schedules.close()
parsedsch.close()
