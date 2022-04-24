import cloudscraper
from bs4 import BeautifulSoup
from telegraph import Telegraph

class Nocturnetls:

  def __init__(self, url=None):
    self.url = url
    self.req = cloudscraper.create_scraper()
    self.novel = {}

  def get_novel(self):
    title1 = (self.url.split("/")[-1]).split("-")
    for tit in title1:
      nt = tit.capitalize()
      title1 = list(map(lambda x: x.replace(tit, nt), title1))
    title1 = " ".join(nt for nt in title1)
    title2 = (self.url.split("/")[-2]).split("-")
    for tit in title2:
      nt = tit.capitalize()
      title2 = list(map(lambda x: x.replace(tit, nt), title2))
    title2 = " ".join(nt for nt in title2)
    title = title1 + " " + title2
    cover = self.get_cover()
    tele = self.get_graph()
    fname = title + ".txt"
    cont =  "<p><b>" + title + "</b><br><br><br>"
    cont += f"<img src='{cover}'><br>"
    s = self.req.get(self.url)
    soup = BeautifulSoup(s.content, "html.parser")
    paras = soup.find_all("span")
    lim = []
    for para in paras:
      x = para.get("data-sheets-hyperlinkruns")
      if x:
        lim.append(paras.index(para))
    start = int(lim[0]) + 1
    end = int(lim[1])
    paras = paras[start:end]
    for para in paras:
      cont += f"{para.string}<br>"
    cont += "</p>"
    fname = tele.create_page(title=title, html_content=cont)
    self.novel['name'] = title
    self.novel['file'] = fname["url"]
    self.novel['cover'] = cover
    return self.novel

  def get_cover(self):
    cover_uri = self.url.split("/")[:-1]
    cover_uri = '/'.join(uri for uri in cover_uri)
    covers = self.req.get(cover_uri)
    covers = BeautifulSoup(covers.content, "html.parser")
    covers = covers.find_all("img")
    for covers in covers:
      cover_src = covers.get("data-src")
      if cover_src:
        cover = cover_src.split("?")[0]
      else:
        pass
    return cover
  
  def get_graph(self):
    tele = Telegraph()
    tel = tele.create_account("AuraMoon-noct")
    return tele
