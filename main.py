import discord 
#asycn lib so things are done with call back
import os
import requests #used to access json returned from api
from keep_alive import keep_alive
# event listening and respond to it 
# connection
import random
# req = requests.get("https://discord.com/api/path/to/the/endpoint")
# print(req.headers["X-RateLimit-Remaining"])
client = discord.Client(intents=discord.Intents.default())
query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "d2cff9dfcd694355a10ff6de09e156b0"
    }
@client.event
async def on_ready():
  print("We have logned as {0.user}".format(client))

@client.event
async def on_message(message):
  msg=message.content
  if message.author == client.user:
    return
  if message.content.startswith("$hello"):
    await message.channel.send("           Hello!          ")
    await message.channel.send("This bot Will Just give You real Time infromation about Weather and current News Around the world")
    await message.channel.send("----------------------------")
    await message.channel.send("         Instructions:      ")
    await message.channel.send("         Country code       \nae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si sk th tr tw ua us ve za")
    await message.channel.send("----------------------------")
    await message.channel.send("         For weather:    \n$weather <city name>\neg:$weather chennai")
    await message.channel.send("----------------------------")
    await message.channel.send("For news at specific county and catagories:\n$news <country code> <topic>\neg: $news in business")
    await message.channel.send("---------------------------")
    await message.channel.send("For Top headlines:\n$news")
    
  if message.content.startswith("$weather"):
    
    city=msg.split("$weather ",1)[1]
    await message.channel.send(get_weather(city))
  if msg.strip()=="$news":
    topics=get_news()
    await message.channel.send("HEADLINES:")
    for topic in topics:
      await message.channel.send(topic)
    await message.channel.send("THAT'S IT FOR TODAY :)")
  elif message.content.startswith("$news") and len(msg)>5:
    
    country=msg.split(" ")[1]
    
    cat=msg.split(" ")[2]
    topics=get_newsatcountry(country,cat)
    await message.channel.send("HEADLINES:")
    for topic in topics:
      await message.channel.send(topic)
    await message.channel.send("THAT'S IT FOR TODAY :)")
  


def get_weather(city_name):
  api_key = os.getenv("API_WEATHER")  # Enter the API key you got from the OpenWeatherMap website
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
  
  complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name  # This is to complete the base_url, you can also do this manually to checkout other weather data available
  response = requests.get(complete_url)
  x = response.json()
  
  if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    z = x["weather"]
  
    weather_description = z[0]["description"]
    return (" Temperature : " +
                    str(current_temperature -273) +
          "\nDescription : " +                    str(weather_description).title())
  else:
    return "CITY NOT FOUND"
                        

def get_news():
  response = requests.get("https://newsapi.org/v1/articles",params=query_params)
  open_bbc_page = response.json()
  article = open_bbc_page["articles"]
  results = []
  for ar in article:
    results.append(ar["title"])
  return results
def get_newsatcountry(country,cat):
  # queryparams = {
  #     "source": "bbc-news",
  #     "sortBy": "top",
  #     "apiKey": "d2cff9dfcd694355a10ff6de09e156b0"
  # }
  
    
  # response = requests.get("https://newsapi.org/v1/articles",params=queryparams)
  urll=f"https://newsapi.org/v2/top-headlines?country={country}&category={cat}&apiKey=d2cff9dfcd694355a10ff6de09e156b0"
  response = requests.get(urll)
  open_bbc_page = response.json()
  article = open_bbc_page["articles"]
  results = []
  for ar in article:
    results.append(ar["title"])
  return results
keep_alive() 
client.run(os.getenv("TOKEN"))
 