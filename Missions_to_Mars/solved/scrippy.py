from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    time.sleep(5)
    redplanet = {}
     # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # results are returned as an iterable list
    results = soup.find_all('div', class_='list_text') 
     # Loop through returned results
    for result in results:
    # Error handling
        try:
        # Identify and return title of listing
            redplanet["title"] = result.find('div', class_='content_title').text
        # Identify and return price of listing
            redplanet["parg"] = result.find('div', class_='article_teaser_body').text
        except AttributeError as e:
            print(e)
        break
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find('div', class_='floating_text_area')
    # Use Beautiful Soup's find() method to navigate and retrieve attributes
    hrev = images.find('a',class_='showimg fancybox-thumbs')['href']
    redplanet["featured_image_url"]='https://spaceimages-mars.com/' + hrev
    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)
    html = browser.html
    tables = pd.read_html(url)
    comp=tables[0]
    comp.columns = ['', 'Mars', 'Earth']
    comp.loc[-1] = ['Description', '', '']
    comp.index = comp.index + 1  
    comp = comp.sort_index() 
    comp.set_index('', inplace=True)
    redplanet["comph"] = comp.to_html()
    cerberus={}
    schiaparelli={}
    syrtis={}
    valles={}
    url = 'https://marshemispheres.com/cerberus.html'
    browser.visit(url)
    time.sleep(5)
     # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    cer = soup.find('div', class_='wrapper') 
    hrez = cer.find('img',class_='wide-image')['src']
    cerberus["img_url"]='https://marshemispheres.com/' + hrez
    cerberus["title"] = cer.find('h2',class_='title').text
    url = 'https://marshemispheres.com/schiaparelli.html'
    browser.visit(url)
    time.sleep(5)
     # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    schiap = soup.find('div', class_='wrapper') 
    shrez = schiap.find('img',class_='wide-image')['src']
    schiaparelli["img_url"]='https://marshemispheres.com/' + shrez
    schiaparelli["title"] = schiap.find('h2',class_='title').text
    url = 'https://marshemispheres.com/syrtis.html'
    browser.visit(url)
    time.sleep(5)
     # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    syrtiz = soup.find('div', class_='wrapper') 
    syrez = syrtiz.find('img',class_='wide-image')['src']
    syrtis["img_url"]='https://marshemispheres.com/' + syrez
    syrtis["title"] = syrtiz.find('h2',class_='title').text
    url = 'https://marshemispheres.com/valles.html'
    browser.visit(url)
    time.sleep(5)
     # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    vallez = soup.find('div', class_='wrapper') 
    varez = vallez.find('img',class_='wide-image')['src']
    valles["img_url"]='https://marshemispheres.com/' + varez
    valles["title"] = vallez.find('h2',class_='title').text
    hemisphere_image_urls = []
    hemisphere_image_urls.append(cerberus)
    hemisphere_image_urls.append(schiaparelli)
    hemisphere_image_urls.append(syrtis)
    hemisphere_image_urls.append(valles)
    redplanet["hemisphere_image_urls"]=hemisphere_image_urls
    browser.quit()
    return redplanet

