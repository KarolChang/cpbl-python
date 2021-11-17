# ssl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 連線取得 json 檔案
import urllib.request as req
import urllib.parse as parse
import json
import bs4

# url
url = "https://www.cpbl.com.tw/player/trans"

def fetchDatas(year, month):
  postData = {
    "Year": year,
    "Month": month
  }

  postDataString = parse.urlencode(postData)
  postDataEncode = postDataString.encode('ascii') 

  request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
  }, method='POST', data=postDataEncode)

  with req.urlopen(request) as res:
    data = res.read().decode('utf-8')

  # 解析網頁原始碼
  obj = {}

  root = bs4.BeautifulSoup(data, "html.parser")
  tds = root.find_all("td")

  obj = {}
  nowDay = ""
  temp = []
  for td in tds:
    if td.string and "/" in td.string:
      obj[td.string.strip()] = []
      nowDay = td.string.strip()
    else:
      temp.append(td.string)
      if len(temp) == 3:
        obj[nowDay].append(temp)
        temp = []
  return obj