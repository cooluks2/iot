import threading, requests, time

class HtmlGetter (threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        # 다중상속한 경우 ≒ super.__init__()
        self.url = url

    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), resp.text)

t = HtmlGetter('https://google.com')
t.start()

print("### End ###")