from threading import Thread
import requests
import time

def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), resp.text)
    
t1 = Thread(target=getHtml, args=('https://naver.com',))
t1.start()
