import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

DATA = []

def locate_cbe():
    from_city = driver.find_element(By.ID, "fromCity")
    from_city.click()
    time.sleep(3)
    from_city_input_field = driver.find_element(By.XPATH,
                                                "//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/input")
    from_city_input_field.send_keys("CJB")
    time.sleep(2)
    driver.find_element(By.XPATH,
                                     '//*[@id="react-autowhatever-1-section-0-item-0"]/div/div[1]/p[1]').click()

def locate_dxb():
    to_city = driver.find_element(By.ID, "toCity")
    to_city.click()
    time.sleep(3)
    to_city_input_field = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/input')
    to_city_input_field.send_keys("DXB")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="react-autowhatever-1-section-0-item-0"]').click()



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.makemytrip.com/flights/")
time.sleep(5)

locate_cbe()
locate_dxb()
time.sleep(3)

arrow_button = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/span[2]').click()
time.sleep(2)

div = driver.find_elements(By.CLASS_NAME,"dateInnerCell")
dates = []
prices = []
for element in div:
    p_elements = element.find_elements(By.TAG_NAME,"p")
    for i,p_element in enumerate(p_elements):
        text = p_element.get_attribute("innerText")
        if i == 0:
            dates.append(text)
        if i == 1:
            prices.append(text)

data = {}
for i,date in enumerate(dates):
    data[i+1] = prices[i]

data = dict(list(data.items())[29:])
data = dict(list(data.items())[:6])

new = 1
old = 32
for i in range(0,4):
    data[new] = data[old]
    del data[old]
    new+=1
    old+=1

# data[1] = data[32]
# data[2] = data[33]
# data[3] = data[34]
# data[4] = data[35]
print(data)


# date = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[7]/div/p[1]').text
# price = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[7]/div/p[2]').text










time.sleep(3)
driver.close()


