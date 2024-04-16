# ssl
import bs4
import json
import urllib.parse as parse
import urllib.request as req
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 連線取得 json 檔案

url = "https://www.cpbl.com.tw/standings/seasonaction"


def fetchDatas(kindCode=0, seasonCode=0):
    if (kindCode == 0) & (seasonCode == 0):
        request = req.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
            },
            method="POST",
        )
    else:
        postData = {"Kindcode": kindCode, "SeasonCode": seasonCode}

        postDataString = parse.urlencode(postData)
        postDataEncode = postDataString.encode("ascii")

        request = req.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
            },
            method="POST",
            data=postDataEncode,
        )

    with req.urlopen(request) as res:
        data = res.read().decode("utf-8")

    # 解析網頁原始碼 => 下載bs4 : pip3 install beautifulsoup4
    datas = []

    # rank
    root = bs4.BeautifulSoup(data, "html.parser")
    ranks = root.find_all("div", class_="rank")
    for rank in ranks:
        if rank.string != "排名":
            datas.append({"rank": rank.string})

    team_count = len(datas)
    count_ary = [i for i in range(team_count)]
    print("count_ary", count_ary)

    # team
    teams = root.find_all("div", class_="team-w-trophy")
    for team, count in zip(teams[1:], count_ary):
        datas[count]["team"] = team.a.string

    # allData
    nums = root.find_all("td", class_="num")

    numCount = 0
    for data in datas:
        for _ in range(4):
            if len(data) == 3:
                items = data["allData"]
            else:
                items = []
            items.append(nums[numCount].string)
            data["allData"] = items
            numCount += 1
        numCount += 10

    return datas
