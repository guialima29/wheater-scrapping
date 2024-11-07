from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup
import unicodedata

@dataclass
class Wheater:

    def normalize(self,city):
        city = city.strip()
    
        city = city.replace(" ", "-")
    
        city = city.lower()
    
        city = ''.join((c for c in unicodedata.normalize('NFD', city) if unicodedata.category(c) != 'Mn'))
    
        return city
    
    def wheater(self,name):
        url = (f"https://www.tempo.com/{name}.htm")
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        wheater_elements = soup.find_all('span', class_="zona-color")

        quotes = []

        for wheater_elements in wheater_elements:
            description = wheater_elements.find('span', class_="descripcion").text
            temp = wheater_elements.find('span', class_="temperatura").find('span',class_="dato-temperatura").text

            if description and temp:
                quotes.append({
                    'description': description,
                    'temp': temp,
                })
            else:
                print("Missing description or temperature in element.")

        if not quotes:
            print("No valid weather data found.")
            return
        
        return (f"Wheater: {quotes[0]['temp']} {quotes[0]['description']}")