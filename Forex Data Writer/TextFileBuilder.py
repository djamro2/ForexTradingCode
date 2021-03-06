'''
Created on Dec 18, 2014

@author: dan
'''

from CurrencyListBuilder import CurrencyListBuilder

fileName = 'EUR_USD_12_19_2014_15SA.txt'
id_eurusd = 'last_3212164'
interval = 15
runs = 480

# use a for loop so there is still some list when canceling midway

for x in range(0, runs):
    
    print('Current run: ' + str(x))
    
    list_to_text = CurrencyListBuilder(id_eurusd, interval, 1)
    list_to_text.run()
    
    currency_list = list_to_text.currency_list
    
    file = open(fileName, 'a+')
    
    for value in currency_list:
        file.write(str(value) + '\n')
    
    file.close()