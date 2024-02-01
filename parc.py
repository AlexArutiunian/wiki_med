import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent

path = "new.json"
path2 = "new2.json"

try:
    with open(path, "r", encoding="utf-8") as f:
        datas = json.load(f)
except Exception as e:
    print("Failed to read the file.")
    with open(path, "r", encoding="utf-8") as f:
        f.seek(0, 2)
        f.seek(max(f.tell() - 10, 0), 0)
        last_chars = f.read()
        print("Last 10 characters:", last_chars)

names = []

google_url = "https://www.google.com/search?q=wikipedia"

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
ua = UserAgent()
user_agent = ua.random
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=options)

for data in datas:
    try:
      name = data["page"]
      
      name = name.replace(" ", "+")
      names.append(name)

      search_url = google_url + name

      driver.get(search_url)
      time.sleep(2)  # Wait for page to load

      soup = BeautifulSoup(driver.page_source, "html.parser")
      links_ = soup.find_all("a")
      link_wiki = str()
      for l_ in links_:
          href = l_.get("href")

          if href != None and "https://en.wikipedia.org/wiki/" in href:
              link_wiki = href
              print(href)
              break
      data["wiki_link"] = link_wiki
      
      with open(path2, "w", encoding="utf-8") as f:
       # print(link_wiki)
        json.dump(datas, f, indent=2)
    except Exception as e:
      print(e)
      print("SOMETH BAD")
      continue

driver.quit()
