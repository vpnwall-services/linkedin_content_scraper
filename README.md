LINKEDIN CONTENT SCRAPER
===

What it do ?
---

This solution retrieve content from a company's linkedin page

#### How does it work ?

It will first grab all page with scripted Selenium browser
Then, this content will be parsed with another python script

#### Installation :
 ```
 cd /home/linkedinapi
 apt update
 apt install python3 python3-pip
 pip3 install selenium
 wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
 tar xf geckodriver-v0.26.0-linux64.tar.gz
 rm -rf geckodriver-v0.26.0-linux64.tar.gz
 cp geckodriver /usr/bin/geckodriver
 python3 linkedin_content_scraper.py
 ```
 
#### How to use:
Install requirements:
```
pip3 install -r requirements.txt
```
* Retrieve company_name here https://www.linkedin.com/company/<xxxxxxx> 
* Put company_name in customerlist.txt, one by line
* Fill linkedin_user and linkedin_password in the python script
* Once done, run the script like this:  
```
python3 linkedin_content_scraper.py
```

#### From who ?
From infra with love ...
