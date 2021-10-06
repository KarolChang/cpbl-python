# ssl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 連線取得 json 檔案
import urllib.request as req
import urllib.parse as parse
import json
import bs4

url = "https://www.cpbl.com.tw/xmdoc/indexaction"

def fetchDatas():
  postData = {
    "__RequestVerificationToken": "tJJAdad8i8l86ZgciPwYavh5qA5ezsIsJU2ztBY9bmzb0tTOaf0FYnmLfkN7IHdPPhyoVZUKJw_cJzJMnd3Oyaz7yBw1",
    "CondsSId": "0L278623004846420986",
    "ExecAction": "Q",
    "IndexOfPages": 0
  }

  postDataString = parse.urlencode(postData)
  postDataEncode = postDataString.encode('ascii') 

  request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
  }, method='POST', data=postDataEncode)

  with req.urlopen(request) as res:
    data = res.read().decode("utf-8")

  # 解析網頁原始碼

  print(datas)
  return datas

fetchDatas()