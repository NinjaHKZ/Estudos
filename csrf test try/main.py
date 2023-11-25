import urllib3


class getCookiesToken:
    def __init__(self, proxy="http://201.95.254.137:3128"):
        self.gmail = "xxxxx@gmail.com"
        self.senha = "xxxxxx"
        self.CSFRtoken = None
        self.CSFRmiddleToken = None
        self.proxy = urllib3.ProxyManager(proxy)

        self.getCSFRtokenURL = "https://my.waveapps.com/login/"
        self.loginInto = "https://my.waveapps.com/login/"
        
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"}
        self.dataPayload = None
        
    def ScrapCSFTtoken(self, url="https://my.waveapps.com/login/", middletoken=False, body=None, headers=None, use_proxy=False):
        httpmanager = urllib3 if use_proxy == False else self.proxy        
        self.CSFRtoken = httpmanager.request(url=url, method="GET", headers=headers, body=body)

        if middletoken == True:
            try:
                html = self.CSFRtoken.data.decode("utf-8")
                LineLocation = html.find('name="csrfmiddlewaretoken"', 0)
                LineEndLocation = html.find(">", LineLocation)
                
                self.CSFRmiddleToken = html[LineLocation:LineEndLocation].split(" ")[1].split("=")[1]
                del html, LineLocation, LineEndLocation
                print("CSFRmiddleTokken has been collected from html...")
            
            except IndexError:
                print("CSFRmiddleTokken has been", html)

        self.CSFRtokenFilter = self.CSFRtoken.headers.get_all("set-cookie")
        
        self.CSFRtoken = "".join(str(i) for i in self.CSFRtokenFilter)
        print(self.CSFRtoken)
        print("Cookies has been Scrapped.")


getCookiesToken(proxy="http://201.95.254.137:3128").ScrapCSFTtoken()
