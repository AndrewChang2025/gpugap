import undetected_chromedriver as uc 
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from classes import GPU

options = uc.ChromeOptions()
options.headless=False # headless does not open browser when run
driver = uc.Chrome(options=options)
driver.get("https://www.videocardz.net")

# get links to all relevant gpus from videocardz.net website
amd = driver.find_element(By.CLASS_NAME, 'main-menu-submenu-amd')
nvidia = driver.find_element(By.CLASS_NAME, 'main-menu-submenu-nvidia')
intel = driver.find_element(By.CLASS_NAME, 'main-menu-submenu-intel')

def get_GPUs(submenu):
    gpu_links = []
    inner_cols = submenu.find_elements(By.CLASS_NAME, 'main-menu-submenu-inner-column')
    for inner_col in inner_cols:

        # do not want Mobile graphics cards
        series = inner_col.find_element(By.CLASS_NAME, 'main-menu-item-level2')
        if "Mobile" in series.get_attribute('text'):
            continue

        # only want desktop graphics cards
        gpus = inner_col.find_elements(By.CLASS_NAME, 'main-menu-item-level3')
        for gpu in gpus:
            gpu_links.append(gpu.get_attribute('href'))

    return gpu_links

def scrape_page(gpu_links):
    gpu_list = []
    for gpu_link in gpu_links:
        driver.get(gpu_link)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        g = GPU()
        g.name = soup.find('div', attrs={'id':'singletitle'}).find('h1').get_text()
        gpu_list.append(g)
    
    return gpu_list