from bs4 import BeautifulSoup
import requests

url = "https://www.indeed.com/jobs?q=data%20analyst&l=Overland%20Park%2C%20KS&from=searchOnHP&vjk=d240da045b2fb078" 
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="Data")
print(prices)

