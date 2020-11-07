# TradeAlerter
Project started 11/6/2020

Couldn't find a free stock price alerter that met my needs, so I am building it from scratch

I will need to keep the API key in a separate file and include that file in the .gitignore, as well as my proprietary list of symbols in a separte file. 

tickers parameter inside of yf.download() takes a string of one or more stock symbols such as 'UBER' or 'UBER, AAPL', see link below for more details on the params

Using Sublime Text3 and Conda testenv (shift + control + p) in Sublime to activate

Importing modules including yfinance. Thank you https://medium.com/@lhessani.sa

Done! Got it working pretty easily! If my script name is "symbols.py" I type import symbols, not import symbols.py. Of course I had to refer to variables in the symbols.py file as symbols.<var name>

Also need to make sure the appropriate libraries are imported in the Anaconda testenv. 

Next: adding a message box


