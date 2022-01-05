from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome(executable_path="C:\\ChromeDriver\\ChromeDriver.exe")
browser.get(link)


bookbut = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,'price'),'$100'))
browser.find_element_by_xpath('//*[@id="book"]').click()

x = browser.find_element_by_xpath('//*[@id="input_value"]').text
int(x)
result = calc(x)
browser.find_element_by_xpath('//*[@id="answer"]').send_keys(result)
browser.find_element_by_xpath('/html/body/form/div/div/button').click()