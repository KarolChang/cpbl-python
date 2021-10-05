import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request as req
import bs4

url = "https://www.cpbl.com.tw/standings/season"

def fetchDatas():
  request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
  })
  with req.urlopen(request) as res:
    data = res.read().decode("utf-8")

  # 解析網頁原始碼 => 下載bs4 : pip3 install beautifulsoup4
  datas = [{}] * 5

  # rank
  root = bs4.BeautifulSoup(data, "html.parser")
  ranks = root.find_all("div", class_="rank")
  count = 0
  for rank in ranks:
    if(rank.string != '排名'):
      datas[count] = {'rank': rank.string}
      count += 1

  # team
  teams = root.find_all("div", class_="team-w-trophy")
  count = 0
  for team in teams:
    if team.a:
      datas[count]['team'] = team.a.string
      count += 1
  
  # allData
  nums = root.find_all("td", class_="num")

  numCount = 0
  
  print(nums[0].string)

  for data in datas:
    for i in range(4):
      if len(data) == 3:
        items = data['allData']
      else:
        items = []
      items.append(nums[numCount].string)
      data['allData'] = items
      numCount += 1
    numCount += 9

  # print(datas)
  return datas