#!/bin/bash

#Initiate main request to get Schedule IDs and Viewstate
./initreq.sh

#Scrape Schedule IDs and Viewstate from initial requests
python ./pyscraper.py

#Request all schedules and place them in schedules.html
./retriever.sh

#Parse all schedules from schedules.html into parsedschedules.txt
python ./pyparser.py

#CLEANUP 

rm ./mainpage.html
rm ./ids.txt
rm ./headers.txt
rm ./schedules.html