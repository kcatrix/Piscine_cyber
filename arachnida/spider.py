import re
import sys
import os
import pprint
import time
import urllib.error
import urllib.request

def download_file(url, dst_path):
    dst_path = dst_path + os.path.splitext(url)[1]
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

def get_image_tags(url):
   try:
        # Effectuer une requête GET pour obtenir le contenu de la page
        response = urllib.request.urlopen(url)
        
        # Vérifier si la requête a réussi
        if response.status == 200:
             html_content = response.read().decode('utf-8')
             image_urls = re.findall(r'(?i)(https?://\S+\.(?:jpg|png|gif|jpeg|bmp))', html_content)
             return image_urls
        else:
            return []
    
   except urllib.error.HTTPError as e:
        if e.code == 403:
            print("Erreur 403: Forbidden - Accès refusé à la ressource.")
        else:
            print("Erreur HTTP:", e.code)

def get_next_page_urls(url):
    try:
        response = urllib.request.urlopen(url)
        
        if response.status == 200:
            html_content = response.read().decode('utf-8')
            return (re.findall(r'(?i)<a\s+href=["\'](.*?)["\']', html_content))
        else:
            return []
    
    except urllib.error.HTTPError as e:
        if e.code == 403:
            print("Erreur 403: Forbidden - Accès refusé à la ressource.")
        else:
            print("Erreur HTTP:", e.code)


def take_img(url, path, depth):
    i = 0
    img_tags = get_image_tags(url)
    if img_tags:
    	for img in img_tags:
             download_file(img, path + "img_" + str(i))
             i += 1
    print(img_tags)
    # download_file(url, path + "img " + str(i))
    if depth > 0:
        next_page_urls = get_next_page_urls(url)  # Fonction à implémenter pour obtenir les URL des pages suivantes
        print("next page = ", next_page_urls,  "\n")
        for next_page_url in next_page_urls:
            take_img(next_page_url, path, depth - 1)

depth = 1
take_img(sys.argv[1], "img/", depth)
