#!/bin/bash

rm -f report.html
nmap -oX nmap_scan.xml --stylesheet /var/www/html/scripts/nmap-bootstrap.xsl -sT -p 1-1024 10.35.0.0/24

xsltproc -o report.html /var/www/html/scripts/nmap-bootstrap.xsl nmap_scan.xml
#su -c chown homesec:homesec nmap_scan.xml