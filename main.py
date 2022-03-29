debugging = 0

from os import access
import requests
import json

student_info = []
with open("student_info.json", "r", encoding="utf-8") as fp:
    student_info = json.load(fp)

proxies = {"http": None, "https": None}


def getIDInfo(nid):
    url = "https://qcsh.h5yunban.com/youth-learning/cgi-bin/common-api/organization/children?pid=" + nid
    res = json.loads(requests.get(url, timeout=3, proxies=proxies).text)
    if debugging:
        print(f'getIDInfo: {res}')
    if res.get("status") == 200:
        return res.get("result")
    else:
        return res


def checkConfig(cardNo, nid):
    if len(cardNo) == 0:
        return {"status": False, "message": "学号不可为空"}
    if len(nid) == 0:
        return {"status": False, "message": "nid不可为空"}
    res = getIDInfo(nid)
    if len(res) != 0:
        return {"status": False, "message": f"nid异常：{res}"}
    return {"status": True}


def getCourse(accessToken):
    url = "https://qcsh.h5yunban.com/youth-learning/cgi-bin/common-api/course/current?accessToken=" + accessToken
    res = json.loads(requests.get(url, timeout=3, proxies=proxies).text)
    try:
        if debugging:
            print(f'getCourse: {res["result"]["id"]}')
        return {"status": True, "message": res["result"]["id"]}
    except:
        return {"status": False, "message": "查询课程致未知错误"}


def getStudy(course, nid, subOrg, cardNo, accessToken):
    url = "https://qcsh.h5yunban.com/youth-learning/cgi-bin/user-api/course/join?accessToken=" + accessToken
    data = {"course": course, "nid": nid, "cardNo": cardNo}
    if len(subOrg) > 0:
        data["subOrg"] = subOrg
    res = json.loads((requests.post(url=url, data=json.dumps(data), timeout=3, proxies=proxies)).text)
    if debugging:
        print(f'getStudy: {res}')
    if res.get("status") == 200:
        return {"status": True, "message": ""}
    else:
        return {"status": False, "message": res}


def getToken(openid):
    url = 'https://qcsh.h5yunban.com/youth-learning/cgi-bin/login/we-chat/callback'
    headers = {'Content-Type': 'text/plain'}
    openId = {'appid': 'wxa693f4127cc93fad', 'openid': openid}
    Token_raw = requests.get(url=url, params=openId, headers=headers, timeout=3, proxies=proxies).text
    Token = Token_raw.replace('"', "'").split("'")
    if debugging:
        print(f'getToken_raw: {Token_raw}')
    for i in Token:
        if '-' in i:
            if debugging:
                print(f'getToken: {i}')
            return {"status": True, "message": i}
    return {"status": False, "message": Token_raw}


if __name__ == '__main__':
    cour = None
    if student_info == []:
        print("没有获取到学生信息！")
        exit()

    for student in student_info:
        cardNo = student["cardNo"]
        subOrg = student["subOrg"] if "subOrg" in student else ""
        nid = student["nid"]
        openid = student["openid"]
        Token = getToken(openid)
        if Token["status"] == False:
            print(f'{cardNo} 登录失败：{Token["message"]}')
            continue
        else:
            Token = Token["message"]
        if cour == None:
            cour = getCourse(Token)
            if cour["status"] == True:
                cour = cour["message"]
            else:
                print(f'获取最新课程失败：{cour["message"]}')
                exit()

        check = checkConfig(cardNo, nid)
        if check["status"] == True:
            result = getStudy(cour, nid, subOrg, cardNo, Token)
            if result["status"] == True:
                print(f'{cardNo} 打卡成功')
            else:
                print(f'{cardNo} 打卡失败：{result["message"]}')
        else:
            print(f'{cardNo} 检测失败：{check["message"]}')
