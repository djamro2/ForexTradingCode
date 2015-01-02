'''
Created on Dec 17, 2014

@author: dan
'''

# If there was an x% increase/decrease between a set amount of time, see how that if that currency pair will increase after
# that condition has been 
#
# The point is to wait for this condition to be met in live data, and when it is, that is an indicator to trade

import sys
import threading
from CurrencyListBuilder import CurrencyListBuilder

class ThreeComparisonAlgorithm(threading.Thread):
    
    def __init__(self, difference_one, difference_two, fileName):
        self.counter = 0
        self.positive = 0
        self.difference_one = difference_one
        self.difference_two = difference_two
        self.pip = .0001
        self.pip_change = 1
        self.results = []
        self.file = open(fileName, 'r')
        
    def run(self):
    
        print('\n ... running analysis\n')
        
        self.currency_list = self.file.read().split()
        
        for x in range(0, len(self.currency_list)):
            if (x + self.difference_one + self.difference_two < len(self.currency_list)):
                value1 = float(self.currency_list[x])
                value2 = float(self.currency_list[x + self.difference_one])
                value3 = float(self.currency_list[x + self.difference_one + self.difference_two])
                if (value2 >= (value1 + (self.pip*self.pip_change))):
                    if(value3 > value2):
                        self.results.append(1)
                        self.counter += 1
                        self.positive += 1
                    elif(value3 < value2):
                        self.results.append(0)
                        self.counter += 1
            
        sys.stdout.write('currency_list[] currently has ' + str(len(self.currency_list)) + ' items\n')
        sys.stdout.write('and results[] currently has ' + str(len(self.results)) + ' items\n\n')
        sys.stdout.write('Results: ')
              
        for result in self.results:
            sys.stdout.write(str(result) + ' ')
            
        sys.stdout.write('\n\nIncreased ' + str((float(self.positive)/self.counter)*100) + '% of the time')
        
    def set_pip_change(self, pip_change):
        self.pip_change = pip_change
    