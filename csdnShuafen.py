from selenium import webdriver
from selenium.webdriver.remote import webelement
import time
i=0;
path="F:\pythonjiaoben\chromedriver_win32\chromedriver.exe"
url="https://blog.csdn.net/qq_26024867/article/details/81783370"
options=webdriver.ChromeOptions()

prefs={
     'profile.default_content_setting_values': {
        'images': 2,
        'javascript':2
    }
}
options.add_experimental_option('prefs',prefs)
options.set_headless()
while(i<1000):
    driver = webdriver.Chrome(executable_path=path,chrome_options=options)
    driver.get(url)
    i=i+1
    time.sleep(30)
    driver.close()