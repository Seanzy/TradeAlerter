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

Next: Figure out why I can't push to git. Done. I had local changes that weren't reflected on my remote (online). So I added the HistBuilder file I needed, removed my 2 recent commits using git reset "HEAD^" twice so that my local was no longer ahead of remote. Then I force pushed my most recent old commit that had not yet been pushed to remote with:
git push -f origin main
main is my main branch, not master, origin is the remote branch online
Then the local and remote are in sync. Yay. 
But then, I tried to change my commit message using reset, then wrote a new commit message. But once I tried to push it, I got the same "updates were rejected because the tip of your current branch is behind its remote counterpart" error, just as I was receiving before. This must be because even though I reset the commit locally, the remote has not been reset. Does this mean I need to do a pull request? 

Yes I think so because now remote is ahead by 1 commit. I did a git pull to merge the changes, it merged automatically because there were not that many changes. I still need to learn how to merge when there are a bunch of changes.   

Next: create 1 modules file that every file can import

11/15/20 - Doing histograms

12/1/20 - My histogram builder is automating now. Saves me lots of time because I don't have to do manual calculations in Excel anymore. 

Next: read predictions file. Done.
Next: Alert on 1 price. 
  1: find "ABC". Done. 
  2: parse predictions lines into a predictions object. Done. 
Next: reorder the code with functions at the top and vars below, function calls next. Done.

12/7/20 - redoing SP 500 companies
12/8/20 - getting trade alerter working
12/9/20 - Connecting to web socket / API to alert on prices

Next: get histbuilder to ouput the data for main.js
12/11/20 - beginning to get alerts. 
12/12/20 - Trying to work with async data in python