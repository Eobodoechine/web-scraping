{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "c2fda22d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import pandas as pd\n",
    "import requests\n",
    "import pymongo\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "5789acd5",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 91.0.4472\n",
      "Get LATEST driver version for 91.0.4472\n",
      "Driver [/Users/eobodoechine/.wdm/drivers/chromedriver/mac64/91.0.4472.101/chromedriver] found in cache\n"
     ]
    }
   ],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "bf20ade2",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://redplanetscience.com/'\n",
    "browser.visit(url)\n",
    "time.sleep(1)\n",
    "redplanet = {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "822b9e97",
   "metadata": {},
   "outputs": [],
   "source": [
    " # HTML object\n",
    "html = browser.html\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "c5b78a12",
   "metadata": {},
   "outputs": [],
   "source": [
    "# results are returned as an iterable list\n",
    "results = soup.find_all('div', class_='list_text') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "6e095bdf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'title': 'MAVEN Maps Electric Currents around Mars that are Fundamental to Atmospheric Loss',\n",
       " 'parg': 'Five years after NASA’s MAVEN spacecraft entered into orbit around Mars, data from the mission has led to the creation of a map of electric current systems in the Martian atmosphere.'}"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " # Loop through returned results\n",
    "for result in results:\n",
    "    # Error handling\n",
    "    try:\n",
    "        # Identify and return title of listing\n",
    "        redplanet[\"title\"] = result.find('div', class_='content_title').text\n",
    "        # Identify and return price of listing\n",
    "        redplanet[\"parg\"] = result.find('div', class_='article_teaser_body').text\n",
    "    except AttributeError as e:\n",
    "        print(e)\n",
    "    break\n",
    "redplanet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "8ebb5e44",
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "url = 'https://spaceimages-mars.com/'\n",
    "browser.visit(url)\n",
    " # HTML object\n",
    "html = browser.html\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "533ff7a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'title': 'MAVEN Maps Electric Currents around Mars that are Fundamental to Atmospheric Loss',\n",
       " 'parg': 'Five years after NASA’s MAVEN spacecraft entered into orbit around Mars, data from the mission has led to the creation of a map of electric current systems in the Martian atmosphere.',\n",
       " 'featured_image_url': 'https://spaceimages-mars.com/image/featured/mars2.jpg'}"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "images = soup.find('div', class_='floating_text_area')\n",
    "# Use Beautiful Soup's find() method to navigate and retrieve attributes\n",
    "hrev = images.find('a',class_='showimg fancybox-thumbs')['href']\n",
    "redplanet[\"featured_image_url\"]='https://spaceimages-mars.com/' + hrev\n",
    "redplanet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "c4449422",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Mars</th>\\n      <th>Earth</th>\\n    </tr>\\n    <tr>\\n      <th></th>\\n      <th></th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Description</th>\\n      <td></td>\\n      <td></td>\\n    </tr>\\n    <tr>\\n      <th>Mars - Earth Comparison</th>\\n      <td>Mars</td>\\n      <td>Earth</td>\\n    </tr>\\n    <tr>\\n      <th>Diameter:</th>\\n      <td>6,779 km</td>\\n      <td>12,742 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 × 10^23 kg</td>\\n      <td>5.97 × 10^24 kg</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2</td>\\n      <td>1</td>\\n    </tr>\\n    <tr>\\n      <th>Distance from Sun:</th>\\n      <td>227,943,824 km</td>\\n      <td>149,598,262 km</td>\\n    </tr>\\n    <tr>\\n      <th>Length of Year:</th>\\n      <td>687 Earth days</td>\\n      <td>365.24 days</td>\\n    </tr>\\n    <tr>\\n      <th>Temperature:</th>\\n      <td>-87 to -5 °C</td>\\n      <td>-88 to 58°C</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url = 'https://galaxyfacts-mars.com/'\n",
    "tables = pd.read_html(url)\n",
    "comp=tables[0]\n",
    "comp.columns = ['', 'Mars', 'Earth']\n",
    "comp.loc[-1] = ['Description', '', '']\n",
    "comp.index = comp.index + 1  \n",
    "comp = comp.sort_index() \n",
    "comp.set_index('', inplace=True)\n",
    "comph = comp.to_html()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "id": "f75046dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<html lang=\"en\"><head>\n",
      "      <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n",
      "      <link rel=\"stylesheet\" type=\"text/css\" href=\"css/jquery-ui.css\">\n",
      "      <title>Astropedia Search Results | GUSS Astrogeology Science Center</title>\n",
      "      <meta name=\"description\" content=\"GUSS Astrogeology Science Center Astropedia search results.\">\n",
      "      <meta name=\"keywords\" content=\"GUSS,Astrogeology Science Center,Cartography,Geology,Space,Geological Survey,Mapping\">\n",
      "      <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n",
      "      <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, maximum-scale=1\">\n",
      "      <link rel=\"stylesheet\" media=\"screen\" href=\"css/main.css\">\n",
      "      <link rel=\"stylesheet\" media=\"print\" href=\"css/print.css\">\n",
      "\n",
      "      <link rel=\"icon\" type=\"image/x-ico\" href=\"#\">\n",
      "   </head>\n",
      "   <body id=\"results\">\n",
      "      <header>\n",
      "         <a href=\"#\" style=\"float:right;margin-top:10px;\" target=\"_blank\">\n",
      "         <img class=\"logo\" height=\"60\" src=\"images/usgs_logo_main_2x.png\" alt=\"USGS: Science for a Changing World\">\n",
      "         </a>\n",
      "         <a href=\"#\" style=\"float:right;margin-top:5px;margin-right:20px;\" target=\"_blank\">\n",
      "         <img class=\"logo\" height=\"65\" src=\"images/nasa-logo-web-med.png\" alt=\"NASA\">\n",
      "         </a>\n",
      "\n",
      "      </header>\n",
      "      <div class=\"wrapper\">\n",
      "         <div class=\"container\">\n",
      "            <div class=\"widget block bar\">\n",
      "               <a style=\"float:right;text-decoration:none;\" href=\"https://astrogeology.usgs.gov/search\">\n",
      "                  <img style=\"width:200px;border:none;float:right;\" src=\"images/astropedia-logo-main.png\" alt=\"Astropedia\">\n",
      "                  <div style=\"clear:both;font-size:.8em;float:right;color:#888;\">Lunar and Planetary Cartographic Catalog</div>\n",
      "               </a>\n",
      "               <div style=\"float:left;height:60px;\">\n",
      "               </div>\n",
      "            </div>\n",
      "            <div class=\"full-content\">\n",
      "               <section id=\"results-accordian\" class=\"block\">\n",
      "                  <div id=\"product-section\" data-section=\"product\" class=\"result-list\">\n",
      "                     <div class=\"accordian\">\n",
      "                        <h2>Products</h2>\n",
      "                        <span class=\"count\">4 Results</span>\n",
      "                        <span class=\"collapse\">Collapse</span>\n",
      "                     </div>\n",
      "                     <div class=\"collapsible results\">\n",
      "                        <div class=\"item\">\n",
      "                           <a href=\"cerberus.html\" class=\"itemLink product-item\"><img class=\"thumb\" src=\"images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png\" alt=\"Cerberus Hemisphere Enhanced thumbnail\"></a>\n",
      "\n",
      "                           <div class=\"description\">\n",
      "                              <a href=\"cerberus.html\" class=\"itemLink product-item\">\n",
      "\n",
      "                                 <h3>Cerberus Hemisphere Enhanced</h3>\n",
      "                              </a>\n",
      "                              <span class=\"subtitle\" style=\"float:left\">image/tiff 21 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br>\n",
      "                              <p>Mosaic of the Cerberus hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. This mosaic is composed of 104 Viking Orbiter images acquired…</p>\n",
      "                           </div>\n",
      "                           <!-- end description -->\n",
      "                        </div>\n",
      "                        <div class=\"item\">\n",
      "                           <a href=\"schiaparelli.html\" class=\"itemLink product-item\"><img class=\"thumb\" src=\"images/08eac6e22c07fb1fe72223a79252de20_schiaparelli_enhanced.tif_thumb.png\" alt=\"Schiaparelli Hemisphere Enhanced thumbnail\"></a>\n",
      "                           <div class=\"description\">\n",
      "                              <a href=\"schiaparelli.html\" class=\"itemLink product-item\">\n",
      "                                 <h3>Schiaparelli Hemisphere Enhanced</h3>\n",
      "                              </a>\n",
      "                              <span class=\"subtitle\" style=\"float:left\">image/tiff 35 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br>\n",
      "                              <p>Mosaic of the Schiaparelli hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. The images were acquired in 1980 during early northern…</p>\n",
      "                           </div>\n",
      "                           <!-- end description -->\n",
      "                        </div>\n",
      "                        <div class=\"item\">\n",
      "                           <a href=\"syrtis.html\" class=\"itemLink product-item\"><img class=\"thumb\" src=\"images/55a0a1e2796313fdeafb17c35925e8ac_syrtis_major_enhanced.tif_thumb.png\" alt=\"Syrtis Major Hemisphere Enhanced thumbnail\"></a>\n",
      "                           <div class=\"description\">\n",
      "                              <a href=\"syrtis.html\" class=\"itemLink product-item\">\n",
      "                                 <h3>Syrtis Major Hemisphere Enhanced</h3>\n",
      "                              </a>\n",
      "                              <span class=\"subtitle\" style=\"float:left\">image/tiff 25 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br>\n",
      "                              <p>Mosaic of the Syrtis Major hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. This mosaic is composed of about 100 red and violet…</p>\n",
      "                           </div>\n",
      "                           <!-- end description -->\n",
      "                        </div>\n",
      "                        <div class=\"item\">\n",
      "                           <a href=\"valles.html\" class=\"itemLink product-item\"><img class=\"thumb\" src=\"images/4e59980c1c57f89c680c0e1ccabbeff1_valles_marineris_enhanced.tif_thumb.png\" alt=\"Valles Marineris Hemisphere Enhanced thumbnail\"></a>\n",
      "                           <div class=\"description\">\n",
      "                              <a href=\"valles.html\" class=\"itemLink product-item\">\n",
      "                                 <h3>Valles Marineris Hemisphere Enhanced</h3>\n",
      "                              </a>\n",
      "                              <span class=\"subtitle\" style=\"float:left\">image/tiff 27 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br>\n",
      "                              <p>Mosaic of the Valles Marineris hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. The distance is 2500 kilometers from the surface of…</p>\n",
      "                           </div>\n",
      "                           <!-- end description -->\n",
      "                        </div>\n",
      "                     </div>\n",
      "                     <!-- end this-section -->\n",
      "                  </div>\n",
      "               </section>\n",
      "            </div>\n",
      "\n",
      "\t\t<div class=\"navigation clear\" style=\"display: none;\">\n",
      "\t\t\t\t  <a href=\"#\" onclick=\"showMain()\" class=\"itemLink product-item\">\n",
      "\t\t\t\t\t <h3>Back</h3>\n",
      "\t\t\t\t  </a>\n",
      "\t\t</div>\n",
      "         </div>\n",
      "\n",
      "         <footer>\n",
      "            <div class=\"left\">\n",
      "               <a href=\"#\">Search</a> |\n",
      "               <a href=\"#\">About</a> |\n",
      "               <a href=\"#\">Contact</a>\n",
      "            </div>\n",
      "            <div class=\"right\">\n",
      "               <a href=\"#\">GUSS Science Center</a>\n",
      "            </div>\n",
      "         </footer>\n",
      "      </div>\n",
      "      <div class=\"page-background\" style=\"\n",
      "         background:url('./images/mars.jpg');\n",
      "         filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(\n",
      "         src='./images/mars.jpg', sizingMethod='scale');\n",
      "         \"></div>\n",
      "      <script type=\"text/javascript\">\n",
      "         var baseUrl = \"\";\n",
      "\n",
      "\n",
      "\n",
      "      </script>\n",
      "      <script type=\"text/javascript\" src=\"js/jquery.min.js\"></script>\n",
      "      <script type=\"text/javascript\" src=\"js/jquery-ui.min.js\"></script>\n",
      "      <script type=\"text/javascript\" src=\"js/general.js\"></script>\n",
      "\n",
      "   \n",
      "</body></html>\n"
     ]
    }
   ],
   "source": [
    "url = 'https://marshemispheres.com/'\n",
    "browser.visit(url)\n",
    " # HTML object\n",
    "html = browser.html\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "print(html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "id": "d76cdf44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://marshemispheres.com/cerberus.html\n",
      "https://marshemispheres.com/schiaparelli.html\n",
      "https://marshemispheres.com/syrtis.html\n",
      "https://marshemispheres.com/valles.html\n"
     ]
    }
   ],
   "source": [
    "# results are returned as an iterable list\n",
    "titlez = soup.find_all('div', class_='item') \n",
    "for title in titlez:\n",
    "        # Identify and return title of listing\n",
    "        linkz = title.find('a')['href']\n",
    "        urls='https://marshemispheres.com/' + linkz\n",
    "        # Print results only if title, price, and link are available\n",
    "        print(urls)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "id": "610fdc9b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': [], 'img_url': []},\n",
       " {'title': [], 'img_url': []},\n",
       " {'title': [], 'img_url': []},\n",
       " {'title': [], 'img_url': []}]"
      ]
     },
     "execution_count": 185,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cerberus={\"title\":[],\"img_url\":[]}\n",
    "schiaparelli={\"title\":[],\"img_url\":[]}\n",
    "syrtis={\"title\":[],\"img_url\":[]}\n",
    "valles={\"title\":[],\"img_url\":[]}\n",
    "hemisphere_image_urls = []\n",
    "hemisphere_image_urls.append(cerberus)\n",
    "hemisphere_image_urls.append(schiaparelli)\n",
    "hemisphere_image_urls.append(syrtis)\n",
    "hemisphere_image_urls.append(valles)\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "id": "3edd35b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://marshemispheres.com/cerberus.html'\n",
    "browser.visit(url)\n",
    " # HTML object\n",
    "html = browser.html\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "cer = soup.find('div', class_='wrapper') \n",
    "hrez = cer.find('img',class_='wide-image')['src']\n",
    "cerli='https://marshemispheres.com/' + hrez\n",
    "cert = cer.find('h2',class_='title').text\n",
    "cerberus[\"title\"].append(cert)\n",
    "cerberus[\"img_url\"].append(cerli)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "id": "bb557a59",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<html lang=\"en\"><head>\n",
      "    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n",
      "    <link rel=\"stylesheet\" type=\"text/css\" href=\"css/jquery-ui.css\">\n",
      "    <title>Astropedia Search Results | GUSS Astrogeology Science Center</title>\n",
      "    <meta name=\"description\" content=\"GUSS Astrogeology Science Center Astropedia search results.\">\n",
      "    <meta name=\"keywords\" content=\"GUSS,Astrogeology Science Center,Cartography,Geology,Space,Geological Survey,Mapping\">\n",
      "    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n",
      "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, maximum-scale=1\">\n",
      "    <link rel=\"stylesheet\" media=\"screen\" href=\"css/main.css\">\n",
      "    <link rel=\"stylesheet\" media=\"print\" href=\"css/print.css\">\n",
      "\n",
      "    <link rel=\"icon\" type=\"image/x-ico\" href=\"#\">\n",
      "</head>\n",
      "\n",
      "<body id=\"results\">\n",
      "    <header>\n",
      "        <a href=\"#\" style=\"float:right;margin-top:10px;\" target=\"_blank\">\n",
      "            <img class=\"logo\" height=\"60\" src=\"images/usgs_logo_main_2x.png\" alt=\"USGS: Science for a Changing World\">\n",
      "        </a>\n",
      "        <a href=\"#\" style=\"float:right;margin-top:5px;margin-right:20px;\" target=\"_blank\">\n",
      "            <img class=\"logo\" height=\"65\" src=\"images/nasa-logo-web-med.png\" alt=\"NASA\">\n",
      "        </a>\n",
      "\n",
      "    </header>\n",
      "    <div class=\"wrapper\">\n",
      "        <div class=\"container\">\n",
      "            <div class=\"widget block bar\">\n",
      "                <a style=\"float:right;text-decoration:none;\" href=\"https://astrogeology.usgs.gov/search\">\n",
      "                    <img style=\"width:200px;border:none;float:right;\" src=\"images/astropedia-logo-main.png\" alt=\"Astropedia\">\n",
      "                    <div style=\"clear:both;font-size:.8em;float:right;color:#888;\">Lunar and Planetary Cartographic\n",
      "                        Catalog</div>\n",
      "                </a>\n",
      "                <div style=\"float:left;height:60px;\">\n",
      "                </div>\n",
      "            </div>\n",
      "<!--==============================================================-->\n",
      "\n",
      "        <div id=\"wide-image\" class=\"wide-image-wrapper \">\n",
      "\n",
      "            <div class=\"downloads\">\n",
      "                <img class=\"thumb\" src=\"images/08eac6e22c07fb1fe72223a79252de20_schiaparelli_enhanced.tif_thumb.png\">\n",
      "                <h3>Download</h3>\n",
      "                <ul>\n",
      "\n",
      "                    <li><a target=\"_blank\" href=\"images/schiaparelli_enhanced-full.jpg\">Sample</a> (jpg) 1024px wide\n",
      "                    </li>\n",
      "                    <li><a target=\"_blank\" href=\"images/schiaparelli_enhanced.tif\">Original</a> (tif<span class=\"tooltip word-tif\" title=\"\"></span>) 35 MB</li>\n",
      "                </ul>\n",
      "            </div>\n",
      "\n",
      "            <img class=\"wide-image\" src=\"images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg\">\n",
      "            <a id=\"wide-image-toggle\" class=\"open-toggle\" href=\"#open\">Open</a>\n",
      "        </div>\n",
      "        <div class=\"cover\">\n",
      "            <h2 class=\"title\">Schiaparelli Hemisphere Enhanced</h2>\n",
      "            <p>Mosaic of the Schiaparelli hemisphere of Mars projected into point perspective, a view similar to that\n",
      "                which one would see from a spacecraft. The images were acquired in 1980 during early northern summer on\n",
      "                Mars. The center of this image is near the impact crater Schiaparelli (latitude -3, longitude 343) The\n",
      "                limits of this mosaic are approximately latitude -60 to 60 and longitude 260 to 30. The color variations\n",
      "                have been enhanced by a factor of two, and the large-scale brightness normalized by large-scale\n",
      "                filtering.</p>\n",
      "            <!--  <div class=\"downloads\">\n",
      "                     <img class=\"thumb\" src=\"images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png\">\n",
      "                     <h3>Download</h3>\n",
      "                     <ul>\n",
      "                        <li><a target=\"_blank\" href=\"images/full.jpg\">Sample</a> (jpg) 1024px wide</li>\n",
      "                        <li><a target=\"_blank\" href=\"images/cerberus_enhanced.tif\">Original</a> (tif<span class=\"tooltip word-tif\" title=\"\"></span>) 21 MB</li>\n",
      "                     </ul>\n",
      "                  </div> -->\n",
      "            <div class=\"description\">\n",
      "                <dl>\n",
      "                    <dt>Mimetype</dt>\n",
      "                    <dd>image/tiff</dd>\n",
      "                    <dt>Filename</dt>\n",
      "                    <dd><a href=\"images/schiaparelli_enhanced.tif\">schiaparelli_enhanced.tif<span class=\"tooltip word-tif\" title=\"\"></span></a></dd>\n",
      "                    <dt>Originator</dt>\n",
      "                    <dd></dd>\n",
      "                    <dt>Group</dt>\n",
      "                    <dd></dd>\n",
      "                    <dt>Added to Astropedia</dt>\n",
      "                    <dd>29 September 2011</dd>\n",
      "                    <dt>Modified</dt>\n",
      "                    <dd>3 November 2017</dd>\n",
      "                </dl>\n",
      "            </div>\n",
      "        </div>\n",
      "\n",
      "<!--==============================================================-->\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "            <div class=\"navigation clear\">\n",
      "                <a href=\"index.html\" class=\"itemLink product-item\">\n",
      "                    <h3>Back</h3>\n",
      "                </a>\n",
      "            </div>\n",
      "        </div>\n",
      "\n",
      "        <footer>\n",
      "            <div class=\"left\">\n",
      "                <a href=\"#\">Search</a> |\n",
      "                <a href=\"#\">About</a> |\n",
      "                <a href=\"#\">Contact</a>\n",
      "            </div>\n",
      "            <div class=\"right\">\n",
      "                <a href=\"#\">GUSS Science Center</a>\n",
      "            </div>\n",
      "        </footer>\n",
      "    </div>\n",
      "    <div class=\"page-background\" style=\"\n",
      "         background:url('./images/mars.jpg');\n",
      "         filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(\n",
      "         src='./images/mars.jpg', sizingMethod='scale');\n",
      "         \"></div>\n",
      "    <script type=\"text/javascript\">\n",
      "        var baseUrl = \"\";\n",
      "\n",
      "\n",
      "\n",
      "    </script>\n",
      "    <script type=\"text/javascript\" src=\"js/jquery.min.js\"></script>\n",
      "    <script type=\"text/javascript\" src=\"js/jquery-ui.min.js\"></script>\n",
      "    <script type=\"text/javascript\" src=\"js/general.js\"></script>\n",
      "    <script type=\"text/javascript\" src=\"js/app.js\"></script>\n",
      "\n",
      "\n",
      "\n",
      "</body></html>\n"
     ]
    }
   ],
   "source": [
    "url = 'https://marshemispheres.com/schiaparelli.html'\n",
    "browser.visit(url)\n",
    " # HTML object\n",
    "html = browser.html\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "schiap = soup.find('div', class_='wrapper') \n",
    "shrez = schiap.find('img',class_='wide-image')['src']\n",
    "schi='https://marshemispheres.com/' + shrez\n",
    "schrelli = schiap.find('h2',class_='title').text\n",
    "schiaparelli[\"title\"].append(schrelli)\n",
    "schiaparelli[\"img_url\"].append(schi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 188,
   "id": "e353356a",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://marshemispheres.com/syrtis.html'\n",
    "browser.visit(url)\n",
    " # HTML object\n",
    "html = browser.html\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "syrtiz = soup.find('div', class_='wrapper') \n",
    "syrez = syrtiz.find('img',class_='wide-image')['src']\n",
    "syi='https://marshemispheres.com/' + syrez\n",
    "syrt = syrtiz.find('h2',class_='title').text\n",
    "syrtis[\"title\"].append(syrt)\n",
    "syrtis[\"img_url\"].append(syi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 189,
   "id": "63197f66",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://marshemispheres.com/valles.html'\n",
    "browser.visit(url)\n",
    " # HTML object\n",
    "html = browser.html\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "vallez = soup.find('div', class_='wrapper') \n",
    "varez = vallez.find('img',class_='wide-image')['src']\n",
    "vali='https://marshemispheres.com/' + varez\n",
    "vart = vallez.find('h2',class_='title').text\n",
    "valles[\"title\"].append(vart)\n",
    "valles[\"img_url\"].append(vali)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "id": "8d88748c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': ['Cerberus Hemisphere Enhanced'],\n",
       "  'img_url': ['https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg']},\n",
       " {'title': ['Schiaparelli Hemisphere Enhanced'],\n",
       "  'img_url': ['https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg']},\n",
       " {'title': ['Syrtis Major Hemisphere Enhanced'],\n",
       "  'img_url': ['https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg']},\n",
       " {'title': ['Valles Marineris Hemisphere Enhanced'],\n",
       "  'img_url': ['https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg']}]"
      ]
     },
     "execution_count": 190,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "id": "ba034460",
   "metadata": {},
   "outputs": [],
   "source": [
    "    browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "id": "7f879e1b",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "'return' outside function (<ipython-input-193-d9ef57e85fb5>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-193-d9ef57e85fb5>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    return hemisphere_image_urls\u001b[0m\n\u001b[0m                                ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m 'return' outside function\n"
     ]
    }
   ],
   "source": [
    "return hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "77250925",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:PythonData] *",
   "language": "python",
   "name": "conda-env-PythonData-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
