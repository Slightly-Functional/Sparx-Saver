import os
os.environ["PYPPETEER_CHROMIUM_REVISION"] = "1263111"
print(os.environ["PYPPETEER_CHROMIUM_REVISION"])

import requests_html, pyppeteer

print(pyppeteer.__chromium_revision__)

PAGE = "https://www.sparxmaths.com"

session = requests_html.HTMLSession()
response = session.get(PAGE)

response.html.render()

print(response.html.find("title")[0].text)
