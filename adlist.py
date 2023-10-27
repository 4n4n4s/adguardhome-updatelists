"""AdList"""
import requests

class AdList:
    def __init__(self, url: str):
        print("Initialize AdList", url)
        self.url = url

    def get_new_filters(self):
        response = requests.get(self.url, timeout=10)
        if response.status_code != 200:
            print(response)
            print(response.text)

        adlines = response.text.split("\n")
        adlines.remove("")
        print ("got", len(adlines), "adlines from", self.url)
        return adlines
