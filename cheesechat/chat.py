import re
import requests
import json


def send_text(body) -> str:
    url = "https://dance.whu.edu.cn/api/conversation/"

    f = open("config.json", "r+")
    cfg_orig = f.read()
    cfg = json.loads(cfg_orig)
    f.close()
    headers = cfg["headers"]

    resp = requests.post(url, json=body, headers=headers, verify=False)
    f = open("resp.html", "w+", encoding="utf-8")
    patt = re.findall(r"{\"content\":.*?}", resp.text)
    string = ""
    for i in patt:
        content = json.loads(i)
        string += str(content["content"])
    print(string)
    f.write(string)
    f.close()
    return string
