#import packages
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#define url of pdfs and where they'll be downloaded
download_to_dir = "./tmp/"
base = "http://www.fairfaxmortgage.com"
uri = "/resources-forms.aspx"
url = base + uri

#read url and find all names and links to pdfs
response = urlopen(url).read()
soup = BeautifulSoup(response, "html.parser")
links = soup.find_all('a')
pdf_links = list()
for link in links:
    if 'pdf' in link.get('href'):
        print("yes")
        pdf_name = link.text
        pdf_link = base + link.get('href')
        pdf_links.append({"name": pdf_name, "url": pdf_url})

#download all pdf links
def download_pdf(pdf_name,pdf_url):
    if not os.path.exists(download_to_dir):
        os.makedirs(download_to_dir)
    response = urlopen(pdf_url).read()
    with open("./{}/{}.pdf".format(download_to_dir,pdf_name), 'wb') as f:
        f.write(response)
    #print("Completed")

for pdf in pdf_links:
    download_pdf(pdf["name"], pdf["url"])
    print(pdf_name,"downloaded to",download_to_dir)
