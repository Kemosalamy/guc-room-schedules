#!/bin/bash

#Initiate main request to get Schedule IDs and Viewstate
./initreq.sh

#Scrape Schedule IDs and Viewstate from initial requests
python ./pyscraper.py

#Request all schedules and place them in schedules.html
./retriever.sh

#Parse all schedules from schedules.html into parsedschedules.txt
printf "Parsing requested schedules.....\n"
python ./pyparser.py
printf "Parsing successful\n"

#CLEANUP 

printf "Cleaning up additional files.....\n"

rm ./mainpage.html
rm ./ids.txt
rm ./headers.txt
rm ./schedules.html

printf "Cleanup successful\n"

printf "DONE\n"