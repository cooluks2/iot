from threading import Thread
import requests
import time

def getHtml(url):
    resp = requests.get(url)
    with open('./image.png', 'wb') as f:
        f.write(resp.content)
        
url ='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png'
t1 = Thread(target=getHtml, args=(url,))
t1.start()