from flask import Flask, request
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import os

app = Flask(__name__)

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'GET':
        data = request.get_json()
        return data
    else:
        data = request.get_json()
        data['message'] = 'received'
        return data

@app.route('/get_all_images', methods=['GET'])
def get_all_images():
    data = request.get_json()
    keyword, page_num = data.get('keyword'), int(data.get('pages', 1))
    current_page = 1
    current_img_qty = 0
    driver = webdriver.Chrome()

    if not os.path.exists('images'):
        os.makedirs('images')

    while current_page != page_num:
        driver.get(f'https://gettyimages.com/search/2/image-film?family=creative&phrase={keyword}&page={current_page}')
        soup = bs(driver.page_source, "html.parser")
        for element in soup.find_all('picture'):
            
            link = element.find('img')['src'] # Get Image Url
            img = requests.get(link)

            current_img_qty += 1  
            with open(f'images/image{current_img_qty}.png', 'wb') as f: # Download Image
                f.write(img.content)
                print(f'Image {current_img_qty} Downloaded')

        current_page += 1 

    return {
        'images_found': current_img_qty, 
        'keyword': keyword, 
        'pages_processed': current_page
    } 




    

if __name__ == "__main__":
    """
    curl -X GET 'http://localhost:8000/verify' -H 'Content-Type: application/json' -d '{"data":123}'
    
    Implement a scraper which will fetch all image source URLs on Getty Images given a search term and "N" number of pages. Then leverage multithreading to parallelize the process with a given max number of workers. 
    
    https://developers.gettyimages.com/docs/authorization/
    """
    app.run(port=8000, debug=True)