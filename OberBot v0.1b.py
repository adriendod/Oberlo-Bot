from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *
import time

options = Options()
options.add_argument('--log-level=3')
options.add_argument('--user-data-dir=Profile S')
driver = webdriver.Chrome("chromedriver_mac64/chromedriver", options=options)

#Login AliExpress
def AliExpressLogIn(AliExpress_email, AliExpress_password):
	driver.get("https://login.aliexpress.com/")
	wait = WebDriverWait(driver, 15)
	wait.until(EC.frame_to_be_available_and_switch_to_it(0))

	aeEmail = driver.find_element_by_id("fm-login-id")
	aePassword = driver.find_element_by_id("fm-login-password")
	aeloginButton = driver.find_element_by_class_name("fm-submit")

	aeEmail.clear()
	aeEmail.send_keys(AliExpress_email)
	aePassword.send_keys(AliExpress_password)
	aeloginButton.click()

	#Wait for login
	try:
		element = WebDriverWait(driver, 10).until(
		        EC.presence_of_element_located((By.CLASS_NAME, "search-key-box"))
		    )
	except:
	    print("Login Failed")


def OberloLogIn(Oberlo_email, Oberlo_password):
	driver.get("https://app.oberlo.com")
	emailField = driver.find_element_by_name(Oberlo_email)
	passwordField = driver.find_element_by_name(Oberlo_password)
	loginButton = driver.find_element_by_class_name("login__button")

	emailField.send_keys(email)
	passwordField.send_keys(password)
	loginButton.click()

	print("Login OK")

def OberloLogOut():
	expandLogOut = driver.find_element_by_class_name('navigation-profile')
	expandLogOut.click()
	time.sleep(2)
	orderButton = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/ul/li[4]/a/div/div/div/span')
	orderButton.click()

def OberloCheckOrder():
	try:
		element = WebDriverWait(driver, 10).until(
		        EC.presence_of_element_located((By.CLASS_NAME, "search-key-box"))
		    )
	except:
	    print("Login Failed")


def OberloOrder():
	driver.get("https://app.oberlo.com/orders?states%5B%5D=0")
	#Start Order

	try:
		orderButton = driver.find_element_by_xpath('//*[@id="oberlo-merchant"]/div/div[2]/div[5]/div[2]/div[2]/div/div[1]/div[2]/div[1]/button')
	except:
		return

	orderName = driver.find_element_by_xpath('//*[@id="oberlo-merchant"]/div/div[2]/div[5]/div[1]/div[1]/div/div[1]/div[4]/a').text
	orderButton = driver.find_element_by_xpath('//*[@id="oberlo-merchant"]/div/div[2]/div[5]/div[2]/div[2]/div/div[1]/div[2]/div[1]/button')
	orderButton.click()

	#Switch to AliExpress Tab
	driver.implicitly_wait(2)
	handles = driver.window_handles;
	size = len(handles);
	for x in range(size):
		if handles[x] != driver.current_window_handle:
			driver.switch_to.window(handles[1])
			print (driver.title)

	time.sleep(20)

	#Checkout
	checkoutButton = driver.find_element_by_id("checkout-button")
	print("button found")
	checkoutButton.click()

	#Wait for payment to complete
	time.sleep(5)

	try:
		element = WebDriverWait(driver, 10).until(
		        EC.presence_of_element_located((By.CLASS_NAME, "search-key-box"))
		    )
	except:
	    print("Order Failed")

	driver.close()
	driver.switch_to.window(handles[0])

def OberloProcessing():
	driver.get("https://app.oberlo.com/orders?states%5B%5D=2")
	for i in range(10):
		processingXPath = '//*[@id="oberlo-merchant"]/div/div[2]/div['+ str(5 + i) +']/div[2]/div[2]/div/div[1]/div[2]/button[1]'
		try:
			processingButton = driver.find_element_by_xpath(processingXPath)
			processingButton.click()
		except:
			print("No Button "+str(i+1))


AliExpressLogIn(AliExpress_email, AliExpress_password)
OberloLogIn(Oberlo_email, Oberlo_password)

for _ in range(2):
    try:
        OberloOrder()
        break
    except:
    	print("Oberlo Order Freezed, retrying")

OberloProcessing()
OberloLogOut()
driver.close()  




