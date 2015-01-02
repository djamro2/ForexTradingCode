'''
Created on Dec 18, 2014

@author: dan
'''

from ThreeComparisonAlgorithm import ThreeComparisonAlgorithm

fileName = 'EUR_USD_12_18_2014_15SA.txt'
difference_one = 1
difference_two = 10
pip_change = 2

eur_usd_TCA = ThreeComparisonAlgorithm(difference_one, difference_two, fileName)
eur_usd_TCA.set_pip_change(pip_change)
eur_usd_TCA.run()

