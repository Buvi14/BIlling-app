# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Plotting the graph for given data
import matplotlib.pyplot as mp                            #plotting the graph
import pandas as pd                                       #for import the data
mydata=pd.read_csv('example.csv')                         #import the data
x=input("Enter the product_id/product_value/price:")      #x-axis values
y=input("Enter the product_id/product_value/price:")      #y-axis values
mp.hist(x,bins=10)                                        #for histogram representation
mp.hist(y,bins=10)
#mp.bar(x,y,width=1,color="green")
mp.show()                                                 #showing the histogram