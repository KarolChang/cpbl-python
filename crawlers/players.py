# ssl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 連線取得 json 檔案
import urllib.request as req
import urllib.parse as parse
import json
import bs4

# url
url = "https://www.cpbl.com.tw/player"

def fetchDatas():
  request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
  })

  with req.urlopen(request) as res:
    data = res.read().decode('utf-8')

  # 解析網頁原始碼
  obj = {}

  root = bs4.BeautifulSoup(data, "html.parser")
  players = root.find_all("dd", class_="")
  for player in players:
    id = player.a.get("href")[18:]
    obj[id] = player.a.string
  
  return obj