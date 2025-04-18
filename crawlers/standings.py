from bs4 import BeautifulSoup
import requests

url = "https://www.cpbl.com.tw/standings/seasonaction"


def fetchDatas(kindCode=None, seasonCode=None):
    postData = (
        {"Kindcode": kindCode, "SeasonCode": seasonCode}
        if kindCode and seasonCode
        else {}
    )

    # 解析網頁原始碼
    datas = []

    web_data = requests.post(url, data=postData, headers={"User-Agent": "Mozilla/5.0"})

    root = BeautifulSoup(web_data.text, "html.parser")
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
