"""AdGuardHome"""
import requests

class AdGuadHome:
    def __init__(self, url: str, username: str, password: str):
        print("Initialize AdGuardHome", url, username)
        self.url = url
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.name_prefix = "[adlist]"

    def do_login(self):
        response = self.session.post(
            f"{self.url}/control/login",
            json={"name": self.username, "password": self.password})
        if response.status_code != 200:
            print(response)
            print(response.text)
            exit(0)
        if not "OK" in response.text:
            print("not logged in corrrectly.")
            exit(0)

    def get_filters(self, filters: str):
        response = self.session.get(f"{self.url}/control/filtering/status")
        if response.status_code != 200:
            print(response)
            print(response.text)
        if not filters in response.json():
            print("no filters")
            exit(0)

        result = response.json()[filters]
        return result if result else {}

    def get_current_whitelist_filters(self):
        return self.get_filters("whitelist_filters")

    def get_current_filters(self):
        return self.get_filters("filters")

    def remove_url(self, url: str, whitelist: bool):
        response = self.session.post(
            f"{self.url}/control/filtering/remove_url", 
            json={"url": url, "whitelist": whitelist})
        if response.status_code != 200:
            print(response)
            print(response.text)
        print(response.text)

    def add_url(self, url: str, whitelist: bool()):
        response = self.session.post(
            f"{self.url}/control/filtering/add_url", 
            json={"url": url, "name": f"{self.name_prefix} {self.url}", "whitelist": whitelist})
        if response.status_code != 200:
            print(response)
            print(response.text)
        print(response.text)
