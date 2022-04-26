import cloudscraper
from bs4 import BeautifulSoup
from telegraph import Telegraph

class Nocturnetls:

  def __init__(self, url):
    self.url = url
    self.req = cloudscraper.create_scraper()
    self.novel = {}

  def dung(self):
    s = self.req.get(self.url)
    sp = bs(s.content, "html.parser")
    body = sp.find_all("p")
    tx = (self.url.split("/")[-1]).split(".")[0]
    tx = tx.replace("-", " ")
    txt = ""
    for body in body[:-1]:
      txt += str(body) 
    txt = txt.replace("strong>", "b>")
    return txt


  def puck(self):
    txt = str(self.dung())
    while "CAPTCHA" in txt:
      txt = str(self.dung())
    return txt

  def get_novel(self):
    t = self.get_graph()
    tx = self.url.split("/")[-1]
    tx = tx.split(".")[0]
    tx = tx.replace("-", " ")
    txt = self.puck()
    uri = t.create_page(title=tx, author_name="Horni Senpai", author_url="https://telegram.dog/Horni_Senpaii", html_content=txt)["url"]
    self.novel['name'] = tx
    self.novel['uri'] = uri
    return self.novel

  def get_graph(self):
    tele = Telegraph()
    tel = tele.create_account("AuraMoon-noct")
    return tele
