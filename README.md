# TradeAlerter
Project started 11/6/2020

Couldn't find a free stock price alerter that met my needs, so I am building it from scratch

I will need to keep the API key in a separate file and include that file in the .gitignore, as well as my proprietary list of symbols in a separte file. 

tickers parameter inside of yf.download() takes a string of one or more stock symbols such as 'UBER' or 'UBER, AAPL', see link below for more details on the params

Using Sublime Text3 and Conda testenv (shift + control + p) in Sublime to activate

Importing modules including yfinance. Thank you https://medium.com/@lhessani.sa

Done! Got it working pretty easily! If my script name is "symbols.py" I type import symbols, not import symbols.py. Of course I had to refer to variables in the symbols.py file as symbols.<var name>

Also need to make sure the appropriate libraries are imported in the Anaconda testenv. 

Next: adding a message box Done. 

Next: How to read my file of pre-defined prices to set the alerts? 


11/8/20 - will start adding docstrings to my functions

11/11/20 - Automating histograms with Python so I can save time working with Excel files. 

Next: Figure out why I can't push to git. Done. I had local changes that weren't reflected on my remote (online). So I added the HistBuilder file I needed and removed my 2 recent commits so that my local was no longer ahead of remote. 

Next: create 1 modules file that every file can import