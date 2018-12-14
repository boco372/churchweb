#!/bin/sh
for file in `find . -type f -mtime -1`
do
done
cd public_html/Newsletters/images
put ./image-2018-04-08.png
put ./08.04.18.pdf StJohns_2018-04-07_web.pdf 

ftp gator4128.hostgator.com
