from bs4 import BeautifulSoup
import requests

res=requests.get("https://www.orangepage.net/")
soup = BeautifulSoup(res.text,"html.parser")
tag_obj=soup.find_all("p")
text_list=[x.string for x in tag_obj]
print(text_list[2])