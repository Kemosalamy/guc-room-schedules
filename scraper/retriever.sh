#!/bin/bash

#Retrieve username and password from userinfo.txt file, setup URL
USERNAME=$(sed -n 1p userinfo.txt | tr -d '\n' | tr -d '\r')
PASSWORD=$(sed -n 2p userinfo.txt | tr -d '\n' | tr -d '\r')
HEADERS=$(cat headers.txt | tr -d '\n' | tr -d '\r')
URL="https://student.guc.edu.eg/Web/Student/Schedule/GeneralGroupSchedule.aspx"


#Looping through all schedule IDs
printf "Sending individual schedule requests.....\n"
cat ids.txt | while read SCHID 
do
    SCHID=${SCHID//$'\n'/}
    SCHID=${SCHID//$'\r'/}
    CURHEADER="$HEADERS&scdTpLst=$SCHID"
    printf "Requesting schedule with ID:$SCHID.....\n"
    curl -s --ntlm -u "$USERNAME:$PASSWORD" "$URL" >> schedules.html \
    --data-raw "$CURHEADER" --compressed
    sleep 3
    printf "Request for $SCHID was successful\n"
done