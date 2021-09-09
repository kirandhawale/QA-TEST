#test 1: Open wyscout platform
from selenium import webdriver


#df = pd.read_excel (r'Path where the Excel file is stored\File name.xlsx') 

#driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path="C:\\Users\\Mudra\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")

driver.implicitly_wait(30)

driver.maximize_window()

driver.get("https://platformrc.wyscout.com/app/ ")

driver.implicitly_wait(10)

driver.find_element_by_name("username").send_keys("kirandhawale00@gmail.com")

driver.implicitly_wait(30)



driver.find_element_by_name("password").send_keys("pw_IndiaTest!")


driver.implicitly_wait(30)
driver.find_element_by_id("login_button").click()

#driver.implicitly_wait(160)




#driver.close()
driver.quit()
print("Test Completed")