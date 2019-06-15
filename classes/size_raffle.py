import requests
import names
import random
from threading import Thread

class SizeRaffle():

    def __init__(self, email, city, country, store, shoe_size, proxies):
        if '@' not in email:
            self.log("ERROR: Invalid email")
            exit()

        self.email = email
        self.city = city
        self.country = country
        self.store = store.upper()
        self.shoe_size = shoe_size
        self.proxies = proxies

        self.headers = {
            'Referer': 'https://size-client-resources.s3.amazonaws.com/email/yezzy/SizeRafflePageUK.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
        }


    def log(self, msg):
        print(str(msg))


    def get_phone(self, phone_number):
        if (len(phone_number) < 11):
            phone_number += str(random.randint(0, 10))
        else:
            return phone_number

        return self.get_phone(phone_number)


    def format_proxy(self, proxy):
        try:
            ip = proxy.split(":")[0]
            port = proxy.split(":")[1]
            userpassproxy = '%s:%s' % (ip, port)
            proxyuser = proxy.split(":")[2].rstrip()
            proxypass = proxy.split(":")[3].rstrip()
            proxies = {'http': 'http://%s:%s@%s' % (proxyuser, proxypass, userpassproxy),
                       'https': 'http://%s:%s@%s' % (proxyuser, proxypass, userpassproxy)}

        except:
            proxies = {'http': 'http://%s' % proxy, 'https': 'http://%s' % proxy}

        return proxies


    def enter(self):
        parameters = {
            'nourl': 'SIZE_YZY_350_BUTTER',
            'firstName': names.get_first_name(),
            'email': "{}{}{}{}{}".format(self.email.split('@')[0], "+", random.randint(10000, 10000000),"@",self.email.split('@')[1]),
            'telephone': self.get_phone("07"),
            'SZ_YZY_BUTTER_shoetype': self.store,
            'SZ_YZY_BUTTER_shoesize': self.shoe_size if self.shoe_size is not None else str((random.randint(7, 26) * 5 ) / 10 ),
            'SZ_YZY_BUTTER_cityofres': self.city,
            'yzemail': 'SIZE_YZY_350_BUTTER',
            'SZ_YZY_BUTTER_countryofres': self.country,
            'emailpermit': '1',
            'sms_optout': '0'
        }

        try:
            if len(self.proxies) > 0:
                requests.post("https://reporting.size.co.uk/cgi-bin/rr/blank.gif", params=parameters, headers=self.headers, proxies=self.format_proxy(random.choice(self.proxies)))
            else:
                requests.post("https://reporting.size.co.uk/cgi-bin/rr/blank.gif", params=parameters, headers=self.headers)
            self.log("Successfully entered")
        except Exception as e:
            self.log("Error entering: " + str(e))


    def run(self, num):
        for i in range(num):
            Thread(target=self.enter).start()