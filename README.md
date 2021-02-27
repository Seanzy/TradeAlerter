# TradeAlerter
Project started 11/6/2020

Couldn't find a free stock price alerter that met my needs, so I am building it from scratch.

I will need to keep the API key in a separate file and include that file in the .gitignore, as well as my proprietary list of symbols in a separate file. Done.

tickers parameter inside of yf.download() takes a string of one or more stock symbols such as 'UBER' or 'UBER, AAPL', see link below for more details on the params

Using Sublime Text3 and Conda testenv (shift + control + p) in Sublime to activate

Importing modules including yfinance. Thank you https://medium.com/@lhessani.sa

Done! Got it working pretty easily! If my script name is "symbols.py" I type import symbols, not import symbols.py. Of course I had to refer to variables in the symbols.py file as symbols.<var name>

Also need to make sure the appropriate libraries are imported in the Anaconda testenv. 

Next: adding a message box Done. 

Next: How to read my file of pre-defined prices to set the alerts? Done. 


11/8/20 - will start adding docstrings to my functions. Done. 

11/11/20 - Automating histograms with Python so I can save time working with Excel files. Done but continuously improving. Kaizen.

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
Next: Alert on 1 price. Done.
  1: find "ABC". Done. 
  2: parse predictions lines into a predictions object. Done. 
Next: reorder the code with functions at the top and vars below, function calls next. Done.

12/7/20 - redoing SP 500 companies. Done. Found new potentials. 
12/8/20 - getting trade alerter working. Done. 
12/9/20 - Connecting to web socket / API to alert on prices. Done. 

Next: get histbuilder to ouput the data for main.js in correct format, work in progress. 
12/11/20 - beginning to get alerts. 
12/12/20 - Trying to work with async data in python. Done. 
12/13/20 - Comparing predictions to intraday data. Done. 

Next: Print a list of alerted companies
Next: Perform loop every 20 seconds. Done. 
Next: If there is a new alert that there wasn't before, add an alert for that. Will this require a db or data persistence? Work in progress. 

12/14/20 - Testing
12/15/20 - It made a lot of spot on predictions! 
Next: Add automatic date calculator. Done. 
Next: Add average predictions. 
Next: Add indicator to show how close to low. 
Next: Add indicator 1. Done. 
Next: Add indicator 2. 
Next: Add indicator 3. Done. 
Next: Create an indicator class instead of this giant function. Need help
12/16/20 - Improved histogram builder
12/18/20 - modified trade alerter
12/19/20 - 
Next: Add a timestamp for alerts
12/20/20 - Prepping for tomorrow
12/22/20 - Finished adding timestamper
12/23/20 - reorganized and restructured
12/24/20 - Next: add indicator 4. Fixed macros for daily upkeep
12/27/20 - applying python to bitcoin
12/28/20 - predictions are working
12/29/20 - Lots of good information coming into trading program
12/30/20 - Need to add a nightly plan for next day
12/31/20 - Updated trade alerter
1/1/20 - taking a break
1/3/20 - Job work
1/4/21 - Next: add last price alert
1/5/21 - Discovered new stock that's ripping higher. 
1/6/21 - Added a histogram
1/7/21 - Added more timestamps
1/8/21 - Added symbol and updated duplicate program with correct date
1/9/21 - Prepping for today
1/11/21 - Monitoring BTC
1/12/21 - figured out how to restore firefox session! 
1/13/21 - Need to figure out why some stocks not working
1/14/21 - Figured out why it wasn't working
1/15/21 - Debugging another stock why isn't it working?
  Next: adding symbols
  Next: close and run scans, fix google search
1/16/21 - Bug fix: symbols file was missing ticker! Duh. Will add to procedures to prevent
1/17/21 - Need to improve alerts system. 
1/18/21 - Converting to data frames, 
  Next: make numpy array of symbols, then others
1/19/21: - still working on yesterday's changes
1/20/21 - Trying to handle volatility
1/21/21 - Becoming more disciplined
1/24/21 - Doing Bitcoin stuff
1/25/21 - Add price of BTC to API
1/27/21 - Need patience
1/28/21 - Market going crazy
1/29/21 - Good day today trading
1/30/21 - Beginning new alert program
1/31/21 - Adding indicator 5. Done. 
2/1/21 - Next: remove the stock from costbasis after it has been sold. 
2/2/21 - Done with new cost basis alerter. 
2/3/21 - Adding new alert
2/4/21 - Taking gains
2/5/21 - Added histogram
2/6/21 - Added new names yesterday and prepared for Monday. 
2/7/21 - Bug fix: why isn't it working for certain stocks? 
2/8/21 - Beginning bug fix
2/9/21 - Still working on bug fix
2/10/21 - Added symbols to fix bug
2/11/21 - Added a bunch of symbols
2/12/21 - Added additional error checking for API limit error to stop interval 
2/13/21 - Add indicator 6
2/14/21 - Program is working okay
2/18/21 - Rank output? Adding indicator 6. 
2/20/21 - Indicator 6 working. 
2/22/21 - Continuing to add indicators
2/24/21 - Make sure there's no extraneous text from copy pasting in the daily file from Chrome. Improved indicator 6.
2/25/21 - Next: modify SPXS SDS numbers
2/26/21 - Making message box appear correctly. 