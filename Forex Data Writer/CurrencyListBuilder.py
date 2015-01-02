'''
Created on Dec 17, 2014

@author: dan
'''

# from my super limited understanding of BeautifulSoup, 
# the soup.find_all( "       ", {"         ": "       "}) looks as follows
#                    |Thing right after the '<' 
#                                |something before an equals sign
#                                              |something after the equals sign (what we're setting the last value equal to) 
# Example: g_data = soup.find_all("div", {"class": "info"})
#
# random helpful thing: time.time() gives us the current time in seconds

import requests
import time
import sys
import threading
from bs4 import BeautifulSoup

class CurrencyListBuilder(threading.Thread):
    
    def run(self):
        self.collect()
        
    def __init__(self):
        None
    
    def __init__(self, id, interval, runs):
        self.id = id
        self.interval = interval
        self.runs = runs
        self.url = 'http://www.fxstreet.com/rates-charts/forex-rates/'
        self.currency_list = []    
    
    def data_crawler(self, start_page, id):
        r = requests.get(start_page)
        soup = BeautifulSoup(r.content)
        
        links = soup.find_all("td", {"id": id})
        
        for link in links:
            self.currency_list.append(link.text)
            
    def print_out_header(self):
        print('Start time: ' + time.strftime("%H:%M:%S") + '\nTime interval in seconds: ' + str(self.interval) + '\nTotal runtime in seconds: ' + str(self.runs*self.interval) + '\n')
        
    def print_out_footer(self):
        print('End time: ' + time.strftime("%H:%M:%S"))
            
    def print_out_list(self, currency_name, currency_list):
        sys.stdout.write(currency_name + ': ')
        for x in currency_list:
            sys.stdout.write(str(x) + ' ')
        print('\n')
    
    def collect(self):                             
        for x in range(0, self.runs):
            start_time_of_loop = time.time()
            self.data_crawler(self.url, self.id)
            end_time_of_loop = time.time()
            runtime = end_time_of_loop - start_time_of_loop
            if((self.interval - runtime) > 0):
                time.sleep(self.interval - runtime)
            
    def get_currency_list(self):
        return self.currency_list
        
        