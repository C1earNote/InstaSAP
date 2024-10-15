from selenium import webdriver
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://kiitportal.kiituniversity.net/irj/portal/")
url = "https://kiitportal.kiituniversity.net/irj/portal/"
response = requests.get(url)

rollno = driver.find_element("id", "logonuidfield")
rollno.send_keys("22053297")
passw = driver.find_element("id", "logonpassfield")
passw.send_keys("Tnigamcom@1")
submitButton = driver.find_element("name", "uidPasswordLogon")
submitButton.click()

selfservice = driver.find_element("id","navNodeAnchor_1_1")
selfservice.click()

soup = BeautifulSoup(response.text, 'html.parser')

# Find the link with the text "Student Self Service"
link = soup.find('a', string="Student Self Service")


input("Press Enter to close the browser...")
driver.quit()
