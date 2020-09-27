import requests, json,base64

s = requests.Session ()

cookie = ""
if (cookie == ""):
    cookie=input ().strip ()

def main ():
    url1 = f'https://api.live.bilibili.com/sign/GetSignInfo'
    url2 = f'https://api.live.bilibili.com/sign/doSign'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        "Referer" : "https://live.bilibili.com/491741",
        "Accept-Encoding" : "gzip, deflate",
        "Cookie":cookie,
    }
    s.get (url1,headers=headers)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        "Referer" : "https://live.bilibili.com/491741",
        "cookie": cookie,
        "Accept-Encoding" : "gzip, deflate",
    }
    s.get (url2,headers=headers)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        "Referer" : "https://live.bilibili.com/491741",
        "Accept-Encoding" : "gzip, deflate",
        "Cookie":cookie,
    }
    
    response=s.get (url1,headers=headers)
    dec=json.loads (response.text)
    if dec ['data']['status']==1:
        print ("已签到！\n签到奖励："+dec ['data']['text']+"\n"+dec ['data']['specialText']+"\n")
    else:
        if dec ['data']['status']==-101:
            print ("失败！请检查 Cookie 是否过期！\n")
            exit (100)
        else:
            print ("网络故障，请重试！\n")
            exit (100)



if __name__ == "__main__":
    main ()

