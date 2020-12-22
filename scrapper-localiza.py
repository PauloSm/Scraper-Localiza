from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

driver.get('https://www.localiza.com/brasil/pt-br/grupos-de-carros')

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//ds-car-group[5]")))

soup = BeautifulSoup(driver.page_source, 'html.parser')

driver.quit()

lista = []
names = soup.find_all(attrs={"class":"ds-car-group-text__group-name"})

for i in names:
    lista.append([i.string, i.find_next(attrs={"class": "ds-car-group-text__model-name"}).string,
                  i.find_next('img')['src']])
    if(len(lista) >= 5):
        break

df = pd.DataFrame(lista)
print(df)
