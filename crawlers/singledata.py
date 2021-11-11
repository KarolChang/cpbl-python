# ssl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 連線取得 json 檔案
import urllib.request as req
import urllib.parse as parse
import json
import bs4

# url
url = "https://www.cpbl.com.tw/stats/toplistaction"

def fetchDatas():
  postData = {
    "KindCode": "A"
  }

  postDataString = parse.urlencode(postData)
  postDataEncode = postDataString.encode('ascii') 

  request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
  }, method='POST', data=postDataEncode)

  with req.urlopen(request) as res:
    data = res.read().decode('utf-8')

  # 解析網頁原始碼
  arr = []

  root = bs4.BeautifulSoup(data, "html.parser")

  # action & actionEn & firstImg
  actions = root.find_all("div", class_="title")
  aTags = root.find_all("a")
  images = []

  for aTag in aTags:
    if aTag.get("style"):
      images.append(aTag)

  # print('images', images, len(images))
  # print('actions', actions, len(actions))

  for action, image in zip(actions, images):
    obj = {
      "action": action.contents[0],
      "actionEn": action.contents[1].string,
      "firstImg": image.get("style")[21:-1],
      "ranking": []
    }
    arr.append(obj)

  # ranking
  players = root.find_all("div", class_="player")
  numbers = root.find_all("div", class_="num")
  index = 0
  print('arr', arr)
  for player, number in zip(players, numbers):
    obj = {
      "name": player.find("a", class_="name").string,
      "team": player.find("a", class_="team").string,
      "data": number.string
    }

    arr[index]["ranking"].append(obj)
    print(arr[index])
    if len(arr[index]['ranking']) == 5:
      index += 1
  
  return arr