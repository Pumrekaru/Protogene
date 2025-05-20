# QR to Webpage data Fetch

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
from pyzbar.pyzbar import decode
from PIL import Image
 
# Step 1: Decode QR from image
img = Image.open(r"C:\Users\Dell\Desktop\Python Scripts\DC_QR_Processing\input\DC_img5.jpg")
decoded = decode(img)
url = decoded[0].data.decode("utf-8")
print("✅ URL from QR:", url)
 
# Step 2: Setup Selenium to load page
service = Service(r"C:/WebDrivers/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)
 
# Step 3: Load and extract table data
driver.get(url)
time.sleep(3)
 
rows = driver.find_elements(By.XPATH, "//table//tr")
data = []
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if len(cells) == 2:
        key = cells[0].text.strip()
        val = cells[1].text.strip()
        data.append((key, val))
 
driver.quit()
 
# Step 4: Convert to DataFrame
df = pd.DataFrame(data, columns=["Field", "Value"])
print(df)