##############################################################################
# Author: Tehran Guluzade
# Date: 2022-12-22
# Description: File scrapper from url and subdirectories
#
# Libraries/Modules:
# - requests
# - BeautifulSoup
#
# Functions:
# - Url validation checker
# - Folder creator
# - Files downloader
#
# Usage:
# - url = 'http://slav0nic.org.ua/static/books/python/'
# - save_path = 'downloaded_files'
# - python scrapper.py
##############################################################################

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_all_files(url, save_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    base_url = url

    for link in soup.find_all('a'):
        href = link.get('href')

        if href:
            new_url = urljoin(base_url, href)

            if is_valid_url(new_url) and new_url.startswith(url):
                if new_url.endswith('/'):
                    subdirectory = os.path.join(save_path, href.strip('/'))
                    create_directory(subdirectory)
                    get_all_files(new_url, subdirectory)
                else:
                    download_file(new_url, save_path)

def download_file(url, save_path):
    local_filename = url.split('/')[-1]
    
    if not set('?*|"<>:').isdisjoint(local_filename):
        print(f"Skipping invalid file name {local_filename}")
        return
    
    local_file_path = os.path.join(save_path, local_filename)
    print(f"Downloading {local_filename}...")

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    print(f"{local_filename} downloaded.")

url = 'http://slav0nic.org.ua/static/books/python/'
save_path = 'downloaded_files'
create_directory(save_path)
get_all_files(url, save_path)
