from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook

driver=webdriver.Chrome(executable_path="C:\\Users\\Ajit\\chromedriver.exe")
driver.get("https://dermnetnz.org/image-library/")
driver.implicitly_wait(10)
disease_name=driver.find_elements(By.XPATH,"//*[@class='imageList__group__item__copy']/h6")
disease_image=driver.find_elements(By.XPATH,"//*[@class='imageList__group__item__image']/img")
disease_url=driver.find_elements(By.XPATH,"//a[@class='imageList__group__item']")

#1) Name of Diseases
disease_data=[]
for disease in disease_name:
    disease_data.append(disease.text)

#2)Icon images of diseases.
img_data=[]
for img in disease_image:
    img_data.append(img.get_attribute('src'))

#3) URLs associated with diseases
url_data=[]
for lnk in disease_url:
    url_data.append(lnk.get_attribute('href'))

data=zip(disease_data,img_data,url_data)

# saving data into a file
wb=Workbook()
wb['Sheet'].title='Disease Data'
sh1=wb.active
sh1.append(['Name','Image','Url' ])
for x in list(data):
    sh1.append(x)
wb.save('DiseaseRecords.xlsx')
