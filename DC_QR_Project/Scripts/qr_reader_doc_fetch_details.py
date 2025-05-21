from qreader import QReader
import cv2
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


#!pip install qreader
#https://googlechromelabs.github.io/chrome-for-testing/#stable - For Selenium drivers


# === Step 1: Decode QR code using QReader ===
image_path = r'C:\Users\Dell\Desktop\Python Scripts\DC_QR_Processing\GIT\Protogene\DC_QR_Project\Inputs\img1.jpg'
img = cv2.imread(image_path)

# Initialize QReader and decode
detector = QReader()
decoded_qrs, qr_locations = detector.detect_and_decode(image=img, return_detections=True)

# Check and extract URL
if not decoded_qrs:
    print("❌ No QR code found.")
    exit()

url = decoded_qrs[0]
print(f"✅ URL from QR: {url}")

# === Step 2: Load the URL using Selenium ===
service = Service(r"C:/WebDrivers/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

# Open the URL
driver.get(url)

# Wait for the table rows to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table//tr")))

# === Step 3: Extract Table Data ===
rows = driver.find_elements(By.XPATH, "//table//tr")
data = []
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if len(cells) == 2:
        key = cells[0].text.strip()
        val = cells[1].text.strip()
        data.append((key, val))

driver.quit()

# === Step 4: Convert to DataFrame and Display ===
df = pd.DataFrame(data, columns=["Field", "Value"])
print(df)
