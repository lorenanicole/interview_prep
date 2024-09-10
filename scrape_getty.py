from bs4 import BeautifulSoup as bs
from selenium import webdriver
import os
import threading
from concurrent.futures import ThreadPoolExecutor
import requests

# def get_all_images(keyword, page_num):
#     current_page = 1
#     current_img_qty = 0
#     driver = webdriver.Chrome()

#     # if not os.path.exists('images'):
#     #     os.makedirs('images')

#     found_imgs = []

#     while current_page != page_num:
#         driver.get(f'https://gettyimages.com/search/2/image-film?family=creative&phrase={keyword}&page={current_page}')
#         soup = bs(driver.page_source, "html.parser")
#         for element in soup.find_all('picture'):
            
#             link = element.find('img')['src'] # Get Image Url
#             # img = requests.get(link)

#             current_img_qty += 1  
#             found_imgs.append(link)
#             # with open(f'images/image{current_img_qty}.png', 'wb') as f: # Download Image
#             #     f.write(img.content)
#             #     print(f'Image {current_img_qty} Downloaded')

#         current_page += 1 

#     print(f'Image {current_img_qty} Downloaded')
          
#     return {
#         'images_found': current_img_qty, 
#         'keyword': keyword, 
#         'pages_processed': current_page
#     } 


def get_all_images_threaded(url):
    current_page = 1
    current_img_qty = 0
    driver = webdriver.Chrome()

    found_imgs = []

    driver.get(url)
    soup = bs(driver.page_source, "html.parser")
    for element in soup.find_all('picture'):
        
        link = element.find('img')['src'] # Get Image Url

        current_img_qty += 1  
        found_imgs.append(link)

    print(f'Image links {current_img_qty} found for url {url}.')
          
    return found_imgs

if __name__ == '__main__':
    keyword = 'programming'
    num_pages = 6
    found_img_urls = []
    image_urls = [
        f'https://gettyimages.com/search/2/image-film?family=creative&phrase={keyword}&page={current_page}'
        for current_page in range(1,num_pages+1)
    ]

    with ThreadPoolExecutor(max_workers=2) as executor:
        iterator = executor.map(get_all_images_threaded, image_urls)
        for result in iterator:
            print(f'pending:{executor._work_queue.qsize():2d} threads:{len(executor._threads)}')
            if result:
                found_img_urls += result
    
    distinct_links = list(set(found_img_urls))
    distinct_links = len(distinct_links)
    print(f"{distinct_links} distinct image links found.")