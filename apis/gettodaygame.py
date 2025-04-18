# ssl
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

import requests

# 連線取得 json 檔案
import urllib.request as req
import urllib.parse as parse
import json

# url
url = "https://www.cpbl.com.tw/home/getdetaillist"


def fetchDatas(gameDate):
    #     postData = {
    #     "GameDate": gameDate
    #   }

    headers = {
        "User-Agent": "/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }
    response = requests.post(url, headers=headers)

    print("Response Text:")
    print(response.text)

    try:
        json_data = response.json()  # 轉換為 Python 字典
        print("\nResponse JSON:")
        print(json_data)
    except ValueError:
        print("\nResponse is not in JSON format.")

    return json_data

    #   postDataString = parse.urlencode(postData)
    #   postDataEncode = postDataString.encode('ascii')

    #   request = req.Request(url, headers={
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    #     "RequestVerificationToken": "XKTE4BqMnSGXivhnltTrzzwz1dyQWCnBbfGb_5o3INWlFCfcGUrjx9XiXVm1DRt_mO16b9mDx9FVNiilzfUKpCqzLd41:E0WVOVgaW3ZZ4pik_mG9FHeBRxBtSlMmdjkvKhSo_iwDUOKiaeGUNidWmjhLlDgwHdYcHzOtGVgkFd63R3i_brvdEMs1",
    #     "X-Requested-With": "XMLHttpRequest"
    #   }, method='POST', data=postDataEncode)

    #   with req.urlopen(request) as res:
    #     data = res.read().decode('utf-8')

    if data == None:
        data = "0"

    return data
