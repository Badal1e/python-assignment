import requests
from bs4 import BeautifulSoup

def webdisplay():
    url='https://en.wikipedia.org/wiki/General-purpose_programming_language'
    
    resp=requests.get(url)
    
    if resp.status_code==200:
        print("Successfully opened the web page")
    
        soup=BeautifulSoup(resp.text,'html.parser')    

        l=soup.find("div",{"class":"div-col"})
    
        for i in l.find_all("li"):
            print(i.text)
    else:
        print("Error")
        
webdisplay()
