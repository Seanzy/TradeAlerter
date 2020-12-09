# TradeAlerter.py
import pandas as pd
import numpy as np
import yfinance as yf
import sys 
import symbols
import tkinter
from tkinter import messagebox
import matplotlib
import matplotlib.pyplot as plt #submodules are not always imported by default
import matplotlib.pylab as lab
# from functools import reduce
import yfinance as yf
# print(sys.path)

# Use this to check current prices? 
# data = yf.download(tickers=symbols.tickers, period='5d', interval='1d')
# print(data)

# This code is to hide the main tkinter window
root = tkinter.Tk()
root.withdraw()

# Message Box
# messagebox.showinfo("Title", "Message")

def readfile(path):
  return open(bspath,"r").readlines()
'''Returns an object of symbols as keys and list of predictions as values'''
def parseline(line):
  splitline = line.split(":")
  symbol = splitline[0]
  predictionslist = eval(splitline[1][5:]) 
 
  # print(splitline)
  # print(splitline[0])
  # print(predictions)
  # print(splitline[1])
  # print(predictionslistlist, type(predictionslistlist))
  predictions[symbol] = list(map(lambda price: float(price), predictionslist))
# end parseline()

# Program execution starts here$$$$$$$$$$$$$$$$$$$$$$$$$$$
filedate = "11-30-20"
bspath = "C:\\Users\\sdgur\\Documents\\T3 Trading\\Plans for Next Day\\berkshireStocks\\"+ filedate #berkshirestockspath
predictionsfile = readfile(bspath) 
lines = {}
predictions = {}
i = 1

for line in predictionsfile: 
  lines[i] = line
  i += 1
  if ": (8)" in line:
    # print("LINE:",line)
    parsedline = parseline(line)
    # print(parsedline[0], parsedline[1])

print(predictions)
print(predictions["ABC"][0]*2)



