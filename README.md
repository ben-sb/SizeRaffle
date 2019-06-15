# SizeRaffle

Python program to enter Size's Antlia raffle. 
Requires Python 3.6 or above



## Config
* email - your email (+ trick will be used to enter) 
* city - your city
* country - your country (make sure it matches exactly a country on the list of the raffle page)
* store_location - location of your nearest Size store (get this from their list of stores on the raffle page)
* specific_size - shoe size **(leave as null if you want random sizes)**
* entries - number of entries you want 

**Everything should be a string (surrounded by ") other than entries (which is an integer) and specific_size if leaving as null**


## To Run
* Download and run the appropriate Python installer from here https://www.python.org/downloads/release/python-367/ (skip this step if you already have Python 3.6 installed)
* Install requirements in requirements.txt using one of the following commands
  - Windows: pip install -r requirements.txt
  - Mac and Linux: python3 -m pip install -r requirements.txt
* Edit config.json
* Put proxies in proxies.txt or clear file to run without proxies
* Run main.py using using one of the following commands
  - Windows: python main.py
  - Mac and Linux: python3 main.py
