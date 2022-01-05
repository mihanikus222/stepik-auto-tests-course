from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome(executable_path="C:\\ChromeDriver\\ChromeDriver.exe")
browser.get(link)

browser.find_element_by_xpath('/html/body/div/form/div/input[1]').send_keys("Ivan")
browser.find_element_by_xpath('/html/body/div/form/div/input[2]').send_keys("Petrov")
browser.find_element_by_xpath('/html/body/div/form/div/input[3]').send_keys("mail")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'a.txt') 
element = browser.find_element_by_xpath('//*[@id="file"]')
element.send_keys(file_path)
browser.find_element_by_xpath('/html/body/div/form/button').click()


#ЗАГРУЗКА ФАЙЛА НА САЙТ
