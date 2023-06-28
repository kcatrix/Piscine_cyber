import re
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

def get_image_tags(url):
    # Effectuer une requête GET pour obtenir le contenu de la page
    response = urllib.request.urlopen(url)
    
    # Vérifier si la requête a réussi
    if response.status == 200:
         html_content = response.read().decode('utf-8')
         image_urls = re.findall(r'(?i)(https?://\S+\.(?:jpg|png|gif|jpeg|bmp))', html_content)
         return image_urls
    
    # Si la requête a échoué, retourner une liste vide
    return []

def take_img(url, path):
    i = 0
    img_tags = get_image_tags(url)
    download_file(img_tags[1], path + "img_" + str(i))
    i += 1
        
    
    print (img_tags)
    # download_file(url, path + "img " + str(i))
    

take_img(sys.argv[1], "img/")
