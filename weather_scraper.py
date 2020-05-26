# A practice scraper on the NOAA website
# Usage: prints information on 7-day forecast in San Francisco

from bs4 import BeautifulSoup
import requests

def main():

  page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.XswPwsYpAUs")
  
  soup=BeautifulSoup(page.content,'html.parser')  #make BS object from page content
  
  #get list of daily forecasts from seven-day-forecast section
  days = soup.select("div#seven-day-forecast div.tombstone-container") 


  ## generate ordered list of period titles, short forecast descriptions,
  ## temperature forecast, and long forecasts descs from each day
  periods = []
  short_descs=[]
  temps = []
  long_descs = []

  for d in days:
    periods.append(d.find(class_='period-name').get_text())
    short_descs.append(d.find(class_='short-desc').get_text())
    temps.append(d.find(class_='temp').get_text())
    long_descs.append(d.find("img")['title'])
    



  
    
  
  
  


if __name__ == '__main__':
  main()