#!/bin/bash

#Retrieve username and password from userinfo.txt file, setup URL
USERNAME=$(sed -n 1p userinfo.txt | tr -d '\n' | tr -d '\r')
PASSWORD=$(sed -n 2p userinfo.txt | tr -d '\n' | tr -d '\r')
URL="https://student.guc.edu.eg/Web/Student/Schedule/GeneralGroupSchedule.aspx"

#Initialise first request to get schedule IDs and Viewstates
printf "Sending first request to retrieve state information.....\n"
curl -s --ntlm -u "$USERNAME:$PASSWORD" "$URL" > mainpage.html
printf "Initial Request Successful\n"