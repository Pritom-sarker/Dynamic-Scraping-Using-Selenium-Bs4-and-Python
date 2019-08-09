from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from   selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
# driver.set_window_position(-10000,0)
driver.get("https://analytics2.rti.co.id/?m_id=1&sub_m=s2&sub_sub_m=4")

elem = driver.find_element_by_name('codefld2')
elem.send_keys("ABBA")
butt = driver.find_element_by_id("go")
butt.click()


wait = WebDriverWait( driver, 5 )

html=driver.page_source
driver.close()
f=open('page.html','w')
f.write(html)
f.close()