import sys
import os
import pprint
import time
import urllib.error
import urllib.request

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

def take_img(url, path):
    i = 0
    type_img = ["jpg", "png", "gif", "jpeg", "bmp"]
    download_file(url, path + "img " + str(i))
    

take_img(sys.argv[1], "img/")
