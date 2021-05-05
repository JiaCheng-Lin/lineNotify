import requests
import time

def lineNotifyMessage(token, msg, img):
    headers = {
        "Authorization": "Bearer " + token
        # "Content-Type" : "application/x-www-form-urlencoded"  //增加後無法傳輸圖片
    }

    payload = {
      'message': msg
      # 'imageThumbnail': img, # http, url
      # 'imageFullsize': img # http, url
      # 'stickerPackageId': 2,  #sticker
      # 'stickerId': 519
    }

    files = {'imageFile': open(img, 'rb')}  # local image 
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload, files = files)
    return r.status_code

if __name__ == '__main__':
  token =  # 'txP5BLNUlmN55K6BNPEcu0zVZ2Pfxd9CYDVRDe21Ntf' # 'nzMzAUlqBfeQdIfIqxr28NbnxfrlAlDL36fWlVVOEYb'

  nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
  message = '\n老人跌倒！！！\n' + str(nowTime)

  # url = 'https://memes.tw/wtf/405443'  
  # img = "https://memeprod.sgp1.digitaloceanspaces.com/user-wtf/1619538805611.jpg"
  img = "C:/Users/TOBY/Desktop/abei.jpg"
  
  lineNotifyMessage(token, message, img)