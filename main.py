import requests
import bs4
import json
def handle(data):
    give = {
        "authority": "mc.yandex.ru",
        "method": "POST",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "ru,en-US;q=0.9,en;q=0.8",
        "origin": "https://zaebike.com",
        "referer": "https://zaebike.com/",
        "sec-ch-ua": "\"Not:A-Brand\";v=\"24\", \"Chromium\";v=\"134\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Linux",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "sec-fetch-storage-access": "active",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}
    output = dict()
    sitemaps = json.loads(data)
    for i in sitemaps:
        pages = requests.get(i, headers = give)
        iSoup = bs4.BeautifulSoup(pages.text, "xml")
        for j in iSoup.find_all("loc"):
            information = requests.get(j.text, headers = give)
            jSoup = bs4.BeautifulSoup(information.text, "html.parser")
            try:
                output[jSoup.find("title").text] = jSoup.get_text(separator = ". ", strip = True)
            except:
                pass
    return json.dumps(output, ensure_ascii=False)
