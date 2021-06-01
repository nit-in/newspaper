#!/bin/bash


function the_hindu(){
    echo "Cd to folder"
    cd /home/runner/work/newspaper/newspaper
    echo "in the folder"
    #rm -f *.csv    
    scrapy crawl --nolog the_hindu #> the_hindu.log
    echo "done"
    #sed -e 's/,,/, ,/g' failed_to_download.csv | column -s , -t | cat
}
function bustd(){
    echo "Cd to folder"
    cd /home/runner/work/newspaper/newspaper
    echo "in the folder"
    #rm -f *.csv
    scrapy crawl --nolog business_standard #> business_standard.log
    echo "done"
    #sed -e 's/,,/, ,/g' failed_to_download.csv | column -s , -t | cat
}
function etime(){
    echo "Cd to folder"
    cd /home/runner/work/newspaper/newspaper
    echo "in the folder"
    #rm -f *.csv
    scrapy crawl --nolog economic_times #> economic_times.log
    echo "done"
    #sed -e 's/,,/, ,/g' failed_to_download.csv | column -s , -t | cat
}
function livem(){
    echo "Cd to folder"
    cd /home/runner/work/newspaper/newspaper
    echo "in the folder"
    #rm -f *.csv
    scrapy crawl --nolog livemint #> livemint.log
    echo "done"
    #sed -e 's/,,/, ,/g' failed_to_download.csv | column -s , -t | cat
}

function indexp(){
    echo "Cd to folder"
    cd /home/runner/work/newspaper/newspaper
    echo "in the folder"
    #rm -f *.csv
    scrapy crawl --nolog indian_express #> livemint.log
    echo "done"
    #sed -e 's/,,/, ,/g' failed_to_download.csv | column -s , -t | cat
}


function finexp(){
    echo "Cd to folder"
    cd /home/runner/work/newspaper/newspaper
    echo "in the folder"
    #rm -f *.csv
    scrapy crawl --nolog financial_express #> livemint.log
    echo "done"
    #sed -e 's/,,/, ,/g' failed_to_download.csv | column -s , -t | cat
}

the_hindu &;bustd &;etime &;finexp &;livem&;indexp &  