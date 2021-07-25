from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import numpy as np
import pandas 
import random


  
# Bước 1: Tu dong tim kiem thong tin     
driver = webdriver.Chrome("D:/Minh/python/Machine Learning/chromedriver.exe")
url = "https://thanhnien.vn/giao-duc/tuyen-sinh/2020/tra-cuu-diem-thi-thpt-quoc-gia.html"
driver.get(url)
sleep(2)


id = []
result = []
st = 45004567
step = 10
print("Truong Thanh Minh")

for i in range (st, st + step + 10):

    id = []
    sbd = driver.find_element_by_id('txtkeyword')
    sbd.send_keys(i)
    sleep(0.5)
    tim_kiem = driver.find_element_by_id('btnresult')
    tim_kiem.click()
    sleep(0.5)
    hoten = driver.find_element_by_xpath('/html/body/form/div[2]/div/div[1]/div/div[3]/section[2]/div/table/tbody/tr/td[3]').text
    toan = driver.find_element_by_xpath('/html/body/form/div[2]/div/div[1]/div/div[3]/section[2]/div/table/tbody/tr/td[7]').text
    van = driver.find_element_by_xpath('/html/body/form/div[2]/div/div[1]/div/div[3]/section[2]/div/table/tbody/tr/td[8]').text
    li = driver.find_element_by_xpath('/html/body/form/div[2]/div/div[1]/div/div[3]/section[2]/div/table/tbody/tr/td[9]').text
    hoa = driver.find_element_by_xpath('/html/body/form/div[2]/div/div[1]/div/div[3]/section[2]/div/table/tbody/tr/td[10]').text
    sinh = driver.find_element_by_xpath('/html/body/form/div[2]/div/div[1]/div/div[3]/section[2]/div/table/tbody/tr/td[11]').text
    su = driver.find_element_by_xpath('/html/body/form/div[2]/div/div[1]/div/div[3]/section[2]/div/table/tbody/tr/td[13]').text
    dia = driver.find_element_by_xpath('/html/body/form/div[2]/div/div[1]/div/div[3]/section[2]/div/table/tbody/tr/td[14]').text
    cd = driver.find_element_by_xpath('/html/body/form/div[2]/div/div[1]/div/div[3]/section[2]/div/table/tbody/tr/td[15]').text
    anh = driver.find_element_by_xpath('/html/body/form/div[2]/div/div[1]/div/div[3]/section[2]/div/table/tbody/tr/td[17]').text
    id.extend([i, hoten, toan, van, anh, li, hoa, sinh, su, dia, cd])
    result.append(id)    
    del id
    sbd = driver.find_element_by_id('txtkeyword')
    sbd.clear()
    sleep(random.randint(2, 5))
    
    
my_array = np.array(result)
df = pandas.DataFrame(my_array, columns = ['Số báo danh', 'Họ và tên', 'Toán', 'Văn', 'Anh', 'Lí', 'Hóa', 'Sinh', 'Sử', 'Địa', 'CD'])
df.to_csv('hihi.csv', encoding='utf-8-sig')
