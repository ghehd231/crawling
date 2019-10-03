import requests
from bs4 import BeautifulSoup
def getList():
    response = requests.get("http://www.frankenmono.com")
    result = response.text

    soup = BeautifulSoup(result, "html.parser")

# end getList()

getList()