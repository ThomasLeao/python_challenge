from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

df = pd.read_excel("challenge.xlsx")
driver = webdriver.Chrome()
dados_pessoas = df.to_dict(orient='records')

driver.get("https://www.rpachallenge.com/")

driver.find_element(By.TAG_NAME,'button').click()

ulnome = {}
ulnome[1] = "Smith"
ulnome[2] = "Dorsey"
ulnome[3] = "Kipling"
ulnome[4] = "Robertson"
ulnome[5] = "Derrick"
ulnome[6] = "Marlowe"
ulnome[7] = "Hamm"
ulnome[8] = "Norton"
ulnome[9] = "Shelby"
ulnome[10] = "Palmer"

i = 1

for pessoas in dados_pessoas:

    driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').send_keys(pessoas ['Phone Number'])
    time.sleep(.5)

    driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys(pessoas ['First Name'])
    time.sleep(.5)


    driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').send_keys(pessoas ['Address'])
    time.sleep(.5)

    driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').send_keys(pessoas ['Company Name'])
    time.sleep(.5)

    driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').send_keys(pessoas ['Role in Company'])
    time.sleep(.5)

    driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys(ulnome[i])
    i = i + 1
    time.sleep(.5)

    
    driver.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').send_keys(pessoas ['Email'])
    time.sleep(.5)

    driver.find_element(By.XPATH,'/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()



t1 = driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/div[1]')

t2 = driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/div[2]')

completo = t1 + t2

print(completo)

time.sleep(1000)



print(df)

#
#



    






time.sleep(2)



#//*[@ng-reflect-name="labelPhone"]