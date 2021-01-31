# newspaper
python program with scrapy spider to search newspaper site and download webpage as pdf


## Usage:

To use the newspaper spider

**Clone the git or download:**

    git clone https://github.com/nit-in/news-paper.git
    
**enter the news-paper diretory:**
    
    cd news-paper

**Install required packages:**

    pip install -r requirements.txt

**Command to use:**

  `scrapy crawl business_standard`
  
  `scrapy crawl economic_times`
  
  `scrapy crawl livemint`
  
  `scrapy crawl the_hindu`
 
if you do not want any logs
run these as

  `scrapy crawl --nolog business_standard`
  
  `scrapy crawl --nolog economic_times`
  
  `scrapy crawl --nolog livemint`
  
  `scrapy crawl --nolog the_hindu`
 
This will create a folder in your home directory i.e. **~/newspaper**

Pdfs will be saved in this folder
You can change this from config.py file **ROOT_DIR**
