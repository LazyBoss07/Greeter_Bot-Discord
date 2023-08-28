# Greeter - A Discord Bot

### Description:
Greeter bots only provide users with news headlines and weather information.
I used Replit to host my bot's backend and the Discord developer platform to design it.
and I connected my bot to the APIs (Open Weather and Newsapi)
This bot receives regular notifications from uptimerobot to prevent it from shutting down.
### Instruction for use:
#### Custom Command
$hello => return the user with greeting and rule to use the bot
$news => return news top headline.
$news "Country Code" "Category" => return news top headline filtered with the users input.
$weather "cityName" => return the city's current temperature and a weather report.
## Code Written
I have used discord lib which contains build in Call-backs and Async method which is used to give the visual message to Bot
Discord library uses event listening.
Client is first initiated.The build-in methods have been implemented.
### Newsapi
News API is a simple JSON-based REST API for searching and retrieving news articles from all over the web. Using this, one can fetch the top stories running on a news website or can search top news on a specific topic (or keyword).

#### Python client library
Use the unofficial Python client library to integrate News API into your Python application without having to make HTTP requests directl
### Open Weather
The OpenWeatherMap is a service that provides weather data, including current weather data, forecasts, and historical data to the developers of web services and mobile applications.

### What i did :-

Import the requests and JSON modules.

Initialize the base URL of the weather API https://api.openweathermap.org/data/2.5/weather?.

Initialize the city and API key.

Update the base URL with the API key and city name.

Send a get request using the requests.get() method.

And extract the weather info using the JSON module from the response.
### Methods
on_read turn the Bot up and make the bot online.
on_message waiting until user input and implement the logic behind each custom command.
### Decorator
The @client.event() decorator is used to register an event. This is an asynchronous library, so things are done with callbacks. A callback is a function that is called when something else happens. In this code, the on_ready() event is called when the bot is ready to start being used. Then, when the bot receives a message, the on_message() event is called.

### get_news() & get_weather:
methods fletch json data from the API using the API token allotted.
The json data is then processed and returned for display.
## Displaying data
data returned from the API are displayed using "await message.channel.send".
each data sends and received is objected and to access we use "message.contain".
## keep_alive
this is a flask code which deploys our bot in to http(s) server in order to make the bot up all time or else the bot will go down
the flask code will regularly verifys the ping.
I used UpTimeRobot to ping the bot regularly to create a positive  network traffic.
To keep the bot running continuously, we'll use another free service called Uptime Robot at https://uptimerobot.com/.

Uptime Robot can be set up to ping the bot's web server on repl.it every 5 minutes. With constant pings, the bot will never enter the sleeping stage and will just keep running.

So to run the bot continuously  two more things are done  :

create a web server in repl.it and
set up Uptime Robot to continuously ping the web server.
### REPLIT
Repl.it is a free IDE (integrated development environment) that allows users to write their own programs and code in dozens of different languages

## Requirement
flask
requests
os
discord
threading
## API
Open weather : openweathermap.org

NewsAPI : newsapi.org

Discord Developer : discord.com/developers







