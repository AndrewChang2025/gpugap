import requests 
import pandas as pd 
from bs4 import BeautifulSoup

URL = "https://www.tomshardware.com/reviews/gpu-hierarchy,4388.html"
page = requests.get(URL)    
soup = BeautifulSoup(page.content, 'html.parser')

hierarchies = {}

#finds only the most relevant lists: rasterization and ray tracing
for hierarchy in soup.find_all('div', attrs={'class': 'table__container'}, limit=2): 

    h = hierarchy.find('caption').string 
    hierarchies[h] = [] 

    for gpu in hierarchy.find_all('strong'): #gpu names are bolded 
        try:
            hierarchies[h].append(gpu.find('a').string)
        except:
            pass

df = pd.DataFrame.from_dict(hierarchies, orient='index')
df = df.transpose() #pandas gets mad if you have missing rows
df.to_csv('tomshardware_best_gpus.csv', index=False)

pd.set_option('display.max_rows', None) 
database = pd.read_csv('tomshardware_best_gpus.csv')
print(database)
