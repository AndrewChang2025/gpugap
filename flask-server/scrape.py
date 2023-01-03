import undetected_chromedriver as uc # videocardz.net is protected from bots 
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup 
import fuckit # Steam roll errors to stop massive try/except chains
from classes import *

options = uc.ChromeOptions()
options.headless=False # headless=True does not open browser when run
driver = uc.Chrome(options=options)
driver.get("https://www.videocardz.net")

# get vendor submenus from web scraping
amd = driver.find_element(By.CLASS_NAME, 'main-menu-submenu-amd')
nvidia = driver.find_element(By.CLASS_NAME, 'main-menu-submenu-nvidia')
intel = driver.find_element(By.CLASS_NAME, 'main-menu-submenu-intel')

# returns a list of videocardz.net GPU links 
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

# scrape page to obtain all GPU specs and returns a list of GPU dataclasses 
# add all spec data from videocardz.net, some unreleased gpus will be blank so fuckit 
@fuckit 
def scrape_page(gpu_links):
    gpu_list = []
    for gpu_link in gpu_links:
        driver.get(gpu_link)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        g = GPU()

        # add all data of GPU from videocardz.net and yes, I know it's terrible
        g.name = soup.find('div', attrs={'id':'singletitle'}).find('h1').get_text()
        g.manufacturer = soup.find('div', string='Manufacturer').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.series = soup.find('div', string='Original Series').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.announced = soup.find('div', string='Announcement Date').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.released = soup.find('div', string='Release Date').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.msrp = soup.find('div', string='Launch Price').find_next_sibling('div', attrs={'class':'value'}).get_text()
        
        g.model = soup.find('div', string='GPU Model').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.architecture = soup.find('div', string='Architecture').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.fab = soup.find('div', string='Fabrication Process').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.die = soup.find('div', string='Die Size').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.transistors = soup.find('div', string='Transistors Count').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.stream_processors = soup.find('div', string='Stream Processors').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.rt_cores = soup.find('div', string='Ray Tracing Cores').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.tmu = soup.find('div', string='TMUs').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.rop = soup.find('div', string='ROPs').find_next_sibling('div', attrs={'class':'value'}).get_text()
        
        g.base_clock = soup.find('div', string='Base Clock').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.game_clock = soup.find('div', string='Game Clock').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.boost_clock = soup.find('div', string='Boost Clock').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.memory_clock = soup.find('div', string='Memory Clock').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.eff_memory_clock = soup.find('div', string='Effective Memory Clock').find_next_sibling('div', attrs={'class':'value'}).get_text()
        
        g.mem_size = soup.find('div', string='Memory Size').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.mem_type = soup.find('div', string='Memory Type').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.mem_bus_width = soup.find('div', string='Memory Bus Width').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.mem_bandwidth = soup.find('div', string='Memory Bandwidth').find_next_sibling('div', attrs={'class':'value'}).get_text()

        g.directx = soup.find('div', string='DirectX').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.vulkan = soup.find('div', string='Vulkan').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.openGL = soup.find('div', string='OpenGL').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.openCL = soup.find('div', string='OpenCL').find_next_sibling('div', attrs={'class':'value'}).get_text()

        g.pixel_fillrate = soup.find('div', string='Pixel Fillrate').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.texture_fillrate = soup.find('div', string='Texture Fillrate').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.peak_FP32 = soup.find('div', string='Peak FP32').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.fp32_perf_per_watt = soup.find('div', string='FP32 Perf. per Watt').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.fp32_perf_per_mm2 = soup.find('div', string='FP32 Perf. per mm').find_next_sibling('div', attrs={'class':'value'}).get_text()
        
        g.interface = soup.find('div', string='Interface').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.length = soup.find('div', string='Length').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.height = soup.find('div', string='Height').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.power_connectors = soup.find('div', string='Power Connectors').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.tdp_tbp = soup.find('div', string='TDP/TBP').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.psu_rec = soup.find('div', string='Recommended PSU').find_next_sibling('div', attrs={'class':'value'}).get_text()

        g.display_port = soup.find('div', string='DisplayPort').find_next_sibling('div', attrs={'class':'value'}).get_text()
        g.hdmi = soup.find('div', string='HDMI').find_next_sibling('div', attrs={'class':'value'}).get_text()

        g.img_src = soup.find('a', attrs={'class':'imagelist-thumbnail mobx'}).get('href')

        gpu_list.append(g)
    
    return gpu_list



