import requests
from bs4 import BeautifulSoup
url = "https://www.ptt.cc/bbs/NBA/index.html"

# pretends to be a request made by the browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.findAll("div", class_="r-ent")

for a in articles:
    # titles
    title = a.find("div", class_="title")
    if title and title.a:
        title = title.a.text
    else:
        title = "No title"

    # popularity
    popularity = a.find("div", class_="nrec")
    if popularity and popularity.span:
        popularity = popularity.span.text
    else:
        popularity = "N/A"

    # date
    date = a.find("div", class_="date")
    if date:
        date = date.text
    else:
        date = "N/A"

    print(f"標題:{title} 人氣:{popularity} 日期:{date}")

# if(response.status_code == 200):
#     with open('output.html', 'w', encoding='utf-8') as f:
#         f.write(response.text)
#     print("Successfully write!")
# else:
#     print("Fail to write!")