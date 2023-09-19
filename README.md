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
<code>pip install python-binance requests talib numpy</code>

# Run
python run_bot.py &lt;Symbol> &lt;Short EMA Period> &lt;Long EMA Period> &lt;Interval> &lt;Leverage>

<b>Example:</b>
<code>python run_bot.py BTCUSDT 8 20 1h 10</code>

<b>To Run in Background</b>
<code>nohup python run_bot.py BTCUSDT 8 20 1h 10 &</code>

<hr>
<b>The Above script was only tested on Ubuntu 18.04.6 LTS Distribution</b>

# Todo
In the current implementation, I haven't provided a way to specify the order quantity through function arguments. Instead, you can manually adjust the order quantity within the <b>place_order</b> function. I recognize this limitation, and I plan to enhance this in the next update by allowing the order quantity to be passed as an argument to the function.

# Risk Warning
Remember, while the EMA crossover strategy is popular, it's essential to combine it with other indicators or methods for more robust trading signals. Always ensure you are comfortable with the risks before running any trading bot live.

# Support This Project
<p>First off, thank you for taking the time to consider supporting this project. It's built with a lot of hard work, dedication, and countless hours of coding.</p>

<p>If you've found any value in my work, and would like to support its continued development, consider making a donation. Every little bit helps in maintaining the project, covering costs, and encouraging further enhancements.
Donate with Bitcoin (BTC)</p>

<p>Support this project by sending a donation to the following BTC address: <code>bc1qau67zsv3lg9pupsegxn0zrln97uk9sjhm2dq3g</code></p>

<p><b>Your generosity and support will always be appreciated!</b></p>
