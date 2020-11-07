# TradeAlerter.py
import pandas as pd
import numpy as np
import yfinance as yf
import sys 
import symbols
import tkinter
from tkinter import messagebox

# print(sys.path)

# tickers = 'UBER,AAPL'
data = yf.download(tickers=symbols.tickers, period='5d', interval='1d')
print(data)


# This code is to hide the main tkinter window
root = tkinter.Tk()
root.withdraw()

# Message Box
messagebox.showinfo("Title", "Message")