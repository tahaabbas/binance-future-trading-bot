# Binance Future Trading Bot (EMA Crossover Strategy)
<p>This bot automates future trading on Binance based on Exponential Moving Average (EMA) crossovers. When the short-term EMA crosses above the long-term EMA, it's an indication of upward momentum, and the bot places a buy order. Conversely, when the short-term EMA crosses below the long-term EMA, signaling potential downward momentum, the bot places a sell order.</p>

<b>How It Works:</b>
    <p>In a continuous loop, the bot fetches the latest price for the given symbol and calculates the short and long EMAs.</p>
    <b>Buy Order Logic:</b>
    <p>If the short EMA is greater than the long EMA (indicating potential upward price movement) and the last action wasn't a buy, the bot closes any existing sell order and places a buy order.
        After placing the buy order, the bot checks if the order was fully executed (FILLED status) before updating its last action.</p>
    <b>Sell Order Logic:</b>
    <p>If the short EMA is less than the long EMA (indicating potential downward price movement) and the last action wasn't a sell, the bot closes any existing buy order and places a sell order.
        After placing the sell order, it checks if the order was fully executed before updating its last action.</p>
    <b>Exception Handling:</b> 
    <p>If there's a timeout when communicating with Binance's API, the bot catches the exception and continues operation, ensuring the script doesn't terminate unexpectedly.</p>

# Usage
This bot is executed from the command line and requires the trading pair symbol, data-fetching interval, and the periods for the short and long EMAs as arguments. The bot then continually checks the EMA values and makes decisions based on the crossover strategy.

# Requirments
- Python3.x
- Pip

# Installation
<b>TA-Lib Installation</b>
<pre>
sudo apt-get update
sudo apt-get install build-essential wget
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib/
./configure --prefix=/usr
make
sudo make install
</pre>

<b>Finally Run</b>
<pre>pip install python-binance requests ta-lib numpy</pre>

# Run
python run_bot.py &lt;Symbol> &lt;Short EMA Period> &lt;Long EMA Period> &lt;Interval> &lt;Leverage> &lt;order size>

<b>Example:</b>
<code>python run_bot.py BTCUSDT 9 30 1h 10 2.5</code>

<b>To Run in Background</b>
<code>nohup python run_bot.py BTCUSDT 9 30 1h 10 2.5 &</code>

<hr>
<b>The Above script was only tested on Ubuntu 20.04.4 LTS Distribution</b>

# Risk Warning
Remember, while the EMA crossover strategy is popular, it's essential to combine it with other indicators or methods for more robust trading signals. Always ensure you are comfortable with the risks before running any trading bot live.

# Support This Project
<p>First off, thank you for taking the time to consider supporting this project. It's built with a lot of hard work, dedication, and countless hours of coding.</p>

<p>If you've found any value in my work, and would like to support its continued development, consider making a donation. Every little bit helps in maintaining the project, covering costs, and encouraging further enhancements.
Donate with Bitcoin (BTC)</p>

<div class="btc-donation-container" style="padding: 20px; width: 91%; text-align: center;">
  <h3>Donate with BTC</h3>
  <p>Scan the QR code or send your donation to the address below:</p>
  <img src="https://tdrintl.com/wp-content/uploads/2023/09/canvas_btc.png" alt="BTC QR Code" style="width: 80px; height: 80px; margin-bottom: 20px;">
  <p><strong>BTC Address:</strong></p>
  <p style="word-wrap: break-word; background-color: #ccc; padding:10px;"><code><b>15AZJpmYEV2Q9fvf7DvQgTHcFgmNg2UcPz</b></code></p>
</div>

<p><b>Your generosity and support will always be appreciated!</b></p>
