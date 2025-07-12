# Varzesh3 News Link & Image Extractor (Unified Script Version)
This project is a Python-based scraper that extracts non-video news article links from the Varzesh3 homepage and downloads the main news images from each article. It's a unified version that runs both steps in one sequence using BeautifulSoup and requests.
# What It Does?
### Step1 : Link Scraping 

- Visits the homepage of Varzesh3

- Locates news blocks (div.widget.news)

- Extracts all `<a>` tags that do not link to videos

- Saves the result in links.txt

### Step2 : Image Downloading

- Reads all news links from links.txt

- Visits each news article

- Extracts the main image inside the .news-main-image block

- Downloads and saves the image in the imagess/ directory
# installation
### Make a venv by using:

python -m venv .venv

### Active venv by using:

.venv\scripts\activate
### Install the dependencies using pip:

pip install requests

pip install bs4

# How to Use?

1. Make sure you have a folder named imagess/ in the same directory as your script

2. Run the script at terminal (let’s say it’s saved as varzesh3_scraper.py) :
python varzesh3_scraper.py

3. After execution:

links.txt will contain all non-video news article URLs.

imagess/ will contain all the downloaded images.

# Code Overview

🔗 Part 1: Scrape Links

```python
web = requests.get("https://www.varzesh3.com")
soup = BeautifulSoup(web.content)
dvs = soup.find_all("div", {"class":"widget news"})
links = dvs[1].find_all("a") + dvs[2].find_all("a")
```
Filters out any links that contain video.varzesh3.com

Writes valid links to links.txt

 🔗Part 2: Download Main Images

```python
f1 = open("links.txt", "rt", encoding="utf-8")
...
img = soup.find_all("div", {"class":"news-main-image"})[0].find_all("img")[0]["src"]
```
For each link, finds the primary news image

Downloads and saves it using the image filename from URL

# 📁 Output Example

Text File : links.txt

https://www.varzesh3.com/news/2000012/some-article
https://www.varzesh3.com/news/2000021/another-article
...

Images Folder: imagess/

15093912.jpg
15093955.jpg
...

## Notes & Tips

The script assumes div.widget.news and div.news-main-image structures are consistent