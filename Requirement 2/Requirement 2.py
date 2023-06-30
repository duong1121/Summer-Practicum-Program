import requests
from bs4 import BeautifulSoup
from PIL import Image
import io
import os
import random
import numpy as np

# Function to scrape and download images from a given URL

def scrape_images(url, category, LIST_img=[], LIST_name=[]):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    # Find all image tags in the HTML
    images = soup.find_all('img')
    
    count = 0
    for image in images:
        try:
            # Get the image URL from the src attribute
            img_url = image['src']
            if img_url.startswith('data:'):
                # Ignore images with invalid data URLs
                continue
            # Send an HTTP GET request to download the image content
            response = requests.get(img_url)
            img = Image.open(io.BytesIO(response.content))

            # Resize the image to 300 x 300
            img = img.resize((300,300))
            
            # Save the image to the specified folder
            file_name = 'img_' + category + '_' + str(count) + '.jpg'

            LIST_img.append(img)
            LIST_name.append(file_name)
            count += 1

            # Stop the loop once 1000 images are saved
            if count == 1000:
                break
        except:
            continue

# Main function to scrape images from Google Images
def scrape_google_images():
    # Set up the image source URL
    LIST_img=[]
    LIST_name=[]
    url_true = ''  #Change url to where we want to download image
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    r = requests.get(url_true, headers=headers)

    folder_path = './imagess/'
    folder1_path = os.path.join(folder_path, 'Folder_1')
    folder2_path = os.path.join(folder_path, 'Folder_2')

    # Create the image folders 
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)
    if not os.path.isdir(folder1_path):
        os.mkdir(folder1_path)
    if not os.path.isdir(folder2_path):
        os.mkdir(folder2_path)

    # Scrape and download true images
    scrape_images(url_true, 'true', LIST_img, LIST_name)

    url_ai = ''  #Change url to where we want to download image
    # Scrape and download AI-generated images
    scrape_images(url_ai, 'AI-generated', LIST_img, LIST_name)

    # Shuffle images 
    if LIST_img and LIST_name:
        mapListTrain = list(zip(LIST_img, LIST_name))
        random.shuffle(mapListTrain)
        LIST_img, LIST_name = zip(*mapListTrain)

    count = 0
    for i in LIST_img:
        if(count<1000):
            img_rgb = LIST_img[count].convert('RGB')  # Convert to RGB mode
            img_rgb.save(os.path.join(folder1_path, LIST_name[count]), "JPEG")
        else:
            img_rgb = LIST_img[count].convert('RGB')  # Convert to RGB mode
            img_rgb.save(os.path.join(folder2_path, LIST_name[count]), "JPEG")
        count += 1

scrape_google_images()
