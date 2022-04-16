#!/bin/bash

#Retrieve username and password from information.txt file, setup URL
USERNAME=$(sed -n 1p userinfo.txt | tr -d '\n' | tr -d '\r')
PASSWORD=$(sed -n 2p userinfo.txt | tr -d '\n' | tr -d '\r')
URL="https://student.guc.edu.eg/Web/Student/Schedule/GeneralGroupSchedule.aspx"

#Initialise first request to get schedule IDs and Viewstates
curl -s --ntlm -u "$USERNAME:$PASSWORD" "$URL" > mainpage.html
