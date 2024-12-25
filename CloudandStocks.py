#Author: Zac Conti (zconti@vt.edu)
#Date: 9/24/24

from bs4 import BeautifulSoup

import requests

def retrieveStocks():
    websiteG = 'https://finance.yahoo.com/markets/stocks/gainers/'
    resultG = requests.get(websiteG)
    contentG = resultG.text
    websiteL = 'https://finance.yahoo.com/markets/stocks/losers/'
    resultL = requests.get(websiteL)
    contentL = resultL.text



    soupG = BeautifulSoup(contentG, 'lxml')
    soupL = BeautifulSoup(contentL, 'lxml')

    row1 = soupG.find('tr', id = "0")
    row2 = soupG.find('tr', id = "1")
    row3 = soupG.find('tr', id = "2")
    row4 = soupG.find('tr', id = "3")
    row5 = soupG.find('tr', id = "4")

    stock1 = row1.find('span').get_text()
    stock2 = row2.find('span').get_text()
    stock3 = row3.find('span').get_text()
    stock4 = row4.find('span').get_text()
    stock5 = row5.find('span').get_text()

    row6 = soupL.find('tr', id = "0")
    row7 = soupL.find('tr', id = "1")
    row8 = soupL.find('tr', id = "2")
    row9 = soupL.find('tr', id = "3")
    row10 = soupL.find('tr', id = "4")

    stock6 = row6.find('span').get_text()
    stock7 = row7.find('span').get_text()
    stock8 = row8.find('span').get_text()
    stock9 = row9.find('span').get_text()
    stock10 = row10.find('span').get_text()
    
    print(f"📈 Gainers\n📈 1. {stock1}\n📈 2. {stock2}\n📈 3. {stock3}\n📈 4. {stock4}\n📈 5. {stock5}\n")
    print(f"📉 Losers\n📉 1. {stock6}\n📉 2. {stock7}\n📉 3. {stock8}\n📉 4. {stock9}\n📉 5. {stock10}\n")
    
def retrieveWeather():
    websiteW = 'https://weather.com/weather/today/l/7784244424753243b43d7a324db1622ffed65b587d50408cdd8e79c61073ccfd'
    resultW = requests.get(websiteW)
    contentW = resultW.text



    soupW = BeautifulSoup(contentW, 'lxml')
    
    highSegment = soupW.find('div', class_ = "CurrentConditions--tempHiLoValue--Og9IG")

    current = soupW.find('span', class_ = "CurrentConditions--tempValue--zUBSz").get_text()
    low = soupW.find('span', class_ = "Column--tempLoValue--gyah9").get_text()
    high = highSegment.find('span').get_text()
    conditions = soupW.find('div', class_ = "CurrentConditions--phraseValue---VS-k").get_text()
    
    print(f"⛅ Currently: {current}")
    print(f"🌧️ Conditions: {conditions}")
    print(f"☀️ High: {high}")
    print(f"❄️ Low: {low}")
    
print("> Type 'stocks' or 'weather'")

while True:
    request = input("> ")
    if request == "stocks":
        retrieveStocks()
    elif request == "weather":
        retrieveWeather()
    elif request == ("quit" or "exit"):
        break